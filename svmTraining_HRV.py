import numpy as np
from pylab import plt
import sklearn.externals.joblib as joblib
import pandas as pd  
from sklearn import cross_validation, svm, preprocessing, metrics

import input_HRV

#讀入資料
test_x, test_y = input_HRV.reda_in_hrv_data('test.csv')
train_x, train_y = input_HRV.reda_in_hrv_data('train.csv')

#test資料樣子
print(test_x.shape)
print(test_y.shape)
print(type(test_x[0][0]))
print(type(test_y[0]))
#train資料樣子
print(train_x.shape)
print(train_y.shape)
print(type(train_x[0][0]))
print(type(train_y[0]))


#import svm
from sklearn.svm import SVC

svc_model=SVC(kernel='linear')

#會train超久
svc_model.fit(test_x, test_y)

print('training Done')