#!/bin/bash

sleep 2
mongo --port 27001 < /init-27001.txt
sleep 2
mongo --port 27004 < /init-27004.txt
sleep 2
mongo --port 27011 < /init-27011.txt
sleep 8
mongo --port 27100 < /init-27100.txt
sleep 1
