import math
import numpy as np
# ST = num characters in plaintext file
# EI size = width x length x # channels

numSquares = 4

# choose file & read it in (check to make sure it's the right type?)
with open("example.txt") as file:
    contents = file.read()
    #print(contents)
    file.close()

# size = Ceil(sqr(ST/4)) --> determines how big each square is based on how many at least are needed to fit the entire text file
    ST = len(contents)
    #print(ST)
    STsize = math.ceil(math.sqrt(ST/numSquares))
    #print(STsize)

red = np.full((STsize,STsize), 0)
green = np.full((STsize,STsize), 0)
blue = np.full((STsize, STsize),0)
transparency = np.full((STsize, STsize),3)

STsquare = STsize * STsize


#https://www.geeksforgeeks.org/python-convert-string-list-to-ascii-values/ --> convert chars to their ascii equivalents

i = 0
for z in range(numSquares): # z = 0 to 3
    for r in range(STsize): # r = 0 to STsize - 1
        for c in range(STsize): # c = 0 to STsize - 1
            if i < ST: # if there's still characters left to assign
                if z == 0:
                    red[r][c] = ord(contents[i])
                elif z == 1:
                    green[r][c] = ord(contents[i])
                elif z == 2:
                    blue[r][c] = ord(contents[i])
                elif z == 3:
                    transparency[r][c] = ord(contents[i])
                else:
                    print("Apologies, I was expecting more image layers than there are.")
                i += 1 # increment i


rgba_values = []#creates a new array
#adds each red, greeen, blue, transparency value to each pixel in the new array
for j in range(STsize):
    for k in range(STsize):
        rgba_values.append((red[j][k], green[j][k], blue[j][k], transparency[j][k]))
        #print("row: " + str(j) + " column: " + str(k) + " rgba: " + str(rgba_values[j][k]))



#worked when using Image.fromArray, but values didn't carry over correctly due to how PIL and NumPy have different dtypes
#colorsArray = np.array(rgba_values)               
#from PIL import Image
#im = Image.fromarray(colorsArray, mode="RGBA") 
#im.save("encryptedImage.png")

from PIL import Image
img = Image.new("RGBA", (STsize, STsize), color=3)#creates a new image with RGBA format, since PIL plays nicer with RBGA than with CYMK
img.putdata(rgba_values) #assigns each pixel color
img.save("encryptedImage.png") #saves the image

print("File successfully converted to image!")
#other sources used in this code = the pillow documentation at pillow.readthedocs.io/en/stable
