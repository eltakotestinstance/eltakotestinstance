from github import Github
from datetime import datetime
import os

# assuming issue_key and author are passed as environment variables
issue_key = os.getenv('INPUT_ISSUE_KEY')
author = os.getenv('INPUT_AUTHOR')
text = os.getenv('TEXT')
timestamp = datetime.now().isoformat()

g = Github(os.getenv('GITHUB_TOKEN'))  # replace with your GitHub token
repo = g.get_repo(f"{os.getenv('GITHUB_REPOSITORY')}")  # get the repository

milestones = repo.get_milestones(state='open')

for milestone in milestones:
    if issue_key in milestone.description:
        new_description = f"{milestone.description}\n---\n### {author}: \n{text}\n({timestamp})"
        milestone.edit(description=new_description,
                       title=milestone.title)
        break


