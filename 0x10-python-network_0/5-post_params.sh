#!/bin/bash
# Bash script sends a POST request and displays the body
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
