from github import Github
import os

# First create a Github instance:

# using an access token
g = Github(os.getenv("GITHUB_TOKEN"))
USER_NAME = os.getenv('USER_NAME')


# Then play with your Github objects:
for repo in g.get_user().get_repos():
    if repo.name == "eltakotestinstance":
        secrets = repo.get_secrets()
        for secret in secrets:
            if secret.name == f"JIRA_API_TOKEN_{os.getenv('USER_NAME')}":
                print("Secret exists")
                break
        else:
            print("Secret does not exist")
