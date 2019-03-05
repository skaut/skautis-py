#!/bin/bash

# This script is used by cron to periodically generate
# and auto-commit all changes to the skautIS API.

cd "/home/pi/Projects/skautis-py"

# Run api generator
./__venv__/bin/python skautis_api_gen.py

# Check if there are new changes to the API
if ! [[ `git status --porcelain` ]]; then
	echo "No changes"
	exit 0
fi

# Increment library version
perl -pe 's/(version=.\d+\.\d+\.)(\d+)/$1.($2+1)/e;' -i setup.py

# Commit changes
DATE=`date "+%d %b %Y"`
COMMIT_MESSAGE="Auto commit - $DATE"

echo "$COMMIT_MESSAGE"
git commit -am "$COMMIT_MESSAGE"

# push changes
# git push

