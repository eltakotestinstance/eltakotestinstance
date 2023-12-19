from git import Repo, Git, exc  # import the exc module from git
import git  # import the git module
import os
import re

# assuming PERSONAL_TOKEN is passed as an environment variable
token = os.getenv('PERSONAL_TOKEN')  # get the token
before_hash = os.getenv('BEFORE_HASH')  # get the hash of the commit to revert to 
branch = os.getenv('GITHUB_REF').split('/')[-1]  # get the branch that triggered the workflow
repo_dir = '.'  # directory of your repository


# assuming repo_dir is the directory of your repository
repo_dir = '.'
repo = Repo(repo_dir)

modified_files = False
# get the commits between the previous commit and the current commit
commits = list(repo.iter_commits('HEAD...{}'.format(before_hash)))

search_strings = ["secrets.PERSONAL_TOKEN"]

for commit in commits:
    print("Checking commit {}".format(commit))
    print("Previous commit:")
    print(commit.parents[0])  # print the previous commit
    # get the diff between the current commit and the previous commit
    diff_index = commit.diff(commit.parents[0])
    # get the names of the modified files
    modified_file_names = [diff.a_path for diff in diff_index.iter_change_type('M')]
    for file_name in modified_file_names:
        # check if the file name matches the pattern
        if re.search(r'protected_.*', file_name):
            print("Found modified protected github workflow files")
            modified_files = True
            break
    diff_index = commit.diff(commit.parents[0])
    # iterate over each diff
    for diff in diff_index.iter_change_type('M'):
        content = diff.a_blob.data_stream.read().decode()
        for search_string in search_strings:
            if search_string in content:
                print("Found '{}' in commit modifications".format(search_string))
                modified_files = True
                break
    if modified_files:
        break

if modified_files:
    print("Reverting commit {}".format(commit))
    """
    g = Git(repo_dir)

    # configure the url
    g.config('--global', 'url.https://x-access-token:' + token + '@github.com/.insteadOf', 'https://github.com/')
    g.config('--global', 'user.email', 'github-actions[bot]@users.noreply.github.com')
    g.config('--global', 'user.name', 'github-actions[bot]')

    repo = Repo(repo_dir)

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
    """
