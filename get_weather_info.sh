# !/bin/bash

echo "Enter Location:"
read location
if [ -z "$location" ]; then
  location="hsinchu"
fi
curl wttr.in/$location
