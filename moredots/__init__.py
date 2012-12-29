"""
moredots -- root file
:author: Karol Kuczmarski "Xion"
"""
from moredots.cmdline import create_argument_parser
from moredots.repo import DotfileRepo


def main():
    """Entry point."""
    parser = create_argument_parser()
    args = vars(parser.parse_args())

    # dispatch execution depending on what command was issued
    command = args.pop('command', None)
    if command:
        command_handler = globals()['handle_%s' % command]
        return command_handler(**args)


# Handlers for different commands

def handle_init(repo_dir, home_dir):
    """Initialize dotfiles repository."""
    DotfileRepo.init(repo_dir, home_dir)


def handle_add(repo, filepath, hardlink):
    """Adds a dotfile to dotfiles repository."""
    repo.add(filepath, hardlink)


def handle_rm(repo, filepath):
    """Remove dotfile from dotfiles repository and return it
    to home directory intact.
    """
    repo.remove(filepath)


def handle_sync(repo, remote_url):
    """Synchronize dotfile repository with a remote one."""
    repo.sync(remote_url)


def handle_install(remote_url, repo_dir, home_dir):
    """Installs remote dotfiles repository on this machine."""
    DotfileRepo.install(remote_url, repo_dir, home_dir)
