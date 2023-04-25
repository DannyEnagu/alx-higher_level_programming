#!/bin/bash
# causes the server to respond with a message containing You got me!
curl -sX PUT -Lu test:password 0.0.0.0:5000/catch_me
