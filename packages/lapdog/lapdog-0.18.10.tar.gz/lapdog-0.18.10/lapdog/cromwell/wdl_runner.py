#!/usr/bin/python

# Copyright 2017 Google Inc.
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

# wdl_runner.py
#
# This script is a wrapper around Cromwell, which will:
#
# 1- take as input:
#     * a WDL file to describe a workflow
#     * a JSON file to describe the inputs
#     * a Google Cloud project ID (ignored if on GCE) to run in
#     * a GCS path to a Cromwell "working directory"
#     * a GCS path to an "output directory"
#
# 2- launch a local instance of Cromwell
#
# 3- submit the inputs to Cromwell to run the workflow
#
# 4- copy the Cromwell run metadata ('wdl_run_metadata.json') to the
#        output directory
#
# 5- copy the Cromwell outputs to the output directory
#
# Cromwell can be found at:
#     https://github.com/broadinstitute/cromwell

import argparse
import json
import logging
import os
import requests
import traceback

import cromwell_driver
from cromwell_driver import gce_get_metadata
import file_util
import sys_util
import tempfile

WDL_RUN_METADATA_FILE = 'wdl_run_metadata.json'


class Runner(object):

    def __init__(self, args, environ):
        self.args = args

        # Fetch all required environment variables, exiting if unset.
        self.environ = sys_util.copy_from_env(
                ['CROMWELL', 'CROMWELL_CONF'], environ)
        cromwell_conf = self.environ['CROMWELL_CONF']
        cromwell_jar = self.environ['CROMWELL']

        # Verify that the output directory is empty (or not there).
        if not file_util.verify_gcs_dir_empty_or_missing(self.args.output_dir):
            sys_util.exit_with_error(
                    "Output directory not empty: %s" % self.args.output_dir)

        # Plug in the working directory and the project id to the Cromwell conf
        self.fill_cromwell_conf(cromwell_conf,
                                                        self.args.working_dir, self.args.project)

        # Set up the Cromwell driver
        self.driver = cromwell_driver.CromwellDriver(cromwell_conf, cromwell_jar)
        if not self.args.batch:
            self.driver.start(3)

    def fill_cromwell_conf(self, cromwell_conf, working_dir, project):
        try:
            project_id = gce_get_metadata('project/project-id')

            if project and project != project_id:
                logging.warning("Overridding project ID %s with %s",
                                                project, project_id)

        except requests.ConnectionError as e:
            logging.warning(
                    "URLError trying to fetch project ID from Compute Engine metdata")
            logging.warning(e)
            logging.warning("Assuming not running on Compute Engine")

            project_id = project

        new_conf_data = file_util.file_safe_substitute(cromwell_conf, {
                'project_id': project_id,
                'working_dir': working_dir
                })

        with open(cromwell_conf, 'w') as f:
            f.write(new_conf_data)

    def copy_workflow_metadata(self, metadata, metadata_filename):

        logging.info("Copying run metadata to %s", self.args.output_dir)

        # Copy the run metadata
        with open(metadata_filename, 'w') as f:
            json.dump(metadata, f)

        file_util.gsutil_cp([metadata_filename], "%s/" % self.args.output_dir)


    def run(self):
        if self.args.batch is not None:
            try:
                file_util.gsutil_cp([os.environ['SUBMISSION_DATA_PATH']], 'submission.json')
                with open('submission.json') as r:
                    submission_data = json.load(r)
                runtime = submission_data['runtime'] if 'runtime' in submission_data else None
                self.driver.start(runtime['memory'] if runtime is not None else 3)
                logging.info("Starting batch request")
                # logging.info("SUBMITTING JOB " + repr((
                #     self.args.batch,
                #     self.args.wdl,
                #     self.args.workflow_inputs,
                #     self.args.workflow_options,
                #     runtime['batch_limit'] if runtime is not None else 250,
                #     runtime['query_limit'] if runtime is not None else 100
                # )))
                job_data = self.driver.batch(
                    self.args.batch,
                    self.args.wdl,
                    self.args.workflow_inputs,
                    self.args.workflow_options,
                    runtime['batch_limit'] if runtime is not None else 250,
                    runtime['query_limit'] if runtime is not None else 100
                )
                logging.info("Copying execution output file")
                with open('workflows.json', 'w') as w:
                    json.dump(
                        job_data,
                        w,
                        indent=2
                    )
                file_util.gsutil_cp(['workflows.json'], self.args.output_dir+'/')
                for data in job_data:
                    logging.info("Workflow %s exited with status %s" % (data['workflow_id'], data['workflow_status']))
                    # if data['workflow_output'] is not None:
                    #     metadata_filename = '%s.%s' % (
                    #         data['workflow_id'],
                    #         WDL_RUN_METADATA_FILE
                    #     )
                    #     with open(metadata_filename, 'w') as w:
                    #         json.dump(
                    #             data['workflow_metadata'],
                    #             w,
                    #             indent=2
                    #         )
                    #     file_util.gsutil_cp([metadata_filename], self.args.output_dir+'/')
                logging.info("Run complete")
                statuses = {wf['workflow_status'] for wf in job_data}
                # infer status then get submission object
                file_util.gsutil_cp([os.environ['SUBMISSION_DATA_PATH']], 'submission.json')
                with open('submission.json') as r:
                    submission_data = json.load(r)
                if len(statuses) == 1 and 'Succeeded' in statuses:
                    submission_data['status'] = 'Succeeded'
                elif 'Aborted' in statuses:
                    submission_data['status'] = 'Aborted'
                elif 'Failed' in statuses:
                    submission_data['status'] = 'Failed'
                else:
                    submission_data['status'] = 'Error'
                    submission_data['error-details'] = {
                        'message': "Unable to resolve the final status of this submission",
                        'encountered-statuses': list(statuses)
                    }
                    self.driver.log(
                        'Unknown job exit status',
                        json=job_data,
                        severity='WARNING'
                    )
                with open('submission.json', 'w') as w:
                    json.dump(submission_data, w, indent=2)
                file_util.gsutil_cp(['submission.json'], os.environ['SUBMISSION_DATA_PATH'])
                self.driver.logger.log(
                    'Cromwell complete. Flushing logs',
                    json=submission_data,
                    severity='DEBUG'
                )
                return
            except:
                self.driver.logger.log_exception()
                logging.error("Batch submission failed: " + traceback.format_exc())
                file_util.gsutil_cp([os.environ['SUBMISSION_DATA_PATH']], 'submission.json')
                with open('submission.json') as r:
                    submission_data = json.load(r)
                submission_data['status'] = 'Error'
                submission_data['error-details'] = {
                    'message': "Lapdog wrappers encountered an unhandled exception",
                    'stack-trace': traceback.format_exc()
                }
                with open('submission.json', 'w') as w:
                    json.dump(submission_data, w, indent=2)
                file_util.gsutil_cp(['submission.json'], os.environ['SUBMISSION_DATA_PATH'])
                return
        logging.info("starting")

        # Submit the job to the local Cromwell server
        (result, metadata) = self.driver.submit(
            self.args.wdl,
            self.args.workflow_inputs,
            self.args.workflow_options
        )
        logging.info(result)

        # Copy run metadata and output files to the output directory
        self.copy_workflow_metadata(metadata, WDL_RUN_METADATA_FILE)

        logging.info("run complete")


