#!/usr/bin/python3
"""Defines fabric script based on the file 1-pack_web_static.py that
 distributes an archive to the web servers using the function do_deploy
"""

from fabric.api import put, run, local, env
from os import exists

env.hosts = ["3.80.19.118", "3.83.18.66"]


def do_deploy(archive_path):
    """Fabric script distributes an archive to your web servers
    """

    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        noext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, noext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, noext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, noext))
        run('rm -rf {}{}/web_static'.format(path, noext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, noext))
        return True
    except Exception:
        return False
