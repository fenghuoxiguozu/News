from path import *
import os
import pandas as pd

labels=os.listdir(FILE_PATH)

txts=[]
tips=[]

def read(FILE_PATH):
    for label in labels:  #分类标签
        print("正在读取《{}》主题.....".format(label))
        files = os.listdir(os.path.join(FILE_PATH,label))  #分类下所有txt文件
        for file in files:
            txt_path=os.path.join(FILE_PATH,label,file)  #读取txt
            with open (txt_path,'r',encoding='utf-8') as f:
                data=''.join(f.readlines()).replace('\n','')  #合并txt里所有数据
                data=''.join(data.split())
                txts.append(data)
                tips.append(label)
        print("《{}》主题已读取完...共有 {} 条新闻".format(label,len(files)))
    return txts,tips


if __name__ == '__main__':
    txts, tips=read(FILE_PATH)
    df=pd.DataFrame({'News':txts,'Tip':tips})
    df.to_csv(os.path.join(OUT_PATH,'NEWS.csv'),index=None)


"""
《体育》主题已读取完...共有 131604 条新闻
《娱乐》主题已读取完...共有 92632 条新闻
《家居》主题已读取完...共有 32586 条新闻
《彩票》主题已读取完...共有 7588 条新闻
《房产》主题已读取完...共有 20050 条新闻
《教育》主题已读取完...共有 41936 条新闻
《时尚》主题已读取完...共有 13368 条新闻
《时政》主题已读取完...共有 63086 条新闻
《星座》主题已读取完...共有 3578 条新闻
《游戏》主题已读取完...共有 24373 条新闻
《社会》主题已读取完...共有 50849 条新闻
《科技》主题已读取完...共有 162929 条新闻
《股票》主题已读取完...共有 154398 条新闻
《财经》主题已读取完...共有 37098 条新闻
"""