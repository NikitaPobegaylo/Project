#!/bin/bash


# https://docs.mongodb.com/manual/reference/configuration-options/
mongod --config /etc/mongod.conf

if [ -f /init.js ]; then
	if [ -f /inited ]; then
		echo "Was inited"
	else
		sleep 8
		mongo < /init.js
		touch /inited
		echo "Is inited"
	fi
fi


tail -f /dev/null
