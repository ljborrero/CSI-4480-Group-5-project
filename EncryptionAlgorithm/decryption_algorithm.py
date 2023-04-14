import math
from PIL import Image

enIm = Image.open("encryptedImage.png", mode='r', formats=None)

red = list(enIm.getdata(band=0))
green = list(enIm.getdata(band=1))
blue = list(enIm.getdata(band=2))
transparency= list(enIm.getdata(band=3))

enIm.close()

txtfile = open("decryptedText.txt", "w") 
#create or overwrite the decryptedText.txt file 
#-> https://www.w3schools.com/python/python_file_write.asp
for r in red:
    txtfile.write(chr(r))
for g in green:
    txtfile.write(chr(g))
for b in blue:
    txtfile.write(chr(b))
for t in transparency:
    txtfile.write(chr(t))
# convert from int to ASCII: https://www.geeksforgeeks.org/python-ways-to-convert-list-of-ascii-value-to-string/?ref=lbp
txtfile.close()
#-------------------------------------------
