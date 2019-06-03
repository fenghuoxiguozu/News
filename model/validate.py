#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os,sys
import jieba
import numpy as np
import pandas as pd
# from model.fenci import *
from path import *
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer


mod=load_model(os.path.join(OUT_PATH,'model.h5'))
dict=np.load(os.path.join(OUT_PATH,'dict.npy'),allow_pickle=True).item()
stopwords=pd.read_table(STOPWORDS,names=['stopword'])['stopword'].tolist()

def clean(text):
    test_data = []
    texts = jieba.lcut(text)
    for text in texts:
        if text in stopwords or len(text)==1 or text.isdigit() or len(text)>4:
            continue
        else:
            test_data.append(text)
    return test_data

def vec(clean_data):
    vec=[]
    for text in clean_data:
        try:
            if dict[text]<=20000 :
                vec.append(dict[text])
            else:
                vec.append(0)
                # continue
        except:
            vec.append(0)
    return vec

if __name__ == '__main__':
    text = '平常上厕所的次数，比一般人还少，这样的生活习惯很容易导致水肿，尿不利自然没法有良好的新陈代谢。' \
           '水肿型肥胖的饮食减肥秘方说到饮食减肥，我们不得不说另外一个问题，那就体质。人的体质共分为两种，一种是热性体质，一种寒性体质。一般情况下来说，热性体质的人通常易流汗，不会有水肿问题，出现水肿现象的肥胖者，大多是寒性体质。不同的体质，其饮食减肥的方法也不同'
    cut=clean(text)
    vec=vec(cut)
    pad = pad_sequences([vec], maxlen=400, padding='post')
    print(pad)
    result=mod.predict_classes(pad)
    print(result)


