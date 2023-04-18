# CSI-4480-Group-5-project

## Main GUI

Created using Python module called TKinter. Allows us to use buttons, widgets, and a menu bar to navigate through the GUI and call functions. 
On the main screen, the top left is the "Options" dropdown which has the different things you can do with the GUI. "Generate Password" pulls up a new page for the random password generator. It only generates a random password if the text input is 12 or higher in terms of length of the password. "Image Encryption" pulls up the page for converting text file into an image. Only with the proper keys will the text file be converted to image during encryption and then converted back to original text during decryption. "RSA Encryption" is an implementation of RSA in Python. Hitting the exit button on the top right of the main page will kill the program, but on any other window it will just close the window.

## Create a Password

Random password will be at least 12 characters long. It will include uppercase letters, lowercase letters, digits, and symbols.

## Image Encryption

For the demo, this takes in the key 1234 to encrypt text into an image, and the key to decrypt the image back into a text file needs to match the generated password.

Then it is an implementation of the text-to-image encryption algorithm described here: https://www.mdpi.com/2073-431X/11/3/39. 

The algorithm is modified to work with python and the Pillow library. 

Particularly noticible are that it was changed from CMYK values to RGBA values, as pillow plays nicer with the later.

Additionally, I believe I used a more brute-force method to assign character ascii values to image band layer pixels. 

I also needed to use PNG because .jpeg suppports CMYK but not RGBA, whereas .png supports RGBA and not CMYK.

Essentially, the algorithm asks the user to select a text file. If they don't, it defaults to the text file "example.txt".

It converts each character to its ascii value, and assigns it to a pixel in one of the 4 RGBA layers of a newly created image. It then saves the image as "encryptedImage.png". 

If you wish to see the image you will really need to zoom in as the image files are very small unless you use a huge text file.

That's why the image shown is so blurry -- it's an extremely blown up image that only consists of a few pixels.

When the decryption algorithm is called, it asks where to save the decrypted output to. If no file is chosen, the default file is "decryptedText.txt"

Then it reads in the image file's bands one after each other and converts each pixel value to the ascii assigned with each integer. 

If the integer is 3 (ASCII End of Text code), it does not write it to the new file. 

Finally, it saves the file.

## RSA Encryption

Installed rsa in Python and used the module to implement the algorithm. The RSA module has newkeys() method which generates a public key and a private key used for 
encryption and decryption respectively. The input from the entry box is taken and encrypted using RSA's encrypt method in Pyhton. This method gets passed the encoded 
text and the public key. For decryption, the decrypt method gets passed the encrypted text and the private key, then decodes the result back to the original text. 
