# Image-Retrieval-With-User-Feedback
About: with picture cut and the user feedback based on SVM, this is the final course design in my university, i do this project with a lot of other's open source code, show my thx to all these guy~

## requirement
keras
<br>
python3
<br>
h5py
<br>
sklearn
<br>
You can install all by the command (pip3 install *** )

## File structure

```structure
├── README.md
├── index.py
├── face_cluster
│   │ 
│   ├── controller.py
│   ├── controller.pyc
│   ├── controller_det.py
│   ├── controller_image.py
│   ├── controller_image.pyc
│   ├── extract_cnn_vgg16_keras.py
│   ├── feedback.py
│   ├── settings.py
│   ├── settings.pyc
│   ├── urls.py
│   ├── urls.pyc
│   ├── wsgi.py
│   └── wsgi.pyc
├── manage.py
├── static
│   ├── img
│   │   ├── 12_t.jpg
│   │   ├── 13_t.jpg
│   │   ├── 14_t.jpg
│   │   ├── 15_t.jpg
│   │   ├── 16_t.jpg
│   │   ├── dataset1----------------------------------------------this file contain your own image
│   │ 
│   │ 
│   ├── index file --------------------------------------this file is your index file,you can get it from the train step
│
│
└── template
    ├── feedback.html
    ├── home.html
    ├── home2.html
    ├── photocutter.html
    ├── search.html
    ├── search.html.det
    ├── search2.html
    └── search3.html
```

## Usage
### First. Train The index file 
In this step you should train a index file for your own image database, you can get it by
`python3 index.py -database <path-to-dataset> -index <name-for-output-index>` the <path-to-dataset> is the path to your own dataset1. then it will generate a index file, and you should put it into the (static/) file. maybe in this step you should download some file like vgg16_weights_tf_dim_ordering_tf_kernels.h5 etc. please wait....
### Run The System
In this step, you should can use `python3 manager.py runserver` and you can use visit `127.0.0.1`to see the web.

## The System demo picture

