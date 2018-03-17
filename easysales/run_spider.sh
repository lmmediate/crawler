#!/usr/bin/env bash

# Script that clears out dir and runs spider in spiders directory.
#

rm -rf ./out/*
scrapy runspider ./src/spiders/dixy_spider.py -o ./out/sales.json


# EOF

