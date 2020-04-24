#!/usr/bin/env python3

from v4l2 import *
import fcntl
import mmap
import select
import time

vd = open("/dev/video1", "rb+", buffering=0)


cp = v4l2_capability()
fcntl.ioctl(vd, VIDIOC_QUERYCAP, cp)

fmt = v4l2_format()
fmt.type = V4L2_BUF_TYPE_VIDEO_CAPTURE
fcntl.ioctl(vd, VIDIOC_G_FMT, fmt)  # get current settings
fcntl.ioctl(vd, VIDIOC_S_FMT, fmt)  # set whatever default settings we got before

parm = v4l2_streamparm()
parm.type = V4L2_BUF_TYPE_VIDEO_CAPTURE
parm.parm.capture.capability = V4L2_CAP_TIMEPERFRAME

req = v4l2_requestbuffers()
req.type = V4L2_BUF_TYPE_VIDEO_CAPTURE
req.memory = V4L2_MEMORY_MMAP
req.count = 1  # nr of buffer frames
fcntl.ioctl(vd, VIDIOC_REQBUFS, req)  # tell the driver that we want some buffers


buffers = []

for ind in range(req.count):
    # setup a buffer
    buf = v4l2_buffer()
    buf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE
    buf.memory = V4L2_MEMORY_MMAP
    buf.index = ind
    fcntl.ioctl(vd, VIDIOC_QUERYBUF, buf)

    mm = mmap.mmap(
        vd.fileno(),
        buf.length,
        mmap.MAP_SHARED,
        mmap.PROT_READ | mmap.PROT_WRITE,
        offset=buf.m.offset,
    )
    buffers.append(mm)

    # queue the buffer for capture
    fcntl.ioctl(vd, VIDIOC_QBUF, buf)


buf_type = v4l2_buf_type(V4L2_BUF_TYPE_VIDEO_CAPTURE)
fcntl.ioctl(vd, VIDIOC_STREAMON, buf_type)


t0 = time.time()
max_t = 1
ready_to_read, ready_to_write, in_error = ([], [], [])
while len(ready_to_read) == 0 and time.time() - t0 < max_t:
    ready_to_read, ready_to_write, in_error = select.select([vd], [], [], max_t)

vid = open("1frame.yuv", "wb")

for _ in range(1):  # capture 100 frames
    buf = v4l2_buffer()
    buf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE
    buf.memory = V4L2_MEMORY_MMAP
    fcntl.ioctl(vd, VIDIOC_DQBUF, buf)  # get image from the driver queue
    # print("buf.index", buf.index)
    mm = buffers[buf.index]
    # print first few pixels in gray scale part of yuvv format packed data
    vid.write(mm.read())  # write the raw yuyv data from the buffer to the file
    # vid.write(bytes((bit for i, bit in enumerate(mm.read()) if not i % 2)))  # convert yuyv to grayscale
    mm.seek(0)
    fcntl.ioctl(vd, VIDIOC_QBUF, buf)  # requeue the buffer

fcntl.ioctl(vd, VIDIOC_STREAMOFF, buf_type)
vid.close()
vd.close()
