import jieba
import re
import pandas as pd
from path import *


def stop(news):
    stop_list = []
    for x in news.split(' '):
        if x in stopwords or len(x)==1 or x.isdigit() or len(x)>4:
            continue
        stop_list.append(x)
    return ' '.join(stop_list)


if __name__ == '__main__':
    df = pd.read_csv(os.path.join(OUT_PATH, 'NEWS.csv'))
    stopwords=pd.read_table(STOPWORDS,names=['stopword'])['stopword'].tolist()

    print("》》》分词开始》》》》")
    df['News'] = df['News'].astype(str).apply(lambda x: ' '.join(jieba.lcut(x)))
    print("分词完成！！！")
    print("》》》加载停用词开始》》》》")
    df['News'] =df['News'].apply(stop)
    print("加载停用词完成！！！")
    print("》》》去除无用符号开始》》》》")
    df['News'] = df['News'].apply(lambda x:re.sub(r'[\d+\.\d+]|%|','',x))
    print("数据预处理完成！！！")
    df.to_csv(os.path.join(OUT_PATH, 'Cleaned_NEWS.csv'),index=None)