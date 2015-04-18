#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

r = requests.get("https://projects.archlinux.org/")
soup = BeautifulSoup(r.text)
repos = soup.select(".sublevel-repo a")

repo_names = []
for repo in repos:
    repo_name = repo.string
    if repo_name[-4:] == ".git":
        repo_name = repo_name[:-4]
    repo_names.append(repo_name)

with open("projects.txt", mode = "w", encoding = "utf-8") as projects_file:
    for repo_name in repo_names:
        projects_file.write(repo_name + "\n")
