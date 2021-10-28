#!/bin/bash

# Check if there are new changes to the API
if ! [[ `git status --porcelain skautis` ]]; then
	echo "No changes"
	exit 0
fi

# Increment library version
perl -pe 's/(version=.\d+\.\d+\.)(\d+)/$1.($2+1)/e;' -i setup.py

# Set up git identity
git config --global user.name 'Automatic commit'
git config --global user.email 'kulikjak@users.noreply.github.com'

# Commit changes
DATE=`date "+%d %b %Y"`
VERSION=`awk -F"'" '/version=/ {print $2}' setup.py`
COMMIT_MESSAGE="Auto commit version $VERSION - $DATE"

echo "$COMMIT_MESSAGE"
# this is needed to include removed and newly introduced files
git add --all skautis
git commit -m "$COMMIT_MESSAGE"

git tag -a "v${NEW_VERSION}" -m "Automatically generated version ${NEW_VERSION}"

# push changes
git push --follow-tags
