import pandas as pd
import os
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
from path import *

df=pd.read_csv(os.path.join(OUT_PATH,'Cleaned_NEWS.csv'))


news=df['News'].astype(str).apply(lambda x:len(x)//3.3)
print(news.values)
plt.scatter(news.index.values,news.values,s=5,c='r',alpha=0.5)
# plt.bar(news.index,news.values,color='#4F94CD',label='新闻长度分布图')
# plt.xlim(0,4)
plt.ylim(0,1200)
# plt.legend(loc='upper left') .value_counts()
plt.show()

#1200