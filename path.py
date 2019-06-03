import os


path = os.path.dirname(os.path.abspath(__file__))  #F:\keras\News

FILE_PATH=r'F:\datas\THUCNews'

# 训练数据的路径
OUT_PATH = os.path.join(path, 'datasets','output')
INPUT_PATH = os.path.join(path, 'datasets','input')

STOPWORDS= os.path.join(INPUT_PATH, 'stopwords.txt')
# DICT=os.path.join(OUT_PATH,)