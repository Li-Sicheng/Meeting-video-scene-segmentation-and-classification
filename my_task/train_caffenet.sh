#!/usr/bin/env sh

./build/tools/caffe train \
    --solver=examples/my_task/bvlc_alexnet/solver.prototxt
