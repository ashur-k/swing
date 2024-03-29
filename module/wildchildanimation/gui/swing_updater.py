# -*- coding: utf-8 -*-
_VERSION = "1.04"

#
# Disable InsecureRequestWarning for now
#
# https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#import urllib3
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import argparse
import platform

import sys
sys.path.append("./module")

import os
from pprint import pprint

import zipfile

# python 3
if sys.version_info.major >= 3:
    import urllib.request as request    
else:
    import urllib as request

SWING_DOWNLOAD = "https://github.com/wildchild-animation/swing/archive/refs/heads/main.zip"

# local import wildchildanimation module by adding to the path
if "Darwin" in platform.system():
    from pathlib import Path
    WCA_ROOT = "{}/WCA".format(Path.home())
else:
    WCA_ROOT = "C:/WCA"

def split_path(path):
     return os.path.splitdrive(path)

def get_python_version(path = ''):
    if "Darwin" in platform.system():
        cmd = '{}python3 --version'.format(path)
    else:
        cmd = '{}python --version'.format(path)
    try:
        p = os.popen(cmd)
        s = p.read()
        p.close()    
        return s
    except:
        return None     

def check_or_create_dir(dir):
    if not os.path.exists(dir):
        print("Creating new directory: {}".format(dir))  
        os.makedirs(dir)
    else:
        print("Found directory {}".format(dir))

def create_venv(dir):
    print("Creating python virtual env")
    drive, tail = split_path(dir)        
    
    if "Darwin" in platform.system():
        cmd = 'cd {} && python3 -m venv env'.format(dir)
    else:
        cmd = '{} && cd {} && python -m venv env'.format(drive, dir)

    p = os.popen(cmd)
    s = p.read()
    p.close()    

    pprint(s)

def update_requirements(dir):
    print("Updating requirements.txt")
    drive, tail = split_path(dir)        
    
    if "Darwin" in platform.system():
        cmd = 'cd {} && source env/bin/activate && pip install -r swing/swing-main/requirements.txt'.format(dir)
    else:
        cmd = '{} && cd {} && "env/Scripts/activate" && pip install -r swing/swing-main/requirements.txt'.format(drive, dir)
    
    p = os.popen(cmd)
    s = p.read()
    p.close()   

def get_swing_release():
    url = 'https://raw.githubusercontent.com/wildchild-animation/swing/main/module/swing.version'
    res = request.urlopen(url)
    dat = res.read()
    tex = dat.decode('utf-8')
    return tex

def run_swing_standalone(dir):
    drive, tail = split_path(dir)        

    if "Darwin" in platform.system():
        cmd = 'cd {}/swing/swing-main && source {}/env/bin/activate && python3 {}/swing/swing-main/module/wildchildanimation/plugin/swing_desktop.py'.format(dir, dir, dir)
    else:
        cmd = '{} &&  cd {}/swing/swing-main && "{}/env/Scripts/activate" && python {}/swing/swing-main/module/wildchildanimation/plugin/swing_desktop.py'.format(drive, dir, dir, dir)

    p = os.popen(cmd)
    s = p.read()
    p.close()   

def download_latest(dir):
    print("Downloading release")
    check_or_create_dir(dir)

    target = "{}/swing-main.zip".format(dir)
    request.urlretrieve(SWING_DOWNLOAD, target)

    return True

def extract_latest(download_dir, module_dir):
    print("Extracting release")
    check_or_create_dir(module_dir)
    with zipfile.ZipFile("{}/swing-main.zip".format(download_dir), 'r') as zf:
        zf.extractall(module_dir)
    
    return True
        
def setup_swing(working_dir, force_update = False):
    # make sure we have default directories
    check_or_create_dir(working_dir)

    venv_dir = "{}/env".format(working_dir)

    if not os.path.exists(venv_dir):
        create_venv(working_dir)
    else:
        print("Found virtual environment {}".format(venv_dir))

    install_dir = "{}/installs".format(working_dir)

    release_version = get_swing_release()
    release_dir = "{}/v{}".format(install_dir, release_version)

    if not os.path.exists(release_dir) or force_update:    
        download_latest(release_dir)

    version_path = "{}/swing/swing-main/module/swing.version".format(working_dir)
    module_path = "{}/swing".format(working_dir)

    if not os.path.exists(module_path) or force_update:
        check_or_create_dir(module_path)        
        extract_latest(release_dir, module_path)

    if not force_update:
        local_version = open(version_path, 'r').read()
        if not local_version == release_version:
            check_or_create_dir(module_path)        
            extract_latest(release_dir, module_path)

    update_requirements(working_dir)
    run_swing_standalone(working_dir)

def update(working_dir, force_update = False):
    print("Treehouse: Swing Updater v{}".format(_VERSION))
    if force_update:
        print("Forcing update")

    if working_dir is None:
        install_dir = WCA_ROOT
    else:
        install_dir = working_dir
    print("path: {}".format(install_dir))

    python_version = get_python_version()
    if not python_version:
        print("Please ensure python is in your path")
        exit(-2)
    else:
        print("Found {}".format(python_version))        

    if "Windows" in platform.platform() or "Darwin" in platform.system():
        setup_swing(install_dir, force_update)
    else:
        print("Not implemented yet")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", help = "Target dir", default = None, action='store')
    parser.add_argument("-f", "--force", help = "Force update", default = None, action='store_true')

    args = parser.parse_args()
    update(args.dir, args.force)
