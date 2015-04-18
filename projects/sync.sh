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
	if [[ -d "$project_folder" ]]; then
		cd $project_folder
		/usr/bin/git pull origin master
	else
		/usr/bin/git clone "$BASEURL/$project"".git"
	fi
done
