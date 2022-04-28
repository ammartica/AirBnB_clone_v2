#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ Compress to .tgz files"""
    try:
        local("mkdir -p versions")
        now = datetime.now()
        date = now.strftime("%Y%m%d%H%M%S")
        file_name = "web_static_{}.tgz".format(date)
        local("tar -cvzf versions/{} web_static".format(file_name))
        return file_name
    except:
        return None
