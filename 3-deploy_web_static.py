#!/usr/bin/python3
"""Fabric script to genereate tgz archive
   Usage: fab -f 1-pack_web_static.py do_pack
"""

from fabric.api import local, run, env, put
from datetime import date
from os.path import exists
from time import strftime

env.hosts = ["3.80.19.118", "3.83.18.66"]


def do_pack():
    """Generates a .tgz archive from the content of
    web_satic folder"""

    file_nam = strftime("%Y%m%d%H%M%S")
    archive = 'web_static_{}.tgz'.format(file_nam)
    local('mkdir -p versions')
    path = local('tar -cvzf versions/{} web_static'.format(archive))
    if path is not None:
        return archive
    else:
        return None


def do_deploy(archive_path):
    """Fabric script distributes an archive to your web servers
    """

    if exists(archive_path) is False:
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
    except Exception as e:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
