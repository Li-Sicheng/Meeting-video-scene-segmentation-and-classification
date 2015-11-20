#!/usr/bin/env sh
TOOLS=/home/lisicheng/CNN_tools/caffe/build/tools
GLOG_logtostderr=1
$TOOLS/caffe train --solver /home/lisicheng/CNN_tools/caffe/examples/my_task/fine_tune/solver.prototxt --weights /home/lisicheng/CNN_tools/caffe/examples/my_task/fine_tune/bvlc_alexnet.caffemodel
