from cv2 import imread
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
path = r'Image vectorization\import_data\sign.jpg'
img = np.array(imread(path))
print(img)