import os

USER_NAME = os.getenv('USER_NAME')

action_content = f"${{{{ secrets.JIRA_API_TOKEN_{USER_NAME} }}}}"

print(action_content)