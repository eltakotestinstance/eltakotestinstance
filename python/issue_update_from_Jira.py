from github import Github
import os

# assuming GITHUB_TOKEN, GITHUB_REPOSITORY, ISSUE_KEY, TITLE, and BODY are passed as environment variables
g = Github(os.getenv('GITHUB_TOKEN'))  # replace with your GitHub token
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))  # get the repository
issue_key = os.getenv('ISSUE_KEY')  # get the issue key
title = os.getenv('ISSUE_TITLE')  # get the title
body = os.getenv('ISSUE_BODY')  # get the body

issues = repo.get_issues(state='all')

issue_number = None

for issue in issues:
    comments = issue.get_comments()
    for comment in comments:
        if issue_key in comment.body:
            issue_number = issue.number
            break
    if issue_number is not None:
        break

if issue_number is not None:
    issue = repo.get_issue(number=issue_number)
    issue.edit(title=title, body=f"{body}")
else:
    raise Exception('Issue not found')
