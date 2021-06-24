#!/bin/bash
# Bash script use URL sends a request to display size of the body
curl -sI "$1" | grep 'Content-Length:' | cut -c 17-
