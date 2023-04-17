# CSI-4480-Group-5-project

## Main GUI

## Create a Password

## Encryption

## Image Encryption

For the demo, this takes in the key 1234 to encrypt text into an image, and the key 678 to decrypt the image back into a text file.

Then it is an implementation of the text-to-image encryption algorithm described here: https://www.mdpi.com/2073-431X/11/3/39. 

The algorithm is modified to work with python and the Pillow library. 

Particularly noticible are that it was changed from CMYK values to RGBA values, as pillow plays nicer with the later.

Additionally, I believe I used a more brute-force method to assign character ascii values to image band layer pixels. 

I also needed to use PNG because .jpeg suppports CMYK but not RGBA, whereas .png supports RGBA and not CMYK.

Essentially, the algorithm takes in the text file "example.txt", converts each character to its ascii value, and assigns it to a pixel in one of the 4 RGBA layers of a newly created image. It then saves the image as "encryptedImage.png". 

If you wish to see the image you will really need to zoom in as the image files are very small unless you use a huge text file.

That's why the image shown is so blurry -- it's an extremely blown up image that only consists of a few pixels.

When the decryption algorithm is called, it reads in each band one after each other and converts each pixel value to the ascii assigned with each integer. 

If the integer is 3 (ASCII End of Text code), it does not write it to the new file. 

It then saves the new file as "decryptedText.txt"".

## RSA Encryption