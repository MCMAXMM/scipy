import matplotlib.pyplot as plt
import numpy as np
def furliye(n,data):
    sum=0
    for i in range(1,n):
        sum=sum+(np.power(-1,i+1)/i)*np.sin(i*data)
    return 2*sum
def furli(n,data):
    sum=0
    for i in range(1,n,2):
        sum=sum+4/np.pi*(np.sin(np.pi*i*data))/i
    return sum
data=np.linspace(-np.pi,np.pi,2000)
y1=furli(30,data)
plt.plot(data,y1)
plt.show()
