from github import Github
import os

# assuming GITHUB_TOKEN, GITHUB_REPOSITORY, MILESTONE_NUMBER, SENDER, and CHANGES are passed as environment variables
g = Github(os.getenv('GITHUB_TOKEN'))  # replace with your GitHub token
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))  # get the repository
milestone_number = int(os.getenv('MILESTONE_NUMBER'))  # get the milestone number and convert to int
sender = os.getenv('SENDER')  # get the sender
previous_description = os.getenv('CHANGES')  # get the changes

milestone = repo.get_milestone(milestone_number)

current_description = milestone.description

if sender == 'github-actions':  # Ignore edits made by a workflow
    print('false')
elif '[skip]' in current_description:  # Ignore edits made from Jira and delete the [skip] tag
    milestone.edit(title=milestone.title, description=current_description.split('[skip]')[0])
    print('false')
else:
    # Split the descriptions at the dividing string
    current_description_split = current_description.split('AUTOMATICALLY GENERATED CONTENT DO NOT EDIT/DELETE BEYOND THIS POINT')[0]
    previous_description_split = previous_description.split('AUTOMATICALLY GENERATED CONTENT DO NOT EDIT/DELETE BEYOND THIS POINT')[0]
    # Compare the descriptions
    if current_description_split.strip() != previous_description_split.strip():  # compares the descriptions before the phrase: "AUTOMATICALLY GENERATED CONTENT DO NOT EDIT/DELETE BEYOND THIS POINT"
        print(current_description_split)
    else:
        print('false')
