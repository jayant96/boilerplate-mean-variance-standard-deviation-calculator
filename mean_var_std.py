import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  arr = np.array(list)
  arr_matrix = arr.reshape((3,3))
  calculations = {
  'mean': [np.mean(arr_matrix, axis = 0).tolist(),np.mean(arr_matrix, axis = 1).tolist(),np.mean(arr_matrix).tolist()],
  'variance': [np.var(arr_matrix, axis=0).tolist(),np.var(arr_matrix, axis=1).tolist(),np.var(arr_matrix).tolist()],
  'standard deviation': [np.std(arr_matrix, axis=0).tolist(),np.std(arr_matrix, axis=1).tolist(),np.std(arr_matrix).tolist()],
  'max': [np.max(arr_matrix, axis=0).tolist(),np.max(arr_matrix, axis=1).tolist(),np.max(arr_matrix).tolist()],
  'min': [np.min(arr_matrix, axis=0).tolist(),np.min(arr_matrix, axis=1).tolist(),np.min(arr_matrix).tolist()],
  'sum': [np.sum(arr_matrix, axis=0).tolist(),np.sum(arr_matrix, axis=1).tolist(),np.sum(arr_matrix).tolist()]
  }
  return calculations
