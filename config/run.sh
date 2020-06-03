#!/bin/bash


rm -rf /data/*


mkdir -p /data/db/001
mkdir -p /data/db/002
mkdir -p /data/db/003
mkdir -p /data/db/004
mkdir -p /data/db/005
mkdir -p /data/db/006
mkdir -p /data/db/011
mkdir -p /data/db/012
mkdir -p /data/db/013
mkdir -p /data/log


# https://docs.mongodb.com/manual/reference/configuration-options/
mongod --config /mongod-001.conf  # --shardsvr --port 27001 --dbpath /data/db/1 --logpath /data/log/1.log --replSet rs0 &
mongod --config /mongod-002.conf  # --shardsvr --port 27002 --dbpath /data/db/2 --logpath /data/log/2.log --replSet rs0 &
mongod --config /mongod-003.conf  # --shardsvr --port 27003 --dbpath /data/db/3 --logpath /data/log/3.log --replSet rs0 &
sleep 8
mongo --port 27001 < /init-27001.txt

mongod --config /mongod-004.conf  # --shardsvr --port 27004 --dbpath /data/db/4 --logpath /data/log/4.log --replSet rs1 &
mongod --config /mongod-005.conf  # --shardsvr --port 27005 --dbpath /data/db/5 --logpath /data/log/5.log --replSet rs1 &
mongod --config /mongod-006.conf  # --shardsvr --port 27006 --dbpath /data/db/6 --logpath /data/log/6.log --replSet rs1 &
sleep 8
mongo --port 27004 < /init-27004.txt

mongod --config /mongod-011.conf  # --configsvr --port 27011 --dbpath /data/db/7 --logpath /data/log/7.log --replSet configReplSet &
mongod --config /mongod-012.conf  # --configsvr --port 27012 --dbpath /data/db/8 --logpath /data/log/8.log --replSet configReplSet &
mongod --config /mongod-013.conf  # --configsvr --port 27013 --dbpath /data/db/9 --logpath /data/log/9.log --replSet configReplSet &
sleep 8
mongo --port 27011 < /init-27011.txt

# https://docs.mongodb.com/manual/reference/method/sh.shardCollection/
mongos --config /mongos-100.conf  # --configdb configReplSet/localhost:27011,localhost:27012,localhost:27013 --port 27100 &
sleep 8
mongo --port 27100 < /init-27100.txt


if [ -f /inited ]; then
	echo "Was inited"
else
	touch /inited
	echo "Is inited"
fi


tail -f /dev/null
