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
        run('mkdir -p {}'.format(dest))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        run('rm -f /tmp/{}.tgz'.format(name))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dest))
        return True
    except:
        return False
