#!/bin/bash

if [[ -n $(ifconfig wlan0 | grep "inet addr" | awk -F: '{print $2}' | awk '{print $1}') ]]; then

	python clock.py
else
	python localclock.py
fi

