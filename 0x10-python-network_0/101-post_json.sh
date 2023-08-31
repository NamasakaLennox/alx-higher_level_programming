#!/bin/bash
# sends a json post request with the contents of the file
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
