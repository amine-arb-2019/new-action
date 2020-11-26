#!/usr/bin/env python3

import os
import sys
import re
from github import Github
import requests as reqs 


def get_env_var(env_var_name, echo_value=False):
    value=os.environ.get(env_var_name)

    if value is None:
        raise ValueError(f'The environmental variable {env_var_name} is empty!')

    if echo_value:
        print(f"{env_var_name} = {value}")
    return value

def main():
    # Check if the number of input arguments is correct
    if len(sys.argv) != 3:
        raise ValueError('Invalid number of arguments!')

    # Get the GitHub token
    token=sys.argv[1]

    # Get the PR number
    pr_number_str=sys.argv[2]

    repo_name=get_env_var('GITHUB_REPOSITORY')
    github_ref=get_env_var('GITHUB_REF')
    github_event_name=get_env_var('GITHUB_EVENT_NAME')

    repo = Github(token).get_repo(repo_name)


    if github_event_name == 'issue_comment':
        print(f' Event = "{github_event_name}"')

        exit(0)
    else:
        exit(1)

if __name__ == '__main__':
    main()


