from github import Github
import os

# assuming GITHUB_TOKEN, GITHUB_REPOSITORY, TITLE, and BODY are passed as environment variables
g = Github(os.getenv('GITHUB_TOKEN'))  # replace with your GitHub token
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))  # get the repository
title = os.getenv('TITLE')  # get the title
body = os.getenv('BODY')  # get the body

if not body or body == '':
    body = "*Posted from Jira*"
else:
    body = f"{body}\n*Posted from Jira*"

issue = repo.create_issue(title=title, body=body)

if issue:
    print(issue.number)
else:
    print("")
    raise Exception('Error: Issue not created')
