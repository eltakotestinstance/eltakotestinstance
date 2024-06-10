from github import Github
import os

# assuming GITHUB_TOKEN, GITHUB_REPOSITORY, MILESTONE_NUMBER, and JIRA_ISSUE are passed as environment variables
g = Github(os.getenv('GITHUB_TOKEN'))  # replace with your GitHub token
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))  # get the repository
milestone_number = int(os.getenv('MILESTONE_NUMBER'))  # get the milestone number and convert to int
jira_issue = os.getenv('JIRA_ISSUE')  # get the Jira issue

milestone = repo.get_milestone(milestone_number)

new_description = (f"{milestone.description}\n---\nAUTOMATICALLY GENERATED CONTENT DO NOT EDIT/DELETE BEYOND THIS "
                   f"POINT\n[Issue in Jira](https://eltakotestinstance.atlassian.net/browse/{jira_issue})")
milestone.edit(title=milestone.title,
               description=new_description)
