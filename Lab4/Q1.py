import numpy as np
Mat_T = np.array([[.5, .5, -.5, -.25, -.25]], dtype= float)
Mat = Mat_T.T

# print(Mat)

A = np.array([[1, .135, .195, .137, .157],
              [.135, 1, .2, .309, .143],
              [.195,.2, 1, .157, .122],
              [.137, .309, .157, 1, .195],
              [.157, .143, .122, .195, 1]])

# print(A)

A_inv = np.linalg.inv(A)

Pro = Mat_T.dot(A_inv.dot(Mat))
print(Pro)
# print(Pro.shape)

Qurdratic_dist = np.sqrt(Pro)
print("Quadratic Distance is :",Qurdratic_dist)