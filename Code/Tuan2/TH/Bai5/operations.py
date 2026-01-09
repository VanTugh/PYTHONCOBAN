import math

def vec_add(v1, v2):
    return (v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2])

def vec_sub(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2])

def vec_length(v):
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def vec_invert(v):
    return (-v[0], -v[1], -v[2])