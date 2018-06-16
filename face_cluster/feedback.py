# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from sklearn import svm
import numpy as np
import h5py
print("THIS IS THE FEEDBACK")
h5f = h5py.File("static/whm_model1",'r')
feats = h5f['dataset_1'][:]
imgNames = h5f['dataset_2'][:]
h5f.close()


def feedback(request):
     dataa={}
#     print("1111")
     print(request.GET)
     check=[]
     check_index=[]
     listimgNames=imgNames.tolist()
#     print(imgNames[3])
     all_images=[]
     uncheck=[]
     uncheck_index=[]

     
     
     
     for key, value in request.GET.items():
         if key.startswith(('checkID')):
#             print(value)
             check.append(value.encode())
#         listimgNames.index
         if key.startswith(('all_imgs')):
             all_images.append(value.encode())


     print("all images is:")
     print(all_images)
     print("all checked images is:")
     print(check)
     uncheck=list(set(check)^set(all_images))
     print("The uncheck image is:")
     print(uncheck)
     for con in check:
         check_index.append(listimgNames.index(con))
     print("The checked index is:")
     print(check_index)

     for uncon in uncheck:
         uncheck_index.append(listimgNames.index(uncon))
     print("The unchecked index is:")
     print(uncheck_index)
#     print(feats[1:3])

     
#     print(feats[list])
     train_x1=feats[check_index]
     train_x=np.vstack((train_x1,feats[uncheck_index]))
#     .tolist()
#     print(len(train_x))
#     train_x=np.array(train_x)
     print("the train_x shape is (%d,%d)"%train_x.shape)
     print(train_x)


     row=train_x1.shape[0]
     train_y=np.ones((row,1))
     row2=train_x.shape[0]-row
     train_y2=np.zeros((row2,1))#制造负样本
     train_y=np.vstack((train_y,train_y2))
     print(train_y)

     clf = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovo')
     clf.fit(train_x, train_y)
     test_x=feats
     test_y=clf.predict(test_x)
     print(test_y)
     count_one=0
     for one_1 in test_y:
         if one_1==1:
             count_one=count_one+1
     print("one has %d "%count_one)
     rank_ID = np.argsort(clf.decision_function(test_x))[::-1]
     
     
     maxres=8
     imlist = [imgNames[index] for i,index in enumerate(rank_ID[0:maxres])]
     print ("top %d images in order are: " %maxres, imlist)



     dataa['result'] = []
     for i in imlist:
        dataa['result'].append(i.decode())

     return render(request,'search3.html',dataa)

