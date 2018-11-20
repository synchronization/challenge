#!/bin/bash

# get the steps and calculate the progress
python generate-analytics.py

# make the commit message
commitmessage="Update the steps on $(date)"

# commit and push
git commit acc-data.tsv Challenge.csv -m "$commitmessage"
git push

