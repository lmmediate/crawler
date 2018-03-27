#!/usr/bin/env bash

export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# Script that clears out dir and runs spider in spiders directory.
#

rm -rf ./out/*
scrapy crawl dixy
scrapy crawl perekrestok


# EOF

