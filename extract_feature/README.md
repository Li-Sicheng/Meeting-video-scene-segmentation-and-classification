You can extract feature following the official tutorial:

http://caffe.berkeleyvision.org/gathered/examples/feature_extraction.html

The feature would be saved to lmdb, and you may need to fetch the feature from lmdb using extra Python script.

----------------------------------------------------------------------------------------------------------------


If you want to extract feature and convert it to .mat (eg: if you want to train a SVM in Matlab using the extracted feature), you can use my script:

1.We’ll make a temporary folder to store things into.
 
    mkdir examples/my_task/_temp

2.Generate a list of the files to process. We’re going to use our own images.

    find `pwd`/data/my_data/train -type f -exec echo {} \; > examples/my_task/_temp/temp.txt

3.The ImageDataLayer we’ll use expects labels after each filenames, so let’s add a 0 to the end of each line.

    sed "s/$/ 0/" examples/my_task/_temp/temp.txt > examples/my_task/_temp/file_list.txt

4.Let’s copy and modify the network definition. We’ll be using the ImageDataLayer, which will load and resize images for us.

    cp examples/feature_extraction/imagenet_val.prototxt examples/my_task/_temp

Tips: Modify data layer (pathes of mean.binaryproto and file_list.txt), so you need to have your own mean.binaryproto in advance.

5.Put these 3 scripts in &CAFFE_ROOT. Modify extract_feature.sh

Tips: BATCHSIZE * BATCHNUM = the size of your images!!



