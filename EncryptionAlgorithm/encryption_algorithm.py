import math
import numpy as np
# ST = num characters in plaintext file
# EI size = width x length x # channels

numSquares = 4

# choose file & read it in (check to make sure it's the right type?)
with open("example.txt") as file:
    contents = file.read()#.lower()
    #print(contents)
    file.close()
# change to all lowercase? .lower()^
# size = Ceil(sqr(ST/4))
    ST = len(contents)
    #print(ST)
    STsize = math.ceil(math.sqrt(ST/numSquares))
    #print(STsize)

#source array = (#images, #channels, x_dim, y_dim) #channels = 4 = RGBA/CYMK

#from the research paper:"
# By default, four keys were used in this paper, each layer has its own key, 
    #and as previously mentioned, it is possible to use several keys according to the programmer's desire.
    #Each letter takes a color, in CMYK this is a 32 bit number of four possible colors with 256 levels each.
    #The first key is for Layer 1 (cyan), the second key is for Layer 2 (magenta),
    #the third key is for Layer 3 (yellow), and the fourth key is for Layer 4 (black). 
    #All keys are entered by the sender according to the language to be encrypted: 
    #English, Arabic, Hindi or any other language. This is one of the advantages of this work.
    #It is also possible to encrypt a text consisting of letters in various languages. 
    #In this work, four keys were used; each key was 37 characters long.
#"

#I chose not to implement the key part (which is what actually makes the encryption unique and therefore secure)


red = np.full((STsize,STsize), 0)
green = np.full((STsize,STsize), 0)
blue = np.full((STsize, STsize),0)
transparency = np.full((STsize, STsize),255)

STsquare = STsize * STsize


#https://www.geeksforgeeks.org/python-convert-string-list-to-ascii-values/ --> convert chars to their ascii equivalents

outOfChars = False
for z in range(numSquares): # z = 0 to 3
    for r in range(STsize): # r = 0 to STsize - 1
        for c in range(STsize): # c = 0 to STsize - 1
            currentIndex = (z * STsize ** z) + (r * STsize) + c # number ** exponent = n^e
            if currentIndex >= ST: outOfChars = True# if you've run out of characters in the input, just quit the loop since you can't access anything
            if z == 0 and  not outOfChars: # z = 0, working with cyan
                red[r][c] = ord(contents[currentIndex])
            elif z == 1 and not outOfChars:
                green[r][c] = ord(contents[currentIndex])
            elif z == 2 and not outOfChars:
                blue[r][c] = ord(contents[currentIndex])
            elif z == 3 and not outOfChars :
                transparency[r][c] = ord(contents[currentIndex])
            elif not outOfChars:
                print("Sorry, I expected more color layers than there were.") # ie z >= number of color layers (4 for cymk)



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
img = Image.new("RGBA", (STsize, STsize), color=0)#creates a new image with RGBA format, since PIL plays nicer with RBGA than with CYMK
img.putdata(rgba_values) #assigns each pixel color
img.save("encryptedImage.png") #saves the image

print("File successfully converted to image!")
#other sources used in this code = the pillow documentation at pillow.readthedocs.io/en/stable
