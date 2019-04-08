from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils  # 用來後續將 label 標籤轉為 one-hot-encoding  
import numpy
import input_HRV
import numpy as np

from keras import optimizers
#強制使用CPU
#import tensorflow as tf
#import keras.backend.tensorflow_backend as KTF
#KTF.set_session(tf.Session(config=tf.ConfigProto(device_count={'gpu':0})))
#強制使用CPU
import os

#import load model package
from keras.models import load_model
model = load_model('DNN_Model.m')
inputArray = np.array([10387.275663716815, 269105.3382682419, 66.8141592920354, 210452557489.1899, 299326795.12177527, 1046303.398823812, 286.0803046786042, 99.65166541079165])
inputArray = inputArray.reshape([1, 8])
print(inputArray.shape)
print(model.predict(inputArray))