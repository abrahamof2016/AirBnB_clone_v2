#!/usr/bin/python3
# A fabric script to distribute an archive to web servers.

from fabric.api import *
from fabric.contrib import files
import os

env.hosts = ['100.26.214.241', '54.237.43.234']


def do_deploy(archive_path):
    """
    distribute a .tgz archive of the web_static directory to a web server.
    """
    if not os.path.exists(archive_path):
        return False

    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = data_path + name

    try:
        put(archive_path, '/tmp')
        local('mkdir -p {}'.format(dest))
        local('tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        local('rm -f /tmp/{}.tgz'.format(name))
        local('mv {}/web_static/* {}/'.format(dest, dest))
        local('rm -rf {}/web_static'.format(dest))
        local('rm -rf /data/web_static/current')
        local('ln -s {} /data/web_static/current'.format(dest))
        return True
    except:
        return False
