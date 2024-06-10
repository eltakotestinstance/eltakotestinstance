from github import Github
import os
import time

# assuming GITHUB_TOKEN, GITHUB_REPOSITORY, ISSUE_KEY, and EPIC_KEY are passed as environment variables
g = Github(os.getenv('GITHUB_TOKEN'))  # replace with your GitHub token
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))  # get the repository
issue_key = os.getenv('ISSUE_KEY')  # get the issue key
epic_key = os.getenv('EPIC_KEY')  # get the epic key

milestone_number = None
milestones = repo.get_milestones(state='open')

for milestone in milestones:
    if epic_key in milestone.description:
        milestone_number = milestone.number
        print(f'Found Epic issue Key {epic_key}')
        break

issue_number = None
max_tries = 10
tries = 0

while issue_number is None and tries < max_tries:
    issues = repo.get_issues(state='all')
    for issue in issues:
        comments = issue.get_comments()
        for comment in comments:
            if issue_key in comment.body:
                issue_number = issue.number
                break
        if issue_number is not None:
            break
    if issue_number is None:
        print(f'Issue not found, try again in 500ms(try: {tries})')
        tries += 1
        time.sleep(0.5)

if issue_number is not None and milestone_number is not None:
    issue = repo.get_issue(number=issue_number)
    issue.edit(milestone=repo.get_milestone(number=milestone_number))
else:
    print('Issue or Milestone not found')
    exit(1)
    