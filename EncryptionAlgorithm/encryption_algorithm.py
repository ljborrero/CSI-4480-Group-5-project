import math
import numpy as np
# ST = num characters in plaintext file
# EI size = width x length x # channels

numSquares = 4

# choose file & read it in (check to make sure it's the right type?)
with open("example.txt") as file:
    contents = file.read().lower()
    print(contents)
# change to all lowercase? .lower()^
# size = Ceil(sqr(ST/4))
    ST = len(contents)
    print(ST)
    STsize = math.ceil(math.sqrt(ST/numSquares))
    print(STsize)
# image type = CYMK mode

#colorsArray = np.full((STsize,STsize), )
#source array = (#images, #channels, x_dim, y_dim) #channels = 4 = RGBA/CYMK
# fills the array with just the color white

#no clue where I got this code from
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



red = np.full((STsize,STsize), 0)
green = np.full((STsize,STsize), 0)
blue = np.full((STsize, STsize),0)
transparency = np.full((STsize, STsize),0)

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




rgba_values = [[]*STsize]*STsize # creates a STsize x STsize array
i = 0
for j in range(STsize):
    for k in range (STsize):
        if i < len(rgba_values):
            rgba_values[j][k] = [red[i], green[i], blue[i], transparency[i]] # list assignment index out of range error here
            print("row: " + j + "column: " + k + "rgba: " + rgba_values[j][k] + "i: " + i)
            i = i + 1


        #print & save image
                #how to create a cymk image: https://stackoverflow.com/questions/43817854/how-to-create-a-cmyk-image-in-python
                #from PIL import Image
                #im = Image.fromarray(A, mode="CMYK")
                #im.save("your_file.jpeg")

colorsArray = np.array(colorsList)               
file.close()
from PIL import Image
im = Image.fromarray(rgba_values, mode="RGBA")
im.save("encryptedImage.jpeg")
