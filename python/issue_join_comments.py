from github import Github
import os

# assuming GITHUB_TOKEN, GITHUB_REPOSITORY, and ISSUE_NUMBER are passed as environment variables
g = Github(os.getenv('GITHUB_TOKEN'))  # replace with your GitHub token
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))  # get the repository
issue_number = int(os.getenv('ISSUE_NUMBER'))  # get the issue number and convert to int

issue = repo.get_issue(number=issue_number)

comments = issue.get_comments()
result = '\n'.join(comment.body for comment in comments)

print(result)
