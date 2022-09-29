#!/usr/bin/python3
# A fabric script that generates wer_static.tgz archive using the do_pack fun

from fabric.operations import local
from datetime import datetime


def do_pack():
    """
        To mkae compressed file in the /versions/web_static dir
        from the web_static dir
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p versions')

    archive_path = 'versions/web_static_{}'.format(time)

    file = local('sudo tar -czvf {}.tgz web_static'.format(
        archive_path), capture=True)

    if file:
        return file
    else:
        return None
