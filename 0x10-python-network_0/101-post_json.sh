#!/bin/bash
# sends a json post request with the contents of the file
curl -X POST "$1"  -H "Content-Type: application/json" -d @"$2"
