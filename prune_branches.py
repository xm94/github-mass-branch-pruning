#!/usr/bin/python

import sys
import json
from github import Github

f = open('config.json')
config = json.load(f)

#defaults
branch_list = ['main','master','dev','develop','development','stable','prod','production']
delete_prs = False

# overwrite config with file if it exists
if config["branch_list"]:
    branch_list = config["branch_list"]

if config["delete_prs"]:
    delete_prs = config["delete_prs"]

target_repo = config["target_repo"]
github_token = config["github_token"]

# using an access token
g = Github(github_token)
repo = g.get_repo(target_repo)

open_branches = []

# closes open PRs - put this behind logic
pulls = repo.get_pulls(state='open', sort='created')
for pr in pulls:
    pr.edit(state='closed')
    print(pr)

for branch in repo.get_branches():
    if branch.name not in branch_list:
        print("Adding " + branch.name)
        open_branches.append("refs/heads/" + branch.name)

print("Found " + str(len(open_branches)) + " branches!")


for ref in repo.get_git_refs():
    if ref.ref in open_branches:
        print("Removing " + ref.ref)
        ref.delete()
