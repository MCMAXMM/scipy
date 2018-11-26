import numpy as np
from scipy.spatial.distance import pdist, cdist,squareform
y=np.array([[1,2],[2,3],[3,1]])
x = np.array([[0, 1], [1, 1], [2, 2]])
#cdist计算的是不同集合中点之间的距离，返回一个矩阵
print(cdist(x,y,"euclidean"))
#pdist计算的是同一个集合中各个点之间的距离，返回一个向量，但是不会计算自己和自己的距离，也不显示对称的距离
#pdist返回的是一个向量
print(pdist(x,'euclidean'))
#squareform将计算好的距离向量变成一个对称矩阵，主对角线都为0
d = squareform(pdist(x, 'euclidean'))
print(d)
