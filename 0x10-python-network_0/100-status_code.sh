#!/bin/bash
# prints only the status code on terminal
curl -s "$1" -o /dev/null -w "%{http_code}"
