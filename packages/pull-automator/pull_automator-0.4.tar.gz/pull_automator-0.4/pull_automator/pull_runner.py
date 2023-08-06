import os
import sys
import subprocess
import git
from colorama import Fore, Style


"""
Python script for pulling remote updates to specified
branches of all git repos in a provided directory.
"""


def git_pull_runner(path, branch):
    """
    Loop through repos in directory. This function serves as a sort of manager for all functions of this script.
    :param path: the path of the directory
    :param branch: name of the branch we wish to pull from remote
    """
    for dir_name in os.listdir(path):
        os.chdir(path + dir_name)
        repo = git.Repo(os.getcwd())
        current_branch_name = repo.active_branch.name

        print("")
        print("project:         " + Fore.YELLOW + dir_name + Style.RESET_ALL, flush=True)
        print("current branch:  " + Fore.YELLOW + current_branch_name + Style.RESET_ALL, flush=True)
        print("   ------------", flush=True)

        # Determine what to do depending on current branch.
        if current_branch_name == branch:
            pull(repo)
        else:
            checkout_pull_checkout(repo, current_branch_name, branch)


def checkout_pull_checkout(repo, current_branch_name, main_branch):
    """
    Handles pulling when not on the specified branch. Stashes if necessary.
    :param repo:
    :param current_branch_name:
    :param main_branch:
    """
    current_branch_status = repo.git.status()
    if 'Changes not staged for commit:' in current_branch_status:
        # Stashes branch, checks out correct branch, pulls, checks back out branch, pops stash.
        with open(os.devnull, 'w') as devnull:
            print("   stashing. checking out " + Fore.LIGHTCYAN_EX + main_branch + Style.RESET_ALL, flush=True)

            repo.git.stash()
            repo.git.checkout(main_branch)
            pull(repo)

            print("   checking back out " + Fore.LIGHTCYAN_EX + current_branch_name + Style.RESET_ALL + " and popping stash", flush=True)

            repo.git.checkout(current_branch_name)
            subprocess.call("git stash pop", stdout=subprocess.DEVNULL)

    else:
        # Checks out correct branch, pulls, checks back out branch.
        with open(os.devnull, 'w') as devnull:
            print("   no stash needed. checking out " + Fore.LIGHTCYAN_EX + main_branch + Style.RESET_ALL, flush=True)

            repo.git.checkout(main_branch)
            pull(repo)

            print("   checking back out " + Fore.LIGHTCYAN_EX + current_branch_name + Style.RESET_ALL, flush=True)

            repo.git.checkout(current_branch_name)


def pull(repo):
    """
    Pulls updates for for a specified repo.
    :param repo: the set git repository for the current os directory.
    """
    try:
        with open(os.devnull, 'w') as devnull:
            pull_response = repo.git.pull()
            if 'Already up to date' in pull_response:
                print("   already up to date", flush=True)
            else:
                print("   pulled updates from remote", flush=True)
    except:
        print(Fore.RED + "   pulling failed. make sure upstream exists and is set" + Style.RESET_ALL, flush=True)
        print("   skipped pull", flush=True)


def parse_args(args):
    """
    Parse arguments to verify correct usage.
    :param args: command line arguments.
    :return: a list containing the values for path and branch.
    """
    parsed_args = []
    path = None
    branch = None

    # If arguments are incorrect
    if '-p' not in args or '-b' not in args or '-usage' in args:
        print_usage_notes()
        sys.exit()
    # If arguments are correct
    else:
        try:
            for index, arg in enumerate(args):
                if arg == '-p':
                    path = args[index+1]
                elif arg == '-b':
                    branch = args[index+1]
        except:
            print(Fore.RED + "invalid arguments. please include -p {path-to-dir} and -b {branch-to-pull}" + Style.RESET_ALL, flush=True)
            sys.exit("run script with -usage argument to view usage notes")

        parsed_args.append(path)
        parsed_args.append(branch)
    return parsed_args


def check_path_string(path_string):
    """
    Ensures path exists. Appends '/' if the path string doesn't end with it already.
    :param path_string: the path argument provided to us.
    """
    if os.path.exists(path_string):
        if not path_string.endswith('/'):
            path_string += '/'
        return path_string
    else:
        print("Invalid path argument. No such path exists: " + path_string, flush=True)
        sys.exit()


def print_usage_notes():
    """
    Displays usage information.
    """
    print("\033[H\033[J")
    print(Fore.YELLOW + "             * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *" + Style.RESET_ALL)
    print(Fore.YELLOW + "             *" + Style.RESET_ALL + " iterates through a directory and updates the specified        " + Fore.YELLOW + "*" + Style.RESET_ALL)
    print(Fore.YELLOW + "             *" + Style.RESET_ALL + " branch of each local git repository with its remote upstream. " + Fore.YELLOW + "*" + Style.RESET_ALL)
    print(Fore.YELLOW + "             * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *" + Style.RESET_ALL)
    print("")
    print("             usage notes:")
    print("")
    print("             arguments")
    print("             ------------")
    print(Fore.YELLOW + "        -p   " + Style.RESET_ALL + "path to directory containing projects")
    print(Fore.YELLOW + "        -b   " + Style.RESET_ALL + "branch name to update. will stash and checkout to branch if not currently on it.")
    print(Fore.YELLOW + "    -usage   " + Style.RESET_ALL + "usage notes are opened anytime this argument is included.")
    print(Fore.YELLOW + "   example   " + Style.RESET_ALL + "python {this-script.py} -p {path-to-dir} -b {name-of-branch}")
    print("")
    print(Fore.YELLOW + "           *" + Style.RESET_ALL + " requires python 3.7 or greater")
    print(Fore.YELLOW + "           *" + Style.RESET_ALL + " supplied path directory must only contain git repositories.")
    print(Fore.YELLOW + "           *" + Style.RESET_ALL + " all projects in the supplied path directory must be git repositories and contain the supplied branch name.")
    print(Fore.YELLOW + "           *" + Style.RESET_ALL + " all branches must have remote upstream set properly.")
    print(Fore.YELLOW + "           *" + Style.RESET_ALL + " arguments can be provided in any order.")
    print("")


if __name__ == "__main__":
    print("\033[H\033[J")

    # getting args
    args = parse_args(sys.argv)
    path = check_path_string(args[0])
    branch = args[1]

    # function that initiates pulling
    git_pull_runner(path, branch)

    print("")
    print("")
    print("OK")
    sys.stdout.flush()
