#!/user/bin/env python3 
"""
uniboost.py: This program is used for Rancher purposes.
Requirements: python2.7 or later.
"""

__author__ = "Michael Shobitan"
__copyright__ = "Copyright 2019, BTCS Platform Engineering"
__credits__ = ["Michael Shobitan"]
__license__ = "PFE"
__version__ = "0.0.4"
__maintainer__ = "Michael Shobitan"
__email__ = "michael.shobitan@pfizer.com"
__status__ = "Development"

import os
import re
import sys
import json
import time
import atexit
import shutil
import argparse
import subprocess

def set_env_var(var_name, var_value):
    os.environ[var_name] = var_value
    
def get_env_var(var_name):
    path = os.environ[var_name]
    return path

def file_to_json(json_file):
    with open(json_file, 'r') as handle:
        parsed = json.load(handle)
    return parsed

def jsonPP(json_content):
    response = json.dumps(json_content, indent=4)
    return response

def cd(cd_dir):
    os.chdir(cd_dir)

def pwd():
    cwd = os.getcwd()
    return cwd