#!/bin/bash
git add *.py
git add README.md
read -p 'input commit information:'
git commit -m "$REPLY"
git push