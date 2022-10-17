# from re import X
import numpy as np
import tensorflow as tf



matrix = np.loadtxt('matrix.txt')
step = tf.train.matrix
row = len(matrix)
col = len(matrix)

print(col, row)
