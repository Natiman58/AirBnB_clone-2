#!/usr/bin/python3
"""
    A fabric script that distributes the archive we created to remote servers
"""

from fabric.api import local, run, put, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['44.192.48.9', '3.236.13.94']


def do_pack():
    """
        To make compressed file in the /versions/web_static dir
        from the web_static dir
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p versions')

    archive_path = 'versions/web_static_{}'.format(time)

    file = local('sudo tar -czvf {}.tgz web_static'.format(
        archive_path))

    if file:
        return file
    else:
        return None


def do_deploy(archive_path):
    """
        Distributes an archive to our web servers
    """
    try:
        file_av = archive_path.split('/')[-1]
        current = '/data/web_static/current'
        path = '/data/web_static/releases/' + file_av.strip('.tgz')

        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(file_av, path))
        run('rm /tmp/{}'.format(file_av))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(path, current))
        print("New version deployed!")
        return True
    except Exception:
        return False
