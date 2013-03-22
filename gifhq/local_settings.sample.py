# deploy/fabric needs
from fabric.api import *

# remote server configs
env.user = 'username'
env.hosts = ['domain.com']
env.key_filename = '/path/to/.ssh/id_rsa'

# deploy directory and repo info
code_dir = '/path/to/code/directory'
code_repo = 'git@gitrepo.com:user/GifHQ.git'
