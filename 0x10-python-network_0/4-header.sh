#!/bin/bash
# Bash script that sends a GET request and displays the body
curl -s "$1" -X GET -H 'X-HolbertonSchool-User-Id: 98'
