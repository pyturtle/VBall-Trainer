import numpy as np

def compute_distance(landmark1, landmark2):
    return np.sqrt((landmark1.x-landmark2.x)**2 + (landmark1.y-landmark2.y)**2 + (landmark1.z - landmark2.z)**2)

