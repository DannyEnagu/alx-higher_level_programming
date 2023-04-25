#!/bin/bash
# send a POST request with the contents of a file
curl -sH "Content-Type: application/json" -d @"$2" -X "POST" "$1"
