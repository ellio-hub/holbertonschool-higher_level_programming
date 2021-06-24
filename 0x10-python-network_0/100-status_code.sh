#!/bin/bash
# Bash script sends a request and displays only the status code
curl -so /dev/null --write-out "%{http_code}" "$1"
