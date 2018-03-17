#!/usr/bin/env bash

if [ -f ./spider_daemon.swp ]
then
    exit 1
fi


touch ./spider_daemon.swp


while :
do
    ./run_spider.sh
sleep 1h

done


# EOF

