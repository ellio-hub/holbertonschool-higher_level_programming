#!/bin/bash
#  Bash script sends a delete request to URL and displays the body
curl -s "$1" -X DELETE
