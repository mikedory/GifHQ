# import the fabric requirements
from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

# import local_settings.py
from gifhq.local_settings import *

"""
Test and prepare everything locally

This leaves a placeholder for minification as well
"""


# run Django's test framework
def test():
    with settings(warn_only=True):
        result = local('./manage.py test gifserver', capture=True)
    if result.failed and not confirm("Tests failed! D: Continue anyway?"):
        abort("Aborting!")


# add and commit all local files
def commit():
    with settings(warn_only=True):
        commit = local("git add -p && git commit")
    if commit.failed and not confirm("Add and commit failed. Proceed?"):
        abort("Aborting!")


# push up to github
def push():
    local("git push origin master")


def minify():
    # this is where one would pack/minify stuff
    pass


# run all the pre-flight tests
def prepare_deploy():
    minify()
    test()
    commit()
    push()


"""
Deploy to the remote server!

For tags:
    fab deploy:tag=YYYY-MM-DD-tag-description

For branches:
    fab deploy:branch=master
"""


def deploy(tag=None, branch=None):

    # when deploying by tag
    if tag is not None:
        # define where this is all going
        code_deploy_dir = code_dir_root + "/" + tag

        print "\n*** deploying %s to %s ***\n" % (tag, code_deploy_dir)

        # make the directory, deploy the code, and symlink it
        run('mkdir -p %s' % code_deploy_dir)
        with cd(code_dir_root):
            run("git clone %s %s" % (code_repo, code_deploy_dir))
        with cd(code_deploy_dir):
            run("git checkout %s" % tag)
        with cd(code_dir_root):
            run("ln -nfs %s %s" % (code_deploy_dir, code_dir_target))

    # when deploying by branch
    elif branch is not None:
        # define where this is all going
        code_deploy_dir = code_dir_target

        # test to make sure the repo exists
        with settings(warn_only=True):
            if run("test -d %s" % code_dir_target).failed:
                run("git clone %s %s" % (code_repo, code_dir_target))
        # fetch, checkout, and merge the target branch
        with cd(code_dir_target):
            run("git fetch")
            run("git checkout %s" % branch)
            run("git merge origin/%s" % branch)

    # gotta have one or the other!
    else:
        abort("like, seriously. you need a tag or a branch, brah.")

    # restart processes and clean up
    with cd(code_deploy_dir):
        print "\n*** code deployed, restarting server ***\n"
        run("supervisorctl restart gif")
        print "\n*** done! ***\n"
