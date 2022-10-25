from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['figure.figsize'] = [16.0, 8.0] # set default size of plots

# Load the image
A = imread('im.png')
X = np.mean(A, -1) # convert to grayscale

img = plt.imshow(256-X)
img.set_cmap('gray')
plt.axis('off')
# plt.show()

# Singular Value Decomposition
U, S, V = np.linalg.svd(X, full_matrices=False)
S = np.diag(S)

j = 0 
for r in (5, 20, 100):
    # Construct approximate image