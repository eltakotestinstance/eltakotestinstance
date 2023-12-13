import os
import requests
import json
import base64

# assuming ISSUE_KEY, JIRA_BASE_URL, JIRA_USER_EMAIL, JIRA_API_TOKEN, NEW_SUMMARY, and NEW_DESCRIPTION are passed as environment variables
issue_key = os.getenv('ISSUE_KEY')  # get the issue key
jira_base_url = os.getenv('JIRA_BASE_URL')  # get the Jira base URL
jira_email = os.getenv('JIRA_USER_EMAIL')  # get the Jira user email
jira_token = os.getenv('JIRA_API_TOKEN')  # get the Jira API token
new_summary = os.getenv('NEW_SUMMARY')  # get the new summary
new_description = os.getenv('NEW_DESCRIPTION')  # get the new description
epic_issue_key = os.getenv('EPIC_KEY')

data = None

if epic_issue_key is None:
    data = {
        "fields": {
            "summary": new_summary,
            "description": {
                "version": 1,
                "type": "doc",
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": f"{new_description}\n\n*Posted from Github*",
                            }
                        ],
                    }
                ],
            },
            "customfield_10045": 1,
        }
    }
else:
    data = {
        "fields": {
            "summary": new_summary,
            "description": {
                "version": 1,
                "type": "doc",
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": f"{new_description}\n\n*Posted from Github*",
                            }
                        ],
                    }
                ],
            },
            "customfield_10045": 1,
            "parent": {"key": f"{epic_issue_key}"}
        }
    }

# create the headers
headers = {
    "Authorization": f"Basic {base64.b64encode(f'{jira_email}:{jira_token}'.encode()).decode()}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# make the PUT request
response = requests.put(
    f"{jira_base_url}/rest/api/3/issue/{issue_key}",
    data=json.dumps(data),
    headers=headers
)

# check the response
if response.status_code != 204:
    print(f"Error: HTTP status code {response.status_code}")
    exit(1)
