from github import Github
import os

# assuming GITHUB_TOKEN, GITHUB_REPOSITORY, ISSUE_KEY, TEXT, and AUTHOR are passed as environment variables
g = Github(os.getenv('GITHUB_TOKEN'))  # replace with your GitHub token
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))  # get the repository
issue_key = os.getenv('ISSUE_KEY')  # get the issue key
text = os.getenv('TEXT')  # get the text
author = os.getenv('AUTHOR')  # get the author

comment_final = f"*Comment from {author}*\n\n{text}\n\n*Posted from Jira*"

issue_number = None
issues = repo.get_issues(state='all')

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
    issue.create_comment(body=comment_final)
else:
    print(f"No issue found with key: {issue_key}")
    exit(1)