def main():
    parser = argparse.ArgumentParser(description='Run WDLs')
    parser.add_argument('--wdl', required=True,
                                            help='The WDL file to run')
    parser.add_argument('--workflow-inputs', required=True,
                                            help='The workflow inputs (JSON) file')
    parser.add_argument('--workflow-options', required=False,
                                            help='The workflow options (JSON) file')
    parser.add_argument('--project', required=False,
                                            help='The Cloud project id')
    parser.add_argument('--working-dir', required=True,
                                            help='Location for Cromwell to put intermediate results.')
    parser.add_argument('--output-dir', required=True,
                                            help='Location to store the final results.')
    parser.add_argument('--batch', help="Submit batch request", default=None)


    args = parser.parse_args()

    # Sanitize the working and output paths
    args.working_dir.rstrip('/')
    args.output_dir.rstrip('/')

    # Write logs at info level
    FORMAT = '%(asctime)-15s %(module)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)

    # Don't info-log every new connection to localhost, to keep stderr small.
    logging.getLogger("urllib3.connectionpool").setLevel(logging.WARNING)
    logging.getLogger("requests.packages.urllib3.connectionpool").setLevel(
            logging.WARNING)

    runner = Runner(args, os.environ)
    runner.run()


if __name__ == '__main__':
    try:
        main()
    finally:
        print("<<<EOF>>>")
