# This is a program that will read a file from a repository, replace all the instances of the text "Andrew" with "Emma"
# Author: Emma Dunleavy


# Required import statements
from github import Github
from config import cfg as cfg

# Initialize a Github instance using github token stored in config.py file in same directory:
github_instance = Github(cfg['githubkey']['githubkey'])

# Get the repository object:
repo = github_instance.get_repo("emma2d/WSAA-coursework")

# The path of the file in the repository
file_path = 'assignments/assignment04.txt'

# Retrieve the file from the repository
contents = repo.get_contents(file_path, ref="main")  

# Decode the file content
file_content = contents.decoded_content.decode("utf-8")

# Replace 'Andrew' with 'Emma' in the file content
updated_content = file_content.replace('Andrew', 'Emma')

# Update the file in the repository
try:
    repo.update_file(contents.path, "Replace instances of 'Andrew' with 'Emma'", updated_content, contents.sha, branch="main")  
    print("File updated successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

