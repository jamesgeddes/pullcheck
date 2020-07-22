from config import git_local_path, target_program, pull_wait
from time import sleep
import subprocess as sp
import git

git_local_path += "/"
target_program += ".py"


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
    stopped = target_stop(target)
    # stop_count = 0
    while stopped != 0:  # naive assumption that the program will close gracefully without returning errors
        print("Can't stop")
        stopped = target_stop(target)
        # stop_count += 1
        # if stop_count > 100:  # a branchless no no, but then again this is not assembly so meh.
        #     pass  # you might like to add an action here

    started = target_start(target)
    # start_count = 0
    while started is not None:
        print("Can't start")
        started = target_start(target)
        # start_count += 1
        # if start_count > 100:
        #     pass  # you might like to add an action here

target_start(target_program)
while True:
    if git_pull_change(git_local_path):
        target_restart(target_program)
    else:
        pass
    sleep(pull_wait)

