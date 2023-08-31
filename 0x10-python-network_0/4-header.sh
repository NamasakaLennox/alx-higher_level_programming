#!/bin/bash
# sends a get request to the url and displays the body of a response
# a header variable must be included
curl -s "$1" -H "X-School-User-Id: 98"
