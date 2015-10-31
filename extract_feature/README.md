You can extract feature following the official tutorial:

http://caffe.berkeleyvision.org/gathered/examples/feature_extraction.html

The feature would be saved to lmdb, and you may need to fetch the feature from lmdb using extra Python script.




If you want to extract feature and convert it to .mat (eg: if you want to train a SVM in Matlab using the extracted feature), you can use my script:

1. We’ll make a temporary folder to store things into.
 
mkdir examples/my_task/_temp

2. find `pwd`/data/my_data/train -type f -exec echo {} \; > examples/my_task/_temp/temp.txt



