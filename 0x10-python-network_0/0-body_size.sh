#!/bin/bash
# displays the size of the body of a requests response
curl -sI 0.0.0.0:5000 | grep -iF "Content-Length" | sed s/"Content-Length: "//
