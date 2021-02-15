import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
from data import Dataset
from keras.layers import LSTM,Dense,Dropout
from keras.models import Sequential
from keras import optimizers

import tensorflow as tf
config=tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess=tf.compat.v1.Session(config=config)

seq_length=60
data=Dataset(seq_length)
x_train,y_train,x_test,y_test=data.get_rnn_input()
simples=len(data.val_data)+len(data.train_data)

model=Sequential()
model.add(LSTM(2048,input_shape=(seq_length,2048) ))

model.add(Dense(1,activation='sigmoid'))
model.compile(optimizer=optimizers.RMSprop(),
              loss='binary_crossentropy',
              metrics=['acc'])

history=model.fit(x_train,y_train,batch_size=128,epochs=20,validation_data=(x_test,y_test))

