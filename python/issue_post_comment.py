from github import Github
import os

# assuming GITHUB_TOKEN, GITHUB_REPOSITORY, ISSUE_NUMBER, and JIRA_ISSUE are passed as environment variables
g = Github(os.getenv('GITHUB_TOKEN'))  # replace with your GitHub token
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))  # get the repository
issue_number = int(os.getenv('ISSUE_NUMBER'))  # get the issue number and convert to int
jira_issue = os.getenv('JIRA_ISSUE')  # get the Jira issue

issue = repo.get_issue(number=issue_number)

comment_body = f"[Issue *{jira_issue}* in Jira](https://eltakotestinstance.atlassian.net/browse/{jira_issue})"
issue.create_comment(body=comment_body)
