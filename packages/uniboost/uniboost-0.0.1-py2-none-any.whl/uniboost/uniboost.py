#!/user/bin/env python3 
"""
rancher2Wrapper.py: This program is used for Rancher purposes.
Requirements: python3.7 or later.
"""

__author__ = "Michael Shobitan"
__copyright__ = "Copyright 2019, BTCS Platform Engineering"
__credits__ = ["Michael Shobitan"]
__license__ = "PFE"
__version__ = "0.1.0"
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

# os.environ['ANSIBLE_HOME'] = "/var/tmp/shobim/Scripts/Python"
# ansible_path = os.environ['ANSIBLE_HOME']
# json_file = "ansible.json"

def test():
    print("Hi")

def jsonPP(json_content):
    response = json.dumps(json_content, indent=4)
    return response

def change_dir(cd_dir):
    os.chdir(cd_dir)

def pwd():
    cwd = os.getcwd()
    return cwd

# change_dir(ansible_path)

# def file_to_json():
#     with open(json_file, 'r') as handle:
#         parsed = json.load(handle)
#     return parsed

# parsed = file_to_json()
# print(jsonPP(parsed))

# with open(json_file) as f:
#     content = f.readlines()
# content = [x.strip() for x in content]
# print(content)
# parsed = json.loads(content)
# print(json.dumps(parsed, indent=4, sort_keys=True))

test()

endpoint = "PDCS-DRM1P"
cluster = "pdcs-shobim-eks-121119"
group = "UNIX-L3SystemAdmins-U"
role = "member"
scid = "SC12345"
ccid = "Yes"
description = "PDCS-01"
provider = "eks"
aws_region = "us-east-1"
metric_type = "t2.small"
asg1 = "1"
asg2 = "3"
asgd = "1"

# script = subprocess.Popen(["clear"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# script = subprocess.Popen(["python", "/var/tmp/shobim/Scripts/Python/Rancher2/Rancher2Library/rancher2.py", "-u", endpoint, "-re", cluster, "-g", group, "-r", role, "-s", scid, "-ccid", ccid, "-d", description, "-p", provider, "-ar", aws_region, "-at", metric_type, "-asg1", asg1, "-asg2", asg2, "-asgd", asgd], stderr=subprocess.PIPE)
# this_out, this_err = script.communicate()