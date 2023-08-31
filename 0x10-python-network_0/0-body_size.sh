#!/bin/bash
# displays the size of the body of a requests response
curl -sI "$1" | grep -iF "Content-Length" | sed s/"Content-Length: "//
