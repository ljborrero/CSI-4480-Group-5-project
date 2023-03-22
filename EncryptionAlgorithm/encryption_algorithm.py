import math
import numpy as np
# ST = num characters in plaintext file
# EI size = width x length x # channels

# choose file & read it in (check to make sure it's the right type?)
with open("example.txt") as file:
    contents = file.read().lower()
    print(contents)
# change to all lowercase? .lower()^
# size = Ceil(sqr(ST/4))
    ST = len(contents)
    print(ST)
    STsize = math.ceil(math.sqrt(ST/4))
    print(STsize)
# image type = CYMK mode

A = np.full((STsize,STsize), )
#for x in range(5):
    #A.append([[]])
#print(A)

# By default, four keys were used in this paper, each layer has its own key, 
    #and as previously mentioned, it is possible to use several keys according to the programmer's desire.
    #Each letter takes a color, in CMYK this is a 32 bit number of four possible colors with 256 levels each.
    #The first key is for Layer 1 (cyan), the second key is for Layer 2 (magenta),
    #the third key is for Layer 3 (yellow), and the fourth key is for Layer 4 (black). 
    #All keys are entered by the sender according to the language to be encrypted: 
    #English, Arabic, Hindi or any other language. This is one of the advantages of this work.
    #It is also possible to encrypt a text consisting of letters in various languages. 
    #In this work, four keys were used; each key was 37 characters long.

# if z = 1
        # key 1 is used
        # increase x until x = size
        # increase y until y = size
        # increase z  
    # if z = 2
        # key 2 is used
        # increase x until x = size
        # increse y until y = size
        # increase z
    # if z = 3
        # key 3 is used
        # increase x until x = size
        # increase y until y = size
        # increase z
    # if z = 4
        # key 4 is used
        # increase x until x = size
        # increase y until y = size
        # break
    # else
    

    #after the break:
        # if ST length != EI size
            # set threshold color
        #print & save image
                #how to create a cymk image: https://stackoverflow.com/questions/43817854/how-to-create-a-cmyk-image-in-python
                #from PIL import Image
                #im = Image.fromarray(A, mode="CMYK")
                #im.save("your_file.jpeg")
                
file.close()
from PIL import Image
im = Image.fromarray(A, mode="CMYK")
im.save("encryptedImage.jpeg")
