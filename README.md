# pullcheck
Pull a repo, check for any changes, restart a program. Bit of a bodge for environments where changes cannot be pushed, such as behind a VPN. Does not check that your changes are good, just whether they have happened.

Change variables in config.py for your setup. Configure git to use SSH that does not need a passcode.

Designed for Ubuntu Linux. Your target program should be a service. See [Setup Autorun a Python Script Using Systemd in Ubuntu 18.04](https://websofttechs.com/tutorials/how-to-setup-python-script-autorun-in-ubuntu-18-04/).

This script should be set to autorun on boot, not your target program.  

##Basic Structure
1. run `git pull` on `git_url`
1. if `pull` output is not `git_nochange` then stop target program
1. reload daemon
1. if target program stopped then start target program
1. loop every minute