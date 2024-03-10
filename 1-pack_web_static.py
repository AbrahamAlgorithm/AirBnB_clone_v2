#!/usr/bin/python3
"""using Fabric to generate archive"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """The function to configure the archive"""
    if not (os.path.isdir("versions")):
        local("mkdir versions")
    pat = "versions/web_static_{}.tgz".format(
           datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    result = local("tar -czvf {} web_static".format(pat))
    if (result.failed):
        return (None)
    else:
        return (pat)
