from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
a=np.linspace(-1000,1000,10000)
b=norm.cdf(a,loc=0,scale=100)
plt.plot(b)
plt.show()
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
print(norm.a)#显示分布中随机变量的下界
print(norm.b)#显示分布中随机变量的下界
print(stats.beta.a,stats.beta.b)#另一个例子
#连续随机变量的主要公共方法如下：
#rvs:随机变量(相当于从这个分布中抽一些样本)
#pdf:概率密度函数
#cdf:累计分布函数
print(stats.norm.cdf(0))
#sf:残存函数(1-cdf)
#ppf:分位点函数(CDF的逆)
print(norm.ppf(0.5))#找到这个分布的中位数
#output:0
#isf:逆残余函数(sf的逆)
#stats:返回均值，方差，(费舍尔)偏态，(费舍尔)峰度
#moment:分布的非中心矩
print(stats.norm.stats())
#所有连续分布可以操纵loc以及scale参数调整分布的location和scale属性。
# 作为例子， 标准正态分布的location是均值而scale是标准差。
norm.stats(loc = 3, scale = 4, moments = "mv")
#(array(3.0), array(16.0))
