#!/bin/bash
# Bash script displays all HTTP methods the server will accept
curl -sI "$1" -X OPTIONS | grep "Allow" | cut -c 8-
