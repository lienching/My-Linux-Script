#!/bin/bash

device=14  # your touchpad id in xinput ( use `xinput list` to check id ) 
state=`xinput list-props "$device" | grep "Device Enabled" | grep -o "[01]$"`

if [ "$state" -eq '1' ];then
  xinput --disable "$device"
  # notify-send is in package "libnotify-bin"
  notify-send "Toggling Touchpad" "Touchpad Disable"
else
  xinput --enable "$device"
  notify-send "Toggling Touchpad" "Touchpad Enable"
fi
