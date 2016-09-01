#! /bin/sh
echo "Sync time with tw.pool.ntp.org"
ntpdate tw.pool.ntp.org
date; sudo hwclock -r
echo "Sync End"
