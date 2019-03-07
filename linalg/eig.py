from scipy.linalg import eig
a=np.array([[1,2],[2,1]])
b=np.array([[1,3],[2,4]])
#广义特征分解y
#Ay=λDy
#特征分解的四种
#1.左特征分解2.右特征分解3.左广义特征分解3.右广义特征分解
a,b=eig(a,b,left=True,right=False)
print(a)#特征值
print(b)#特征向量
