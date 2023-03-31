#!/bin/bash
# DELETE URL and Displays the body of the response
curl -sI "$1" | grep -i "Allow" | cut -d ' ' -f 2-4
