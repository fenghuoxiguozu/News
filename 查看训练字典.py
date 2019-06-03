import numpy as np
data_dict=np.load(r'F:\keras\News\datasets\output\dict.npy',allow_pickle=True, encoding='latin1').tolist().items()
print(type(data_dict))
i=0
for key,value in data_dict:
    i+=1
    if i>19000 and i<23000 :
        print(key, " : ", value)
