import os

USER_NAME = os.getenv('USER_NAME')

action_content = f"""
        if [[ -z "${{{{ secrets.JIRA_API_TOKEN_{USER_NAME} }}}}"  ]]; then
          echo "JIRA secret for {USER_NAME} is not set"
          OUTPUT="{{{{secrets.JIRA_API_TOKEN}}}}"
        else
          echo "JIRA secret for {USER_NAME} is set"
          OUTPUT="{{{{secrets.JIRA_API_TOKEN_{USER_NAME}}}}}"
        fi
"""

print(action_content)