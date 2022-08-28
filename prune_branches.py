#!/usr/bin/python

import sys
from github import Github

# using an access token
g = Github("<token here>")

# print('Argument List:', str(sys.argv))

branch_list = ['main','master','dev','stable','prod']

repo = g.get_repo("xm94/zzztestrepo") #using my test repo for now

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
