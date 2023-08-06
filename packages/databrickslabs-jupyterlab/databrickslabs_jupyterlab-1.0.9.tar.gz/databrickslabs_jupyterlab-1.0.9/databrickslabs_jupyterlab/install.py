import json
import os
import re
import subprocess
import sys
import tempfile

import databrickslabs_jupyterlab
from databrickslabs_jupyterlab.remote import get_python_path, get_remote_packages
from databrickslabs_jupyterlab.local import print_ok, print_error
from databrickslabs_jupyterlab.utils import bye


WHITELIST = [
    "boto3", "jsonschema", "hyperopt", "keras-applications", "keras-preprocessing", "keras", "lxml", "matplotlib",
    "mleap", "mlflow", "numba", "numpy", "pandas", "patsy", "pillow", "pyarrow", "python-dateutil", "pyparsing",
    "scikit-learn", "scipy", "seaborn", "simplejson", "statsmodels", "tabulate", "tensorboard",
    "tensorboardx", "tensorflow-estimator", "tensorflow", "torch", "torchvision", "urllib3"
]

BLACKLIST = [
    "absl-py", "ansi2html", "asn1crypto", "astor", "attrs", "backcall", "backports.shutil-get-terminal-size", "bcrypt",
    "bleach", "blessings", "brewer2mpl", "certifi", "cffi", "chardet", "click", "colorama", "configobj", "configparser",
    "cryptography", "cycler", "cython", "databricks-cli", "databrickslabs-jupyterlab", "decorator", "defusedxml",
    "docker", "docopt", "docutils", "entrypoints", "enum34", "et-xmlfile", "flask", "freetype-py", "funcsigs", "fusepy",
    "future", "gast", "gitdb2", "gitpython", "grpcio", "gunicorn", "h5py", "horovod", "html5lib", "idna", "inquirer",
    "ipaddress", "ipykernel", "ipython", "ipython-genutils", "ipywidgets", "itsdangerous", "jdcal", "jedi", "jinja2",
    "jmespath", "jsonschema", "jupyter-client", "jupyter-core", "llvmlite", "mako", "markdown", "markupsafe", "mistune",
    "mkl-fft", "mkl-random", "mock", "msgpack", "msgpack-python", "nbconvert", "nbformat", "ndg-httpsclient",
    "networkx", "nose", "nose-exclude", "notebook", "olefile", "openpyxl", "openpyxl", "packaging", "pandocfilters",
    "paramiko", "parso", "pathlib2", "pexpect", "pickleshare", "pip", "ply", "prometheus-client", "prompt-toolkit",
    "protobuf", "psutil", "psycopg2", "ptyprocess", "py4j", "pyasn1", "pycparser", "pycurl", "pygments", "pygobject",
    "pymongo", "pynacl", "pypng", "pysocks", "python-apt", "python-dateutil", "python-editor", "python-geohash",
    "pyopenssl", "pytz", "pyyaml", "pyzmq", "querystring-parser", "readchar", "requests", "scour", "send2trash",
    "setuptools", "sidecar", "simplegeneric", "singledispatch", "six", "smmap2", "sqlparse", "ssh-config",
    "ssh-import-id", "tabulate", "termcolor", "terminado", "testpath", "texttable", "tornado", "tqdm", "traitlets",
    "unattended-upgrades", "version-parser", "virtualenv", "wcwidth", "webencodings", "websocket-client", "werkzeug",
    "wheel", "widgetsnbextension", "wrapt"]

def execute(cmd):
    try:
        result = subprocess.call(cmd)
    except Exception as ex:
        print_error(ex)
        result = 1
    return {"returncode": result}

def execute_script(script, script_name, success_message, error_message):
    with tempfile.TemporaryDirectory() as tmpdir:
        script_file = os.path.join(tmpdir, script_name)
        with open(script_file, "w") as fd:
            fd.write(script)

        result = execute(["bash", script_file])
        if result["returncode"] != 0:
            print_error(error_message)
            sys.exit(1)
        else:
            print_ok(success_message)

def validate(env_name=None, labext=False):
    if env_name is None:
        script = """#!/bin/bash
        set -e
        """
    else:
        script = """#!/bin/bash
        set -e
        source $(conda info | awk '/base env/ {print $4}')/bin/activate "%s"
        """ % env_name

    if labext:
        script += """
            jupyter-labextension list
        """
    else:
        script += """
            pip show databrickslabs_jupyterlab
            jupyter-serverextension list
        """

    print("* Validating conda environment")
    execute_script(script, "validate_env.sh", 
        "Successfully validated conda environment", 
        "Error while validating conda environment")

def update_env(env_file):
    script = """#!/bin/bash
    conda env update --file %s
    """ % (env_file)

    print("* Updating conda environment")
    execute_script(script, "update_env.sh", 
        "Successfully updated conda environment", 
        "Error while updating conda environment")
    validate()

def install_env(env_file, env_name):
    script = """#!/bin/bash
    conda env create -n %s -f %s
    """ % (env_name, env_file)

    print("* Installing conda environment %s" % env_name)
    execute_script(script, "install_env.sh", 
        "Successfully installed conda environment",
        "Error while installing conda environment")
    validate(env_name)


