import os

USER_NAME = int(os.getenv('USER_NAME'))

action_content = f"""
        if [[ -z "${{{{ secrets.JIRA_API_TOKEN_{user_name}" }}}} ]]; then
          echo "JIRA secret for {user_name} is not set"
          OUTPUT="{{{{secrets.JIRA_API_TOKEN}}}}"
        else
          echo "JIRA secret for {user_name} is set"
          OUTPUT="{{{{secrets.JIRA_API_TOKEN_{user_name}}}}}"
        fi
"""

print(action_content)