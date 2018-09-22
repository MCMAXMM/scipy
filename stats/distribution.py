from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
a=np.linspace(-1000,1000,10000)
b=norm.cdf(a,loc=0,scale=100)
plt.plot(b)
plt.show()
