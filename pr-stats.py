#!/usr/bin/env python


# Create script to get PR(Pull Request) statistics from GitHub.
# Required options and usage see below.
# Usage:
# pr-stats [options] <user> [<repo>]
# pr-stats --version
# pr-stats (-h | --help)
# Options:
# Implement at least 5 options. Choose any or provide your own options.
# • Show help.
# • Print the program's installed version
# • Basic statistics about merged/closed rate.
# • Number of days opened.
# • Number of comments created.


import sys
import argparse
import requests
import json

version = "0.0.1"


def createParser():
    parser = argparse.ArgumentParser(
        prog="pr-stats",
        description="Usage: \
        pr-stats [options] <user> [<repo>] \
        pr-stats --version \
        pr-stats (-h | --help) \
\
        Options: \
        -h --help         Show this screen.\
        --version      Show the program's installed version.\
        --basic        Show basic statistics about merged/closed rate.\
        --days-open    Show number of days opened.\
        --comments     Show number of comments created.",
        epilog="(c) Andrei Sheihus 2019 ",
        add_help=False)

    parent_group = parser.add_argument_group(title='Parameters')
    parent_group.add_argument('--help', '-h', action='help', help='Help')

    parent_group.add_argument(
        '-v', '--version', action='version',
        help="Show the program's installed version.", version='%(prog)s {}'.format(version))

    parser.add_argument('user')
    parser.add_argument('repo', nargs='?')
    parser.add_argument("--basic", action='store_const', const=True, default=False)
    parser.add_argument("--days-open", action='store_const', const=True, default=False)
    parser.add_argument("--comments", action='store_const', const=True, default=False)

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    print(namespace)

    with open("mytoken.bin", "r") as token_file:
        username = token_file.read()
        token = token_file.read()

    gh_session = requests.Session()
    gh_session.auth = (username, token)

    user = namespace.user
    repo = namespace.repo

    gh_session = requests.Session()
    gh_session.auth = (username, token)

    if namespace.basic:
        print("Basic:")
        repo_url = 'https://api.github.com/repos/' + user + '/' + repo + '/pulls'
        pulls = json.loads(gh_session.get(repo_url).text)
        for pull in pulls:
            print(pull["state"], pull["html_url"])
    elif namespace.days_open:
        print("Days open:")
        repo_url = 'https://api.github.com/repos/' + user + '/' + repo + '/stats/commit_activity'
        activity = json.loads(gh_session.get(repo_url).text)
        print(activity)
    elif namespace.comments:
        print("Comments:")
        repo_url = 'https://api.github.com/repos/' + user + '/' + repo + '/pulls/comments'
        comments = json.loads(gh_session.get(repo_url).text)
        for com in comments:
            print(com["url"], com["id"])
    else:
        parser.print_help()
