# import the fabric requirements
from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

# import local_settings.py
from gifhq import local_settings

# get the local_settings.py variables
env.user = local_settings.env.user
env.hosts = local_settings.env.hosts
env.key_filename = local_settings.env.key_filename

print local_settings

code_dir = local_settings.code_dir
code_repo = local_settings.code_repo


def test():
    with settings(warn_only=True):
        result = local('./manage.py test gifserver', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")


def commit():
    local("git add -p && git commit")


def push():
    local("git push")


def prepare_deploy():
    test()
    commit()
    push()


# ---------------------

def deploy():
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone %s %s" % (code_repo, code_dir))
    with cd(code_dir):
        run("git fetch")
        run("git merge origin/master")
        run("supervisorctl restart gif")
