from git import Repo, Git, exc  # import the exc module from git
import git  # import the git module
import os

# assuming PERSONAL_TOKEN is passed as an environment variable
token = os.getenv('PERSONAL_TOKEN')  # get the token
before_hash = os.getenv('BEFORE_HASH')  # get the hash of the commit to revert to 
branch = os.getenv('GITHUB_REF').split('/')[-1]  # get the branch that triggered the workflow
repo_dir = '.'  # directory of your repository

g = Git(repo_dir)

print('Token: ' + token)

# configure the url
g.config('--global', 'url."https://x-access-token:' + token + '@github.com/".insteadOf', 'https://github.com/')
g.config('--global', 'user.email', 'github-actions[bot]@users.noreply.github.com')
g.config('--global', 'user.name', 'github-actions[bot]')

repo = Repo(repo_dir)

# get the current branch


# revert the last commit
try:
    # try to revert the commit
    repo.git.revert('--no-commit', before_hash)
except git.exc.GitCommandError as e:
    if 'is a merge' in str(e):
        # if the commit is a merge commit, revert with -m option
        repo.git.revert('--no-commit', '-m', '1', before_hash)
    else:
        raise e

# commit the revert
repo.git.commit('-m', 'Revert last commit')

# push the changes
repo.git.push('origin', branch)
