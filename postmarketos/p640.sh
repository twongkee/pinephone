#!/bin/bash

FDATE=$(date +"%Y%m%dT%H%M%S")
FFMPEG=/home/wongkt2/dev/ffmpeg/ffmpeg/ffmpeg

R=45
RATE=@1/${R}
#media-ctl -d /dev/media1 --set-v4l2 '"ov5640 4-004c":0[fmt:SBGGR8_1X8/640x480${RATE}]'
media-ctl -d /dev/media1 --set-v4l2 '"ov5640 4-004c":0[fmt:UYVY8_2X8/640x480'${RATE}']'

#FMT=bayer_bggr8
FMT=yuv420p
${FFMPEG} -hide_banner -f rawvideo -pix_fmt ${FMT} -s 640x480 -f video4linux2 -i /dev/video3 -vsync 2 -vframes 20 ~/Pictures/${FDATE}_vid.yuv
${FFMPEG} -hide_banner -f rawvideo -pix_fmt ${FMT} -s 640x480 -i ~/Pictures/${FDATE}_vid.yuv -vsync 2 -vframes 20 ~/Pictures/${FDATE}_R${R}_%05d.jpg
