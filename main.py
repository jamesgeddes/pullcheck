from config import git_local_path, target_program
from time import sleep
import subprocess as sp
import git

target_program += ".py"
git_local_path += "/"


def git_pull_change(path):
    repo = git.Repo(path)
    current = repo.head.commit

    repo.remotes.origin.pull()

    if current == repo.head.commit:
        print("Repo not changed. Sleep mode activated.")
        return False
    else:
        print("Repo changed! Activated.")
        return True


def target_start(target):
    #  Thanks! https://stackoverflow.com/questions/5611576/how-do-i-spawn-a-separate-python-process
    return sp.Popen(["python3", git_local_path + target]).returncode  # assumes target in root of git directory


def target_stop(target):
    return sp.run(["pkill", "-f", target]).returncode


def target_restart(target):
    target_stop(target)
    target_start(target)


target_start(target_program)
while True:
    if git_pull_change(git_local_path):
        target_restart(target_program)
    else:
        pass
    sleep(60)

