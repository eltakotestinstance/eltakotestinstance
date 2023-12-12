from github import Github
import os

# assuming GITHUB_TOKEN, GITHUB_REPOSITORY, and MILESTONE_NUMBER are passed as environment variables
g = Github(os.getenv('GITHUB_TOKEN'))  # replace with your GitHub token
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))  # get the repository
milestone_number = int(os.getenv('MILESTONE_NUMBER'))  # get the milestone number

milestone = repo.get_milestone(milestone_number)

current_description = milestone.description
if '[skip]' in current_description:
    milestone.edit(description=current_description.split('[skip]')[0],
                   title=milestone.title)
    print("false")
else:
    print("true")
