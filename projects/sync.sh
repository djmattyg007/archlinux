#!/bin/bash

BASEDIR=$PWD
BASEURL="https://projects.archlinux.org/git"
PROJECTS=`cat projects.txt`

for project in $PROJECTS; do
	cd $BASEDIR
	path_to_project=`dirname $project`
	if [[ ! -d "$path_to_project" ]]; then
		/usr/bin/mkdir -p $path_to_project
	fi
	cd $path_to_project

	project_folder=`basename $project`
	echo "Updating $project"
	if [[ -d "$project_folder" ]]; then
		cd $project_folder
		tracking_branch=$(/usr/bin/git rev-parse --abbrev-ref --symbolic-full-name @{u})
		/usr/bin/git fetch -p origin
		/usr/bin/git merge $tracking_branch
	else
		/usr/bin/git clone "$BASEURL/$project"".git"
	fi
done
