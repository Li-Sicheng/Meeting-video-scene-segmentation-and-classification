Finetune a net based on a pretrained caffemodel:

1.You should in advance have these 3 files:

    train_val.prototxt (defining the net structure. Here is "train_val_origin.prototxt")
    
    solver.prototxt (defining parameters about training)
    
    pretrained caffemodel (you should have the pretrained model in advance. Here should be AlexNet)
    
2.Modify finetune.sh and run it.

    -- solver: the path of solver.prototxt
    
    -- weights: the path of the pretrained caffemodel 
    

