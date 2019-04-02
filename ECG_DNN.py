from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils  # 用來後續將 label 標籤轉為 one-hot-encoding  
import numpy
import input_HRV

numpy.random.seed(7)

#讀入訓練資料
x_train, y_train = input_HRV.reda_in_hrv_data('test.csv')

print(x_train.shape)    #(41033, 8)
print(y_train.shape)    #(41033, )

#label轉成one hot encode 的形式
y_train_OneHot = np_utils.to_categorical(y_train, num_classes=2)
print(y_train_OneHot.shape)    #(41033, 2)



model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(24, activation='relu'))
model.add(Dense(48, activation='softmax'))
model.add(Dense(24, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(2, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

train_history = model.fit(x=x_train, y=y_train_OneHot, validation_split=0.2, epochs=100, batch_size=2500, verbose=2)

#scores = model.evaluate()