
USER_NAME = int(os.getenv('USER_NAME'))

action_content = """
name: Check Secrets

on: [push, pull_request]

jobs:
  check-secrets:
    runs-on: ubuntu-latest
    steps:
    - name: Check secrets
      run: |
        if [[ -z "${{ secrets.JIRA_${{ github.actor }}" ]]; then
          echo "JIRA secret for ${{ github.actor }} is not set"
          exit 1
        fi
"""

# Create the GitHub Action
action_path = ".github/workflows/check_secrets.yml"

# Define the commit message
commit_message = "Create check secrets workflow"

try:
    # Try to get the file
    contents = repo.get_contents(action_path)

    # If the file exists, update it
    repo.update_file(contents.path, commit_message, action_content, contents.sha)
except github.UnknownObjectException:
    # If the file does not exist, create it
    repo.create_file(action_path, commit_message, action_content)
