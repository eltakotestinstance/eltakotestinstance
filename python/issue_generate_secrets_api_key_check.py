from github import Github
import os

# First create a Github instance:

# using an access token
g = Github(os.getenv("GITHUB_TOKEN"))
USER_NAME = os.getenv('USER_NAME')

jira_server = os.getenv("JIRA_BASE_URL")
jira_user = os.getenv("JIRA_USER_EMAIL")
jira_token = os.getenv("JIRA_API_TOKEN")
issue_key = os.getenv("ISSUE_KEY")
comment_text = os.getenv("COMMENT_TEXT")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    if repo.name == "eltakotestinstance":
        secrets = repo.get_secrets()
        for secret in secrets:
            if secret.name == f"JIRA_API_TOKEN_{os.getenv('USER_NAME')}":
                jira_token = secret.value
                break
        

# Create a JIRA connection
jira = JIRA(server=jira_server, basic_auth=(jira_user, jira_token))

# Get the issue
issue = jira.issue(issue_key)

# Add a comment to the issue
jira.add_comment(issue, comment_text)