def install_labextensions(labext_file, env_name=None):
    if env_name is None:
        script = """#!/bin/bash
        """
    else:
        script = """#!/bin/bash
        source $(conda info | awk '/base env/ {print $4}')/bin/activate "%s" 
        """ % env_name

    script += ("""
        jupyter labextension install --no-build $(cat %s)
        jupyter lab build --dev-build=True
    """ % labext_file)

    print("* Installing jupyterlab extensions")
    execute_script(script, "install_labext.sh", 
        "Successfully installed jupyter labextensions",
        "Error while installing jupyter labextensions")
    validate(env_name, labext=True)

def update_local():
    module_path = os.path.dirname(databrickslabs_jupyterlab.__file__)

    env_file = os.path.join(module_path, "lib/env.yml")
    update_env(env_file)

    labext_file = os.path.join(module_path, "lib/labextensions.txt")
    install_labextensions(labext_file)
    usage(os.environ.get("CONDA_DEFAULT_ENV", "unknown"))


def install(profile, host, token, cluster_id, cluster_name, use_whitelist):
    print("\n* Installation of local environment to mirror a remote Databricks cluster")
    result = get_remote_packages(cluster_id, host, token)
    if result[0] != 0:
        print_error(result[1])
        bye(1)
    libs = json.loads(result[1])

    if use_whitelist:
        print_ok("   => Using whitelist to select packages")
        ds_libs = [lib for lib in libs if lib["name"].lower() in WHITELIST]
    else:
        print_ok("   => Using blacklist to select packages")
        ds_libs = [lib for lib in libs if lib["name"].lower() not in BLACKLIST]

    ds_yml = ""
    for lib in ds_libs:
        if lib["name"] == "python":  # just artificially added
            python_version = lib["version"]
        else:
            if lib["name"] in ["hyperopt", "torchvision"]:
                r = re.compile(r"(\d+\.\d+.\d+)(.*)")
                version = r.match(lib["version"]).groups()[0]
            elif lib["name"] in ["tensorboardx"]:
                r = re.compile(r"(\d+\.\d+)(.*)")
                version = r.match(lib["version"]).groups()[0]
            else:
                version = lib["version"]
            ds_yml += ("    - %s==%s\n" % (lib["name"], version))

    module_path = os.path.dirname(databrickslabs_jupyterlab.__file__)
    env_file = os.path.join(module_path, "lib/env.yml")
    with open(env_file, "r") as fd:
        master_yml = fd.read()
    lines = master_yml.split("\n")
    for i in range(len(lines)):
        if lines[i].startswith("dependencies"):
            lines.insert(i+1, "  - python=%s" % python_version)
            break
    master_yml = "\n".join(lines)

    print("\n Installed environment \n")
    print(master_yml)
    print("\n    # Data Science Libs\n")
    print(ds_yml + "\n")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        env_file = os.path.join(tmpdir, "env.yml")
        with open(env_file, "w") as fd:
            fd.write(master_yml)
            fd.write("\n    # Data Science Libs\n")
            fd.write(ds_yml)
            fd.write("\n")

        env_name = cluster_name.replace(" ", "_")
        answer = input("    => Provide a conda environment name (default = %s): " % env_name)
        if answer != "":
            env_name = answer.replace(" ", "_")

        install_env(env_file, env_name)

        labext_file = os.path.join(module_path, "lib/labextensions.txt")
        install_labextensions(labext_file, env_name)

    usage(env_name)


def usage(env_name):
    print_ok("""
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
                              Q U I C K S T A R T
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

Prerequisites:
--------------

- Install Databricks CLI and configure profile(s) for your cluster(s)

  AWS: https://docs.databricks.com/user-guide/dev-tools/databricks-cli.html)
  Azure: https://docs.azuredatabricks.net/user-guide/dev-tools/databricks-cli.html

- Create an ssh key pair called ~/.ssh/id_<profile> for each cluster and 
  add the public key to the cluster SSH configuration


databrickslabs-jupyterlab:
--------------------------

1) Show help

    conda activate %s
    databrickslabs-jupyterlab -h

2) Create jupyter kernel for remote cluster

    Databricks on AWS:
        databrickslabs-jupyterlab <profile> -k [-i cluster-id]
    
    Azure Databricks:
        databrickslabs-jupyterlab <profile> -k -o <organisation>

3) Compare local and remote python package versions
    
    databrickslabs-jupyterlab <profile> -v all|same|diff

4) Copy Personal Access token for databricks cluster to cipboard (same on AWS and Azure)

    databrickslabs-jupyterlab <profile> -c

5) Start jupyter lab to use the kernel(s) created in 2)

    databrickslabs-jupyterlab <profile> -l [-i cluster-id]


6) Check currently available profiles 

    databrickslabs-jupyterlab -p

7) Download a demo notebook from docs.databricks.com (experimental)

    databrickslabs-jupyterlab -n https://docs.databricks.com/_static/notebooks/delta/xyz.html


""" % env_name)
