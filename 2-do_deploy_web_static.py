#!/usr/bin/python3
"""
    A fabric script that distributes the archive we created to remote servers
"""
from fabric.operations import local, run, 

def do_deploy(archive_path):
    """
        To deploy to web servers
    """
    if != archive_path:
        return False


