import math
import numpy as np

# this file is testing how to store the cymk values properly in a way PIL will accept

cyan = np.full((500,500), 0)
magenta = np.full((500,500), 0)
yellow = np.full((500, 500),0)
key_color = np.full((500, 500),0)

cymk_colors = 


        #print & save image
                #how to create a cymk image: https://stackoverflow.com/questions/43817854/how-to-create-a-cmyk-image-in-python
                #from PIL import Image
                #im = Image.fromarray(A, mode="CMYK")
                #im.save("your_file.jpeg")



colorsArray = np.array(colorsList)               
file.close()
from PIL import Image
im = Image.fromarray(CYMK_values, mode="CMYK")
im.save("encryptedImage.jpeg")
