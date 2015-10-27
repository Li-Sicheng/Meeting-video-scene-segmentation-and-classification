# Meeting-video-scene-segmentation-and-classification
Usage of Caffe:
1.Prepare your datasets
	1.1 Put your images in "my_data/train" and "my_data/val"
	1.2 Write your labels in "train.txt" and "val.txt"
	1.3 Put "my_data" in "caffe_root/data/"

2.Process your datasets
	2.1 Put "my_task" in "caffe_root/example/"
	2.2 Convert your datasets to lmdb
		2.2.1 Revise "my_task/create_imagenet.sh" (Revise the pathes)
		2.2.2 Run "my_task/create_imagenet.sh"
	2.3 Compute the mean of your datasets
		2.3.1 Revise "my_task/make_imagenet_mean.sh" (Revise the pathes)
		2.3.2 Run ""my_task/make_imagenet_mean.sh"
3.Define your net
	3.1 Revise "my_task/bvlc_alexnet/train_val.prototxt" (Revise the pathes of data layer.You can also write your own net here.)
	3.2 Revise "my_task/bvlc_alexnet/solver.prototxt" (Revise the pathes and the paramerters)
4.Train
	4.1 Revise "my_task/train_caffenet.sh" 
	    (Revise to: ./build/tools/caffe train --solver=examples/my_task/bvlc_alexnet/solver.prototxt)
	4.2 Enter the "caffe_root"
	4.3 Enter: ./build/tools/caffe train --solver=examples/my_task/bvlc_alexnet/solver.prototxt

To be continued...
