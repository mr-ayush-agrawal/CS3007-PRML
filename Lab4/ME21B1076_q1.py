import numpy as np
import pandas as pd

def quadratic_form_distance(x,y,a):
    var1 = np.dot(np.dot(x, a), y)
    distance = np.sqrt(var1)
    return distance

hq_minus_htT = np.array([0.5, 0.5, -0.5, -0.25, -0.25] )
hq_minus_ht = np.array([[0.5], [0.5], [-0.5], [-0.25], [-0.25]])
A = np.array([[1,0.135,0.195,0.137,0.157],
              [0.135,1,0.2,0.309,0.143],
              [0.195,0.2,1,0.157,0.122],
              [0.137,0.309,0.157,1,0.195],
              [0.157,0.143,0.122,0.195,1]])


# Calculate quadratic form distance
distance = quadratic_form_distance(hq_minus_htT, hq_minus_ht, A)
print(distance)