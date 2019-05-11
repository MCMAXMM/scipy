from scipy.sparse import coo_matrix
coo_matrix((3, 4), dtype=np.int8).toarray()
# Constructing a matrix using ijv format
row  = np.array([0, 3, 1, 0])
col  = np.array([0, 3, 1, 2])
data = np.array([4, 5, 7, 9])
coo_matrix((data, (row, col)), shape=(4, 4)).toarray()
#其实就是用行坐标，列坐标，data，来存储稀疏数据
