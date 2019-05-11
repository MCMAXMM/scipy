from scipy.sparse import csr_matrix, triu
A = csr_matrix([[1, 2, 0, 0, 3], [4, 5, 0, 6, 7], [0, 0, 8, 9, 0]],
               dtype='int32')
#scipy.sparse.triu(A, k=0, format=None)[source]
#Return the upper triangular portion of a matrix in sparse format

#Returns the elements on or above the k-th diagonal of the matrix A.
#k = 0 corresponds to the main diagonal
#k > 0 is above the main diagonal
#k < 0 is below the main diagonal



A.toarray()

triu(A).toarray()

triu(A).nnz

triu(A, k=1).toarray()

triu(A, k=-1).toarray()

triu(A, format='csc')
