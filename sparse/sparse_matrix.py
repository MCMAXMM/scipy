import scipy.sparse as sp
#coo_matrix
row=[2,4,3,2]
col=[3,4,2,4]
data=[5,6,7,8]
c=sp.coo_matrix((data,(row,col)),shape=(5,6))
##dok_matrix
import numpy as np
from scipy.sparse import dok_matrix
S = dok_matrix((5, 5), dtype=np.float32)
for i in range(5):
    for j in range(5):
            S[i, j] = i + j
c=S.tocsr()

##lil_matrix
#lil采用两个list来存储，一个存储数据的列，一个存储数据，行通过第几个列表来判断
from scipy.sparse import lil_matrix
l = lil_matrix((6,5))
l[2,3] = 1
l[3,4] = 2
l[3,2] = 3
print(l.toarray())
print(l.data)
print(list(l.rows[3]))
####csr_matrix
from scipy.sparse import csr_matrix
indptr = np.array([0, 2, 3, 6])
indices = np.array([0, 2, 2, 0, 1, 2])#存储数据所在的列
data = np.array([1, 2, 3, 4, 5, 6])#存储数据
c=csr_matrix((data, indices, indptr), shape=(3, 3))
print(c.toarray())
print("indices",c.indices)
print("data",c.data)
print("indptr",c.indptr)#indptr主要是用来划分行的，存储的是indices第i到第j个元素是第一列的
#比如输出的indptr为[0,2,3,6]则第一行所在为indptr[0]:indptr=[0,1],是indeces中的0,1位置缩对应的元素
#简单来说,indptr其实存储的是列中第*到第#个元素是第多少行，其实就是行的划分
