
# Impoting Numpy library
import numpy as np 

# Initialising arrays
x = np.array([[1,2,3],[3,2,1],[1,0,-1]])
y = np.array([[-4,-3,2],[1,2,1],[2,4,2]]) 

# Printing rank of x
print("rank of x: {}".format(np.linalg.matrix_rank(x)))

# Storing and Finding eigen vector and value of X Using eig function of Numpy
eigen_valuesX,eigen_vectorX= np.linalg.eig(x)

# Printing eigen value and vector of X
print("\nEIGEN VALUES OF X:\n{}".format(eigen_valuesX))
print("\nEIGEN VECTOR OF X:\n{}".format(eigen_vectorX))

# Printing rank of y
print("rank of y : {}".format(np.linalg.matrix_rank(y)))

# Storing and Finding eigen vector and value of Y Using eig function of Numpy
eigen_valuesY,eigen_vectorY= np.linalg.eig(y)

# Printing eigen value and vector of Y
print("\nEIGEN VALUES OF Y:\n{}".format(eigen_valuesY))
print("\nEIGEN VECTOR OF Y:\n{}".format(eigen_vectorY))

#*************** OUTPUT ************************# 
# rank of x: 2

# EIGEN VALUES OF X:
# [ 4.31662479e+00 -2.31662479e+00  1.93041509e-17]

# EIGEN VECTOR OF X:
# [[ 0.58428153  0.73595785  0.40824829]
#  [ 0.80407569 -0.38198836 -0.81649658]
#  [ 0.10989708 -0.55897311  0.40824829]]

# rank of y : 2

# EIGEN VALUES OF Y:
# [-4.12310563e+00  4.12310563e+00 -7.83686841e-16]

# EIGEN VECTOR OF Y:
# [[ 0.96413818 -0.05497126  0.66742381]
#  [-0.11869083 -0.44653738 -0.57207755]
#  [-0.23738167 -0.89307476  0.47673129]]
#*************** END OF OUTPUT ************************# 