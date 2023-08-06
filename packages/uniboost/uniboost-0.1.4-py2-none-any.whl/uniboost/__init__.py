#!/user/bin/env python3 
"""
uniboost.py: This program is used for Rancher purposes.
Requirements: python2.7 or later.
"""

__author__ = "Michael Shobitan"
__copyright__ = "Copyright 2019, BTCS Platform Engineering"
__credits__ = ["Michael Shobitan"]
__license__ = "PFE"
__version__ = "0.0.9"
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

def latest():
    script = subprocess.Popen(["pip", "install", "uniboost", "-U"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    this_out, this_err = script.communicate()
    return this_out

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

def hi():
    print("Hi")

def file_exist(self, this_file):
    status = os.path.exists(this_file)
    if(status == True):
        if(os.path.isdir(this_file)):
            file_type = 'directory'
            # print(file_type)
        elif(os.path.isfile(this_file)):  
            file_type = 'file'
            # print(file_type)
        else:
            print("It is a special file (socket, FIFO, device file, etc.)" )
        status = 'exist'
    else:
        file_type = status
        status = status

    return file_type, status