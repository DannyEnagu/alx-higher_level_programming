#!/bin/bash
# Displays the size of the body of the response
curl -s -I "$1" | grep -i "Content-Length" | cut -d ' ' -f 2
