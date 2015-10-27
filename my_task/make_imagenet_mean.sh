#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=/home/lisicheng/CNN_tools/caffe/examples/my_task
DATA=/home/lisicheng/CNN_tools/caffe/data/my_data
TOOLS=/home/lisicheng/CNN_tools/caffe/build/tools

$TOOLS/compute_image_mean $EXAMPLE/10_26_train_lmdb \
  $DATA/10_26_mean.binaryproto

echo "Done."
