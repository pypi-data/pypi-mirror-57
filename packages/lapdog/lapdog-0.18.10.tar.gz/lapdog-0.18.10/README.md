# Lapdog

[![PyPI](https://img.shields.io/pypi/v/lapdog.svg)](https://pypi.io/project/lapdog)

A relaxed wrapper for dalmatian and FISS

## Prerequisites
* Lapdog requires MacOS or Linux. Windows is not officially supported
* Lapdog requires Python >= 3.3
* Lapdog requires the Google Cloud SDK, which can be installed [here](https://cloud.google.com/sdk/).
    * Your `gcloud --version` should be at least `252.0.0`. If it is not, please run `gcloud components update`
* Lapdog uses your Gcloud application-default credentials
    * Use `gcloud auth application-default login` and `gcloud config set account {account}` before running Lapdog
* Lapdog requires the Alpha and Beta suite for Gcloud
    * Alpha and Beta suite can be installed with `gcloud components install alpha beta`
* (Optional) The Lapdog User Interface requires node and npm, which can be installed using your system's package manager
    * MacOS: `brew install node npm`
    * Linux: Install through system package manager or [from source](https://nodejs.org/en/download/)
    * Lapdog requires `node --version` >= 10.15.1
    * Lapdog requires `npm --version` >= 6.4.1

## Installing
1. Install lapdog via pip: `pip install lapdog`
    - If you already have lapdog installed, you can upgrade it with
    `pip install --upgrade lapdog`
    - If you encounter an error with PyYAML see the [PyYaml Note](#pyyaml-note) below
2. (Optional) Enable the Lapdog User Interface:
    - The UI runs locally by default. If you are installing Lapdog on a server, you'll
    need to set up an SSH tunnel for ports 4200 and 4201
    - Install `node` and `npm` if you don't already have them installed
        - If you're on Mac OS, run `brew install node npm`
    - Run `lapdog ui --install`. This may take a while

## Usage
1. `lapdog` may be imported within python as a drop-in replacement for `dalmatian`
    - lapdog presents a superset of features available in dalmatian
    - `WorkspaceManager`s in lapdog cache data when communicating with Firecloud.
    If Firecloud experiences an intermittent failure, the `WorkspaceManager` may be
    able to continue running in offline mode. Calling `WorkspaceManager.sync()` will
    reconnect to Firecloud, pushing out any data updates that were queued while in offline mode
    - `WorkspaceManager`s in lapdog present the execution api via `WorkspaceManager.execute()`.
    Executions differ from submissions in that they run directly on Google and results are
    uploaded back to Firecloud afterwards
2. `lapdog` may be used as a command line tool.
    - The tool provides the necessary functions to create a workspace, fill it with data,
    import or upload methods and configurations, and submit jobs (or execute them directly)
    - Run `lapdog --help` to get the list of available commands
3. `lapdog` may be used via an interactive user interface which serves to run and
  monitor lapdog executions
    - Run `lapdog ui` to launch the user interface

## Job Execution

Lapdog executes jobs through dedicated Google Projects ("Engines") for each FireCloud Namespace.
A Lapdog Engine can only be initialized for a given Namespace by a billing account admin.
To initialize a new Engine, contact your Namespace admin and ask them to run `lapdog initialize-project`.

After an Engine is initialized, you will have to register with it:

* The Lapdog User Interface will automatically register you when you load a workspace
in a namespace that you're not registered to
* The Lapdog python module supports manual registration
    * When you create a `WorkspaceManager` in an unregistered Namespace, you will get a warning
    * You can also check your registration status by checking the value of `WorkspaceManager.gateway.registered`
    * You can then register by using `WorkspaceManager.gateway.register()`
    * If registration fails due to any FireCloud errors, simply wait a few minutes
    then try calling `register()` again
* The Lapdog CLI does not support registration. You can register through the UI or
python module

### Workspace Permissions

In the UI, at the bottom of every page, you will find a **firecloud.org** email.
This is a proxy group email which contains you, and all your service accounts.
To allow the Lapdog Engine to run jobs, that proxy group email must be granted
WRITE access to FireCloud workspaces where jobs will run. You may grant the group
READ access to workspaces where data will be read from, but jobs cannot execute
in workspaces without WRITE permissions. The proxy group email can be found by
calling `lapdog.cloud.proxy_group_for_user(YOUR_EMAIL)`.

**NOTE:** Due to a bug in FireCloud, permissions will not be granted if the group
was already granted access to a workspace before you registered to that namespace's
Lapdog Engine. If your proxy email definitely was granted access to a workspace,
but your jobs are still failing with permissions errors, try removing access and then
re-granting it. You can see FireCloud's response to this bug report [here](https://gatkforums.broadinstitute.org/firecloud/discussion/23350/account-not-inheriting-permissions-when-added-to-group)

---

### Roadmap

See the [milestones page](https://github.com/broadinstitute/lapdog/milestones) to
read the development roadmap.

### Pro/Con with Firecloud

##### Pros
* Each submission has a dedicated Cromwell instance. Your jobs will never queue, unless you hit a Google usage quota
* Lapdog supports Requester Pays buckets and GPUs
* Workspace cache: Lapdog caches most data received from Firecloud.
    * In the event of a Firecloud error, Lapdog will attempt to keep running by using it's cached data. Any data updates will by pushed back to Firecloud when the workspace is synced
* Data caches: The Lapdog API caches data sent to the UI and read from Google
    * These caches greatly improve UI performance by storing results whenever possible
* Streamlined UI: The Lapdog UI was built with efficiency in mind
* Quality of life features:
    * Save time updating methods. Set `methodRepoMethod.methodVersion` to "latest" and let Lapdog figure out what the snapshot ID is
    * Easy data uploads. Call `prepare_entity_df` on a DataFrame before uploading to Firecloud. Any local filepaths will be uploaded to the workspace's bucket in the background and a new DataFrame will be returned containing the new `gs://` paths
    * Automatic reference uploads. When you call `update_attributes`, any values which refer to local filepaths will be uploaded in the background (just like `prepare_entity_df`). `update_attributes` now returns a dictionary containing the attributes exactly as uploaded

##### Cons
* You pay an additional 5c/hour fee for each submission to run the Cromwell server
* Submission results must be manually uploaded to Firecloud by clicking the `Upload Results` button in the UI.
* There are small overhead costs billed to the Lapdog Engine for operation. These costs
are for calls to the API and for storage of metadata, both of which should be very cheap

## PyYAML Note

Often, when installing Lapdog, the installation fails when upgrading PyYAML because
it is unable to uninstall the current PyYAML version.

This is because some older versions of PyYAML were distributed through `distutils`
which prevents packages from being uninstalled. New versions of PyYAML are distributed
through `setuptools` which can be successfully uninstalled.

To resolve this issue, navigate to your Python site-packages directory. The site-packages
directory usually ends with `.../lib/python{version}/site-packages/`. The exact location
depends on your platform, environment manager, and python configuration.

* For anaconda, this path is within anaconda's installation folder: `/{path to anaconda}/envs/{environment}/lib/python{version}/site-packages`
* For virtualenvs, this path is within the environment's installation folder: `/{path to environment}/lib/python{version}/site-packages`
* For system python on Unix systems: `/usr/local/lib/python{version}/site-packages`

An easy way to locate this folder is to open python and then:
```python
import yaml
yaml
```

This expression will evaluate and print the path to the `yaml` module, which will be
within your site-packages directory.

After locating the site-packages directory, you must remove the following two directories:
* `.../site-packages/yaml/`
* `.../site-packages/PyYAML*.egg-info`

Once removed, you can try the installation command for lapdog again.
