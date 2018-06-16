# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import base64
import string
import random
import traceback
import time
import requests
import json
import base64
import string
import random
import traceback
import time
from . import settings
import requests
import base64
import json
import random
from sklearn.neighbors import KDTree
import numpy as np
from . import extract_cnn_vgg16_keras #import VGGNet
import numpy as np
import h5py
import matplotlib.image as mpimg
from sklearn import svm
from django.http import HttpResponseRedirect

data={}



h5f = h5py.File("static/whm_model1",'r')
feats = h5f['dataset_1'][:]
print(feats.shape)
imgNames = h5f['dataset_2'][:]
h5f.close()
model = extract_cnn_vgg16_keras.VGGNet()





def home(request):
#    data={}
    return render(request, 'home.html')



def image_feedback(request):
    print("dadadasdadad")
    return render(request,'feedback.html',data)

#def image_feedback_vector(request):
#    print("11111")
#    dat={}
#    dat["checkID"]=request.GET['checkID']
#    print("####!")
#    print(dat["checkID"])
#    print("####!")
#    return render(request,'feedback.html',dat)

def imagesplite(request):
    dataa={}
    dataa["image_raw"]=request.GET['image_raw']
#    print(dataa)
#    print("sssssssssssssss"),
    return render(request, 'photocutter.html',dataa)




# capture pic image
#http://www.cnblogs.com/linxiyue/p/4038436.html about request.FILES
@csrf_exempt
def recognise(request):
    try:
        f = request.FILES['image']
        
        k=request.POST.getlist("selectt")
        print(k)
        print("%%%%%%%%%%%")
        
        
        #Return a k length list of unique elements chosen from the population sequence
        get_pic_name= f.name + ''.join(random.sample(string.ascii_letters + string.digits, 3))
        # store the file in disk
        with open('static/img/'+get_pic_name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        print ('[INFO]:',request.method)
        print ('[INFO]:get from upload')
    except:
        get_pic_name = request.GET['image_name']
        print ('[INFO]:',request.method)
        print ('[INFO]:get from click image')
    finally:
        print ('[INFO]:Get',get_pic_name,'\n')
        
        
        
        
       
        print ("--------------------------------------------------")
        print ("               searching starts")
        print ("--------------------------------------------------")
        queryDir = "static/img/"+get_pic_name
        queryImg = mpimg.imread(queryDir)
        
#        a=time.time()
# extract query image's feature, compute simlarity score and sort
        queryVec = model.extract_feat(queryDir)
        #print(len(queryVec))
#        b=time.time()
#        print("Algorithm run time is %d"%(b-a))
        scores = np.dot(queryVec, feats.T)
        rank_ID = np.argsort(scores)[::-1]
        #argsort函数返回的是数组值从小到大的索引值
        rank_score = scores[rank_ID]
        #print rank_ID
        #print rank_score


# number of top retrieved images to show
        maxres=8
        imlist = [imgNames[index] for i,index in enumerate(rank_ID[0:maxres])]
        print ("top %d images in order are: " %maxres, imlist)
    
        
        
        
        
        
        
        
        
        global data
        data={}
        data["image_name"] = get_pic_name
        data['result'] = []
        
        
        
        #cur_list = [1,2,4,5,7,12,18,15]
        #np.random.shuffle(cur_list)
        for i in imlist:
            data['result'].append(i.decode())
        return render(request, 'search.html',data)
