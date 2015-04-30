#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import simplediff
from pprint import pprint

r = requests.get("https://projects.archlinux.org/")
soup = BeautifulSoup(r.text)
repos = soup.select(".sublevel-repo a")

with open("projects.txt", mode = "r", encoding = "utf-8") as projects_file:
    cur_repos = projects_file.readlines()

new_repos = []
for repo in repos:
    repo_name = repo.string
    if repo_name[-4:] == ".git":
        repo_name = repo_name[:-4]
    new_repos.append(repo_name + "\n")

repo_diff = simplediff.string_diff(''.join(cur_repos), ''.join(new_repos))
added = []
removed = []
for (diff_type, values) in repo_diff:
    if diff_type == "+":
        added.extend(values)
    elif diff_type == "-":
        removed.extend(values)

if added:
    print("Added:")
    pprint(added)
if removed:
    print("Removed:")
    pprint(removed)

if added or removed:
    with open("projects.txt", mode = "w", encoding = "utf-8") as projects_file:
        for repo_name in new_repos:
            projects_file.write(repo_name)
else:
    print("No projects were added or removed.")
