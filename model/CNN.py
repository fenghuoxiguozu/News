import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from path import *
from sklearn.utils import shuffle
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Embedding,Convolution1D,MaxPool1D,Flatten
from keras.layers.recurrent import SimpleRNN,LSTM
from keras.layers import Dense,Dropout
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.optimizers import Adam

maxlen=400  #向量维度
num_words=20000 #索引字典长度
epochs=20 #训练次数

Tip_Num={'体育':0,'娱乐':1,'家居':2,'彩票':3,'房产':4,'教育':5,'时尚':6,
 '时政':7,'星座':8,'游戏':9,'社会':10,'科技':11,'股票':12,'财经':13 }


df=pd.read_csv(os.path.join(OUT_PATH,'Cleaned_NEWS.csv'),names=None)
df=shuffle(df)

all_texts=df['News'].astype(str).tolist()

tokenizer=Tokenizer(num_words=num_words,lower=True)
tokenizer.fit_on_texts(all_texts)
np.save(os.path.join(OUT_PATH,'dict.npy'),tokenizer.word_index)
sequences=tokenizer.texts_to_sequences(all_texts)
vocab_size=len(tokenizer.word_index)+1 #得到每个词的编号 698335
print('vocab_size:',vocab_size)
X=pad_sequences(sequences,padding='post',maxlen=maxlen) #将超过固定值的部分截掉，不足的在最前面用0填充

df['Tip']=df['Tip'].map(Tip_Num)
Y=np_utils.to_categorical(df['Tip'].values,num_classes=14)
print(X.shape,Y.shape)  # (318150, 400) (318150, 14)


model=Sequential()
model.add(Embedding(input_dim=num_words,output_dim=256,input_length=maxlen))
model.add(Dropout(0.1))
model.add(Convolution1D(128, 3, padding='same'))
model.add(MaxPool1D(3,3,padding='same'))
model.add(Dropout(0.2))
model.add(Convolution1D(64, 3, padding='same'))
model.add(Flatten())
model.add(Dropout(0.1))
model.add(Dense(units=32,activation='relu'))
model.add(Dense(units=14,activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer=Adam(lr=0.001),metrics=['accuracy'])
history=model.fit(X,Y,epochs=epochs,batch_size=256,validation_split=0.2)
loss1,acc1=model.evaluate(X,Y)
print('训练集准确度：',acc1)
model.summary()
model.save(os.path.join(OUT_PATH,'model.h5'))

#绘制 acc，loss
acc = history.history['acc']
loss = history.history['loss']
print(acc,loss)

x=range(1,epochs+1)
plt.plot(x,acc, 'r', label='Training acc')
plt.plot(x,loss, 'b', label='Training loss')
plt.title('Training acc and loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
plt.savefig('acc-loss.png')