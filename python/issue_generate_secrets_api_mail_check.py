import os

USER_NAME = os.getenv('USER_NAME')

action_content = f"""
        if [[ -z "${{{{ secrets.JIRA_USER_EMAIL_{user_name}" }}}} ]]; then
          echo "JIRA secret for {user_name} is not set"
          OUTPUT="{{{{secrets.JIRA_USER_EMAIL}}}}"
        else
          echo "JIRA secret for {user_name} is set"
          OUTPUT="{{{{secrets.JIRA_USER_EMAIL_{user_name}}}}}"
        fi
"""

print(action_content)