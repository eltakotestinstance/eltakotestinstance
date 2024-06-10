from github import Github
import os

# assuming GITHUB_TOKEN, GITHUB_REPOSITORY, ISSUE_KEY, and TEXT are passed as environment variables
g = Github(os.getenv('GITHUB_TOKEN'))  # replace with your GitHub token
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))  # get the repository
issue_key = os.getenv('INPUT_ISSUE_KEY')  # get the issue key
text = os.getenv('INPUT_TEXT')  # get the text

milestones = repo.get_milestones(state='open')

for milestone in milestones:
    if issue_key in milestone.description:
        current_generated_split = milestone.description.split('AUTOMATICALLY GENERATED CONTENT DO NOT EDIT/DELETE '
                                                              'BEYOND THIS POINT')[1]
        new_description = f"{text}\nAUTOMATICALLY GENERATED CONTENT DO NOT EDIT/DELETE BEYOND THIS POINT\n{current_generated_split}"
        milestone.edit(title=milestone.title, description=new_description)
        break
