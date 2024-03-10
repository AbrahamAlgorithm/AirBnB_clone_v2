#!/usr/bin/python3
"""Full deployment"""
from fabric.api import run, local, env, put
from datetime import datetime
import os

env.hosts = ['18.210.', '35.168.2.166']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    """function to deploy the code"""
    fil = os.path.basename(archive_path)
    folder = fil.replace(".tgz", "")
    path = "/data/web_static/releases/{}/".format(folder)
    yes = False
    if os.path.exists(archive_path):
        try:
            put(archive_path, '/tmp/')
            run("mkdir -p {}".format(path))
            run("tar -xzf /tmp/{} -C {}".format(fil, path))
            run("rm -rf /tmp/{}".format(fil))
            run("mv {}web_static/* {}".format(path, path))
            run("rm -rf {}web_static".format(path))
            run("rm -rf /data/web_static/current")
            run("ln -sf {} /data/web_static/current".format(path))
            print('Ran SUccesfully')
            yes = True
        except Exception as e:
            print(e)
            yes = False
    else:
        return (False)
    return (yes)


def deploy():
    """overall deployment"""
    result = do_pack()
    final = do_deploy(result) if result else False
    return(final)
