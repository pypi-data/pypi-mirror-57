from setuptools import setup
import os
import re

with open(os.path.join(os.path.dirname(__file__), 'lapdog', '__init__.py')) as r:
    version = re.search(r'__version__ = \"(\d+\.\d+\.\d+[-_a-zA-Z0-9]*)\"', r.read()).group(1)

with open('requirements.txt') as r:
    requirements = r.readlines()

with open('README.md') as r:
    readme = r.read()

setup(
    name = 'lapdog',
    version = version,
    packages = [
        'lapdog',
        'lapdog.api',
        'lapdog.cloud'
    ],
    package_data={
        '':[
            'cromwell/wdl_pipeline.yaml',
            'cromwell/LICENSE',
            'cromwell/README.md',
            'vue/.babelrc',
            'vue/index.html',
            'vue/package.json',
            'vue/webpack.config.js',
            'vue/src/main.js',
            'vue/src/App.vue',
            'vue/src/Pages/*.vue',
            'vue/src/Components/*.vue',
            'api/swagger/lapdog.yaml',
            'wdl_pipeline.yaml'
        ],
    },
    description = 'A relaxed wrapper for FISS and dalmatian',
    url = 'https://github.com/broadinstitute/lapdog',
    author = 'Aaron Graubert - Broad Institute - Cancer Genome Computational Analysis',
    author_email = 'aarong@broadinstitute.org',
    long_description = readme,
    long_description_content_type='text/markdown',
    entry_points = {
        'console_scripts': [
            'lapdog = lapdog.__main__:main'
        ]
    },
    install_requires = requirements,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: System :: Clustering",
        "Topic :: System :: Distributed Computing",
        "License :: OSI Approved :: MIT License"
    ],
    license="MIT"
)
