import scipy.io as sio
#使用scipy读取mat格式的文件
data = sio.loadmat('train_data.mat');
data = data['data']
