from config import git_url, git_nochange, git_local_path, target_program
from os import system
from time import sleep
import git
import subprocess

# https://www.devdungeon.com/content/working-git-repositories-python

target_program += ".service"
# git.remote.Remote(set)
repo = git.Repo(git_local_path)


def git_pull_changed():
    repo.remotes.origin.pull()
    # check if something    changed
    current = repo.head.commit

    repo.remotes.origin.pull()
    if current != repo.head.commit:
        print("Repo changed! Activated.")
        return True
    else:
        print("Repo not changed. Sleep mode activated.")
        return False


def target_restart():
    # restart target
    result = subprocess.run(['/usr/bin/systemctl daemon-reload'], stdout=subprocess.PIPE) # restart daemon
    # result.stdout
    # b'total 0\n-rw-r--r--  1 memyself  staff  0 Mar 14 11:04 files\n'

    # The return value is a bytes object, so if you want a proper string, you'll need to decode it. Assuming the called process returns a UTF-8-encoded string:

    print(result.stdout.decode('utf-8'))
    # 'total 0\n-rw-r--r--  1 memyself  staff  0 Mar 14 11:04 files\n'


while True:
    # changes = git_pull_changed()
    # if changes:
    target_restart()
    sleep(60)  # runs roughly every minute. depends on everything else, but close enough for jazz.


#
#
# cmd = ['echo', 'I like potatos']
# proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
# o, e = proc.communicate()
#
# print('Output: ' + o.decode('ascii'))
# print('Error: '  + e.decode('ascii'))
# print('code: ' + str(proc.returncode))