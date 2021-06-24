#!/bin/bash
# Bash script that sends a JSON POST request and displays the body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
