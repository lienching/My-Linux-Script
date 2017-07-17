#!/bin/bash
# This script will only work in gnome desktop enviroment

state=`gsettings get org.gnome.desktop.peripherals.touchpad send-events`

if [[ $state == "'disabled'" ]];then  
  gsettings set org.gnome.desktop.peripherals.touchpad send-events 'enabled'
  # notify-send is in package "libnotify-bin"
  notify-send "Toggling Touchpad" "Touchpad Enabled"
else
  gsettings set org.gnome.desktop.peripherals.touchpad send-events 'disabled'
  notify-send "Toggling Touchpad" "Touchpad Disabled"
fi
