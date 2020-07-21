# pullcheck
Pull a repo, check for any changes, restart a program. Arguably a bit of a bodge for environments where changes cannot be pushed, such as behind a VPN. Does not check that your changes are good, just whether they have happened.

Change variables in config.py for your setup. Configure git to use SSH that does not need a passcode. Set up the remote origin on your local git directory before you run.

Designed for Ubuntu Linux. `pullcheck` should be set to autorun on boot, not your target program.  

## Basic Structure
1. run `git pull` on `git_url`
1. if `git_pull_change` is `True` then stop target program
1. Start target program
1. loop every `pull_wait` seconds until the end of the universe or the server dies, whichever comes first