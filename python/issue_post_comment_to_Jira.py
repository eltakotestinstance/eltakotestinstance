import os
import requests
import json
import base64

# assuming ISSUE_KEY, USER_NAME, COMMENT_TEXT, JIRA_BASE_URL, JIRA_USER_EMAIL, and JIRA_API_TOKEN are passed as environment variables
issue_key = os.getenv('ISSUE_KEY')  # get the issue key
user_name = os.getenv('USER_NAME')  # get the user name
comment_text = os.getenv('COMMENT_TEXT')  # get the comment text
jira_url = os.getenv('JIRA_BASE_URL')  # get the Jira base URL
jira_email = os.getenv('JIRA_USER_EMAIL')  # get the Jira user email
jira_token = os.getenv('JIRA_API_TOKEN')  # get the Jira API token

comment = f"{user_name} posted :\n{comment_text}\n*Posted from GitHub*"

# create the JSON data
data = {
    "body": {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {
                        "text": comment,
                        "type": "text"
                    }
                ]
            }
        ]
    }
}

# create the headers
headers = {
    "Authorization": f"Basic {base64.b64encode(f'{jira_email}:{jira_token}'.encode()).decode()}",
    "Content-Type": "application/json",
}

# make the POST request
response = requests.post(
    f"{jira_url}/rest/api/3/issue/{issue_key}/comment",
    data=json.dumps(data),
    headers=headers
)

# check the response
if response.status_code != 201:
    print(f"Error: Failed to post comment to Jira: {response.text}")
    exit(1)
    