#!/usr/bin/python3
"""
Deletes out-of-date archives
fab -f 100-clean_web_static.py do_clean:number=2
    -i my ssh-key -u ubuntu > /dev/null 2>&1
"""

from fabric.api import *

env.user = "ubuntu"
env.hosts = ['3.80.19.118', '3.83.18.66']


def do_clean(number=0):
    """This delete out-of-date archives."""

    number = int(number)
    number = 2 if number == 0 else (number + 1)

    local("cd versions ; ls -t | tail -n +{} | xargs rm -rf".format(number))
    folder = "/data/web_static/releases"
    run("cd {} ; ls -t | tail -n +{} | xargs rm -rf".format(folder, number))
