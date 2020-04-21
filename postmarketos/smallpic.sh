#!/bin/bash

cd /home/wongkt2/dev

/home/wongkt2/py3/bin/python t1frame.py
./strans640jpg
convert second.jpg -rotate 90 secondr.jpg
convert secondr.jpg -resize 320 second.jpg
