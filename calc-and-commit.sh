#!/bin/bash

echo "get the steps and calculate the progress"
python3 generate-analytics.py

echo "make the commit message"
commitmessage="Update the steps on $(date)"

echo "commit and push"
git commit acc-data.tsv Challenge.csv -m "$commitmessage"
git push

