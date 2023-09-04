import numpy as np
H1 = np.array([ 0.24, 0.2, 0.16, 0.12, 0.08, 0.04, 0.12, 0.04])
H2 = np.array([ 0.22, 0.23, 0.16, 0.13, 0.11, 0.08, 0.05, 0.02])

# KL Distance

kl_dist = np.sum(H1 * np.log(H1 / H2))
print("KL Dist :",kl_dist)

# Bhatacharyas Distance

bc_dist = -np.log(np.sum(np.sqrt(H1 * H2)))
print("Bhattacharya's Dist :",bc_dist)
