import numpy as np


def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")

  calculations = {}
  array = np.array(list)
  matrix = array.reshape(3, 3)

  # calculate the mean
  mean_axis1 = matrix.mean(axis=0).tolist()
  mean_axis2 = matrix.mean(axis=1).tolist()
  mean_flattened = matrix.mean()

  # calculate the variance
  variance_axis1 = matrix.var(axis=0).tolist()
  variance_axis2 = matrix.var(axis=1).tolist()
  variance_flattened = matrix.var()

  # calculate the standard deviation
  std_axis1 = matrix.std(axis=0).tolist()
  std_axis2 = matrix.std(axis=1).tolist()
  std_flattened = matrix.std()

  # calculate the max
  max_axis1 = matrix.max(axis=0).tolist()
  max_axis2 = matrix.max(axis=1).tolist()
  max_flattened = matrix.max()

  # calculate the min
  min_axis1 = matrix.min(axis=0).tolist()
  min_axis2 = matrix.min(axis=1).tolist()
  min_flattened = matrix.min()

  # calculate the sum
  sum_axis1 = matrix.sum(axis=0).tolist()
  sum_axis2 = matrix.sum(axis=1).tolist()
  sum_flattened = matrix.sum()

  calculations = {
      'mean': [mean_axis1, mean_axis2, mean_flattened],
      'variance': [variance_axis1, variance_axis2, variance_flattened],
      'standard deviation': [std_axis1, std_axis2, std_flattened],
      'max': [max_axis1, max_axis2, max_flattened],
      'min': [min_axis1, min_axis2, min_flattened],
      'sum': [sum_axis1, sum_axis2, sum_flattened]
  }
  return calculations
