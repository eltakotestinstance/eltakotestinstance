from git import Repo
from git import Git
import os

# assuming PERSONAL_TOKEN is passed as an environment variable
token = os.getenv('PERSONAL_TOKEN')  # get the token
before_hash = os.getenv('BEFORE_HASH')  # get the hash of the commit to revert to 
branch = os.getenv('GITHUB_REF').split('/')[-1]  # get the branch that triggered the workflow
repo_dir = '../'  # directory of your repository

g = Git(repo_dir)

# configure the url
g.config('--global', 'url."https://x-access-token:' + token + '@github.com/".insteadOf', 'https://github.com/')

repo = Repo(repo_dir)

# get the current branch


# revert the last commit
repo.git.revert('--no-commit', before_hash)

# commit the revert
repo.git.commit('-m', 'Revert last commit')

# push the changes
repo.git.push('origin', branch)
