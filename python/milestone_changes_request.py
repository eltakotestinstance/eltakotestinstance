import os
import requests
import json

# assuming NEW_DESCRIPTION, JIRA_USER_EMAIL, JIRA_API_TOKEN, ISSUE, and DUE_DATE are passed as environment variables
new_description = os.getenv('NEW_DESCRIPTION')  # get the new description
jira_user_email = os.getenv('JIRA_USER_EMAIL')  # get the Jira user email
jira_api_token = os.getenv('JIRA_API_TOKEN')  # get the Jira API token
jira_instance_url = os.getenv('JIRA_BASE_URL')
issue = os.getenv('ISSUE')  # get the issue
due_date = os.getenv('DUE_DATE')  # get the due date

new_description = new_description.split('AUTOMATICALLY GENERATED CONTENT DO NOT EDIT/DELETE BEYOND THIS POINT')[0]

# create the JSON data
data = {
    "fields": {
        "description": new_description,
        "duedate": due_date,
        "customfield_10041" : 1
    }
}

# make the PUT request
response = requests.put(
    f"{jira_instance_url}rest/api/2/issue/{issue}",
    data=json.dumps(data),
    headers={"Content-Type": "application/json"},
    auth=(jira_user_email, jira_api_token)
)

# check the response
if response.status_code != 204:
    print(f"Error: HTTP status code {response.status_code}")
    exit(1)
