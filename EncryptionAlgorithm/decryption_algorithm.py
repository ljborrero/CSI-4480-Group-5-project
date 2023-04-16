import math
from PIL import Image

enIm = Image.open("encryptedImage.png", mode='r', formats=None)

red = list(enIm.getdata(band=0))
green = list(enIm.getdata(band=1))
blue = list(enIm.getdata(band=2))
transparency= list(enIm.getdata(band=3))

enIm.close()

#create a new textfile and put the decrypted text in it
txtfile = open("decryptedText.txt", "w") 
#create or overwrite the decryptedText.txt file 
#-> https://www.w3schools.com/python/python_file_write.asp
for r in red:
    character = chr(r)
    if (character != 3): #if the character is not 3 (ASCII end of file)
        txtfile.write(character)
for g in green:
    character = chr(g)
    if (character != 3): #if the character is not 3 (ASCII end of file)
        txtfile.write(character)
for b in blue:
    character = chr(b)
    if (character != 3): #if the character is not 3 (ASCII end of file)
        txtfile.write(character)
for t in transparency:
    character = chr(t)
    if (character != 3): #if the character is not 3 (ASCII end of file)
        txtfile.write(character)
# convert from int to ASCII: https://www.geeksforgeeks.org/python-ways-to-convert-list-of-ascii-value-to-string/?ref=lbp
txtfile.close()
