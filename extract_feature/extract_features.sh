rgs for EXTRACT_FEATURE
# TOOL=../../build/tools
MODEL=models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel  #pre-trained caffemodel
PROTOTXT=examples/my_task/_temp/imagenet_val.prototxt #net structure
LAYER=fc7 #feature to be extracted
LEVELDB=examples/my_task/_temp/features_leveldb #address to save the feature
BATCHSIZE=1
TYPE=leveldb #save to lmdb/leveldb

# args for LEVELDB to MAT
DIM=4096 #length of feature(compute by yourself)
OUT=examples/my_task/_temp/features.mat #address to save the feature(.mat)
BATCHNUM=1

./build/tools/extract_features.bin $MODEL $PROTOTXT $LAYER $LEVELDB $BATCHSIZE $TYPE
python leveldb2mat.py $LEVELDB $BATCHNUM  $BATCHSIZE $DIM $OUT
