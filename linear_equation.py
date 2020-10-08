# Solve the system of equations 2x + y + z = 4, x + 3y + 2z = 5, x = 6
# Importing necessary libraries
import numpy as np
from matplotlib import pyplot as plt

# Initialising arrays
q=np.array([[2,1,1],[1,3,2],[1,0,0]])
w=np.array([4,5,6])

# Using Numpys solve matrix function
x = np.linalg.solve(q, w)

print(x)

#*************** OUTPUT ************************# 
# [  6.  15. -23.]
#*************** END OF OUTPUT ************************# 