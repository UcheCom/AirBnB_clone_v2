#!/usr/bin/python3
"""Fabric script to genereate tgz archive
   Usage: fab -f 1-pack_web_static.py do_pack
"""

from fabric.api import local
from datetime import date
from time import strftime


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
