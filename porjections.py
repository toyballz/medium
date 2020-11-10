# @ is explicit operator for the dot product

def proj_matrix(v):
  return v @ np.linalg.inv(v.T@v) @ v.T

def proj(vector, plane):
  return proj_matrix(vector) @ plane
