#!/bin/bash

FDATE=$(date +"%Y%m%dT%H%M%S")

media-ctl -d /dev/media1 --set-v4l2 '"ov5640 4-004c":0[fmt:SBGGR8_1X8/2592x1944@1/15]'
  media-ctl -d /dev/media1 -p > ${FDATE}_TEST_bayer_bggr8_SBGGR8_1X8_2592.txt 
ffmpeg -hide_banner -f rawvideo -pix_fmt bayer_bggr8 -s 2592x1944 -f video4linux2 -i /dev/video3 -vsync 2 -vframes 10 ${FDATE}_TEST_bayer_bggr8_SBGGR8_1X8_2592_%05d.jpg
