from PIL import Image
import numpy as np
np.set_printoptions(threshold=np.inf)
path = r'Image vectorization\import_data\sign.jpg'
img = np.array(Image.open(path))
print(img)