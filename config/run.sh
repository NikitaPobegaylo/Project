#!/bin/bash

# rm -rf /data/configdb
# rm -rf /data/db
# rm -rf /data/log

mkdir -p /data/db/1
mkdir -p /data/db/2
mkdir -p /data/db/3
mkdir -p /data/db/4
mkdir -p /data/db/5
mkdir -p /data/db/6
mkdir -p /data/db/7
mkdir -p /data/db/8
mkdir -p /data/db/9
mkdir -p /data/log

mongod --shardsvr  --port 27001 --dbpath /data/db/1 --logpath /data/log/1.log --replSet rs0 &
mongod --shardsvr  --port 27002 --dbpath /data/db/2 --logpath /data/log/2.log --replSet rs0 &
mongod --shardsvr  --port 27003 --dbpath /data/db/3 --logpath /data/log/3.log --replSet rs0 &

mongod --shardsvr  --port 27004 --dbpath /data/db/4 --logpath /data/log/4.log --replSet rs1 &
mongod --shardsvr  --port 27005 --dbpath /data/db/5 --logpath /data/log/5.log --replSet rs1 &
mongod --shardsvr  --port 27006 --dbpath /data/db/6 --logpath /data/log/6.log --replSet rs1 &


mongod --configsvr --port 27011 --dbpath /data/db/7 --logpath /data/log/7.log --replSet configReplSet &
mongod --configsvr --port 27012 --dbpath /data/db/8 --logpath /data/log/8.log --replSet configReplSet &
mongod --configsvr --port 27013 --dbpath /data/db/9 --logpath /data/log/9.log --replSet configReplSet &

mongos --configdb configReplSet/localhost:27011,localhost:27012,localhost:27013 --port 27100 &

# /init.sh

tail -f /dev/null