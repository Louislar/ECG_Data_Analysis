from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils  # 用來後續將 label 標籤轉為 one-hot-encoding  
import numpy
import input_HRV

from keras import optimizers
#強制使用CPU
#import tensorflow as tf
#import keras.backend.tensorflow_backend as KTF
#KTF.set_session(tf.Session(config=tf.ConfigProto(device_count={'gpu':0})))
#強制使用CPU
import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""


numpy.random.seed(7)

#讀入訓練資料
x_train, y_train = input_HRV.reda_in_hrv_data('train.csv')
x_test, y_test = input_HRV.reda_in_hrv_data('test.csv')

print(x_train.shape)    #(41033, 8)
print(y_train.shape)    #(41033, )
print(x_test.shape)
print(y_test.shape)

#label轉成one hot encode 的形式
print('原本的label')
print(y_train[0])
y_train_OneHot = np_utils.to_categorical(y_train, num_classes=2)
print('後來的label')
print(y_train_OneHot[0])
print(y_train_OneHot.shape)    #(41033, 2)
#test data set 的label也轉
y_test_OneHot = np_utils.to_categorical(y_test, num_classes=2)
print(y_test_OneHot.shape)


model = Sequential()
model.add(Dense(16, input_dim=8, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(2, activation='softmax'))
adam = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0001, amsgrad=False)
model.compile(loss='binary_crossentropy', optimizer=adam, metrics=['accuracy'])

train_history = model.fit(x=x_train, y=y_train_OneHot, validation_split=0.2, epochs=500, batch_size=128, verbose=2)

scores = model.evaluate(x_test, y_test_OneHot)

print('Scores: ')
print(scores)

#save model 
model.save('DNN_Model.m')