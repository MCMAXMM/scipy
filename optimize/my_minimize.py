import numpy as np
from scipy.optimize import minimize
def fun(a,b,x):
    v=lambda x:(x-a)*(x-b)
    return v
#这里说明一下minimize中的参数的设置
#（1）func:要优化的函数需要返回一个scala
#（2）x0:变量的初始猜测值
#（3）methods:采用的优化的方法
#args : tuple, optional Extra arguments passed to the objective function and its derivatives (fun, jac and hess functions).

#jac:夹克比矩阵
#hess:海瑟矩阵，二阶导数
#contrains:等式约束或者不等式约束，eq:说明是等式约束，等于0，ineq:不等式约束，必须非负
#bounds:变量的限制范围
res=minimize(fun(4,1),np.array(2),method="SLSQP")
#minimize(中的第一个参数是一个函数)
print(res.fun)
print(res.success)
print(res.x)

#举一个有约束的优化问题
fun = lambda x: (x[0] - 1)**2 + (x[1] - 2.5)**2
#等式和不等式约束
cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
        {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
        {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})
#变量范围的限制
bnds = ((0, None), (0, None))
res = minimize(fun, (2, 0), method='SLSQP', bounds=bnds,constraints=cons)
print(res.success)#判断是否求解成功
print(res.fun)#输出求解后的函数值
print(res.x)#输出求解后的变量
