#!/bin/bash

device=14  # your touchpad id in xinput ( use `xinput list` to check id ) 
state=`xinput list-props "$device" | grep "Device Enabled" | grep -o "[01]$"`

if [ "$state" -eq '1' ];then
  xinput --disable "$device"
  notify-send "Touchpad Disable"  # notify-send is in package "libnotify-bin"
else
  xinput --enable "$device"
  notify-send "Touchpad Enable"
fi
