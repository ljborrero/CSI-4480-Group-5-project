import tkinter as tk #for gui
from tkinter import * #for gui
from tkinter import messagebox #for messageboxes
from tkinter.filedialog import askopenfile #for tkinter open file
from tkinter import filedialog as fd # for image encryption
import string #for password
import random #for password
import rsa #for encryption
import math #for image encryption
import numpy as np #for image encryption
from PIL import Image, ImageTk #for image encryption


pubKey, privKey = rsa.newkeys(1024) #keys for RSA algorithm, declaring them here

def generatePassword():
    length = int(userEntry.get())
    global password
    password = []
    values = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    if length >= 12:
        for x in range(length):
            randomize = random.choice(values)
            password.append(randomize)
        generatedP = Toplevel(mainWindow)
        generatedP.geometry("400x200")
        generatedP.title("Your New Password is:")
        generatedP.config(bg = "black")
        text = Text(generatedP, height = 5, width = 35)
        text.pack(pady = 50)
        text.insert(END, "".join(password))
    else:
        messagebox.showerror("Try Again", "Invalid Length. A Strong Password Should Be at Least 12 Digits Long.")
    
def passW():
    passWindow = Toplevel(mainWindow)
    passWindow.geometry("400x400")
    passWindow.title("Random Password Generation")
    passWindow.config(bg = "#00353f")

    label = tk.Label(passWindow, text = "Specify the desired \nlength of your password: ", font = ("Times", 20), bg = "#d46f4d")
    label.pack(pady = 15)
    global userEntry
    userEntry = tk.Entry(passWindow, text = "", show = "*", font = ("Times", 15))
    userEntry.pack(pady = (0, 15))
    button = tk.Button(passWindow, text = "Generate Password", font = ("Times", 15), command = generatePassword)
    button.pack(pady = (0, 15))
def uploadFile():
    fileName = fd.askopenfilename(title='Open an unencrypted text file:', initialdir='/', filetypes=[('text files', '*.txt')])

        #https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/
    if fileName is not None and fileName != '': #if the user selects a file to read in
        with open(fileName) as inputfile: #open the file
            txtfile = open("unencryptedText.txt", "w") #open the unencryptedText.txt input file
            txtfile.write(inputfile.read()) #write the contents of that file to the input file
            txtfile.close() # close the input file
            inputfile.close()#close the user-selected file
            
def encryptImage():
    key = '1234'
    if imgKey.get() == key:
        
        # ST = num characters in plaintext file
        # EI size = width x length x # channels

        numSquares = 4

        # choose file & read it in (check to make sure it"s the right type?)
        uploadFile() # see if the user wants to upload their own file

        with open("unencryptedText.txt") as file:
            contents = file.read()
                    #print(contents)
            file.close()
                
            # size = Ceil(sqr(ST/4)) --> determines how big each square is based on how many at least are needed to fit the entire text file
            ST = len(contents)
            #print(ST)
            STsize = math.ceil(math.sqrt(ST/numSquares))
             #print(STsize)



        
##        with open("example.txt") as file:
##            contents = file.read()#.lower()
##            #print(contents)
##            file.close()
##        # change to all lowercase? .lower()^
##        # size = Ceil(sqr(ST/4))
##            ST = len(contents)
##            #print(ST)
##            STsize = math.ceil(math.sqrt(ST/numSquares))
##            #print(STsize)

        #source array = (#images, #channels, x_dim, y_dim) #channels = 4 = RGBA/CYMK

        #from the research paper:"
        # By default, four keys were used in this paper, each layer has its own key, 
            #and as previously mentioned, it is possible to use several keys according to the programmer"s desire.
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
        transparency = np.full((STsize, STsize),3)

        STsquare = STsize * STsize


        #https://www.geeksforgeeks.org/python-convert-string-list-to-ascii-values/ --> convert chars to their ascii equivalents

        i = 0
        for z in range(numSquares): # z = 0 to 3
            for r in range(STsize): # r = 0 to STsize - 1
                for c in range(STsize): # c = 0 to STsize - 1
                    if i < ST: # if there"s still characters left to assign
                        if z == 0:
                            red[r][c] = ord(contents[i])
                        elif z == 1:
                            green[r][c] = ord(contents[i])
                        elif z == 2:
                            blue[r][c] = ord(contents[i])
                        elif z == 3:
                            transparency[r][c] = ord(contents[i])
                        else:
                            labelS = tk.Label(imP, text = "Sorry, I expected more color layers than there were.")
                            labelS.pack()
                        i += 1
                        #print("Sorry, I expected more color layers than there were.") # ie z >= number of color layers (4 for cymk)


        rgba_values = []#creates a new array
        #adds each red, greeen, blue, transparency value to each pixel in the new array
        for j in range(STsize):
            for k in range(STsize):
                rgba_values.append((red[j][k], green[j][k], blue[j][k], transparency[j][k]))
                #print(rgba_values)
                #print("row: " + str(j) + " column: " + str(k) + " rgba: " + str(rgba_values[j][k]))

        #worked when using Image.fromArray, but values didn"t carry over correctly due to how PIL and NumPy have different dtypes
        #colorsArray = np.array(rgba_values)               
        #from PIL import Image
        #im = Image.fromarray(colorsArray, mode="RGBA") 
        #im.save("encryptedImage.png")


        img = Image.new("RGBA", (STsize, STsize), color=3)#creates a new image with RGBA format, since PIL plays nicer with RBGA than with CYMK
        img.putdata(rgba_values) #assigns each pixel color
        img.save("encryptedImage.png") #saves the image
        messagebox.showinfo("Successful Encryptions", "File was Encrypted to an Image!")
        encImg = Image.open("encryptedImage.png")
        #encImg = encImg.resize((250, 250), Image.ANTIALIAS)
        #encImg = encImg.resize((250,250),resample=Image.NEAREST)
        encImg = encImg.resize((275, 275))
        encImg = ImageTk.PhotoImage(encImg)
        panel = Label(imP, image = encImg)
        panel.image = encImg
        panel.pack()
        #print("File successfully converted to image!")
        #other sources used in this code = the pillow documentation at pillow.readthedocs.io/en/stable
    else:
        messagebox.showerror("Try Again", "Key for Encryption Does Not Match")
def decryptImage():
    dKey = "".join(password)
    if imgKey.get() == dKey:
    
        enIm = Image.open("encryptedImage.png", mode="r", formats=None)

        red = list(enIm.getdata(band=0))
        green = list(enIm.getdata(band=1))
        blue = list(enIm.getdata(band=2))
        transparency= list(enIm.getdata(band=3))

        enIm.close()

        #create a new textfile and put the decrypted text in it
        txtfile = fd.asksaveasfile(defaultextension=".txt") # ask the user where to save the output file
        if txtfile is None: # if they don't choose, output it to the local file "decryptedText.txt"
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
        #-------------------------------------------
        messagebox.showinfo("Successful Decryption", "Image was Decrypted back to Plaintext")
    else:
        messagebox.showerror("Try Again", "Key for Decryption Does Not Match")
def imageE():
    global imP
    imP = Toplevel(mainWindow)
    imP.geometry("500x550")
    imP.title("Image Encryption")
    imP.config(bg = "#eff1e4")
    label2 = tk.Label(imP, text = "Enter the Key for Encryption", font = ("Times", 20), bg = "#eff1e4")
    label2.pack(pady = 15)
    global imgKey
    imgKey = tk.Entry(imP, text = "", show = "*", font = ("Times", 15))
    imgKey.pack(pady = (0, 15))
    button0 = tk.Button(imP, text = "Encrypt", font = ("Times", 15), command = encryptImage)
    button0.pack(pady = (0, 15))
    button9 = tk.Button(imP, text = "Decrypt", font = ("Times", 15), command = decryptImage)
    button9.pack(pady = (0, 15))

def rsa_encrypt():
    mess = rsaEntry1.get()
    global encMess
    encMess = rsa.encrypt(mess.encode(), pubKey)
    pop = Toplevel(mainWindow)
    pop.geometry("400x225")
    pop.title("Encrypted Text")
    pop.config(bg = "#0D0208")
    text2 = Text(pop, height = 5, width = 35, font = ("Times", 15))
    text2.pack(pady = 40)
    text2.insert(END, encMess)
def rsa_decrypt():
    decMess = rsa.decrypt(encMess, privKey).decode()
    pop2 = Toplevel(mainWindow)
    pop2.geometry("400x225")
    pop2.title("Decrypted Text")
    pop2.config(bg = "#00FF41")
    text3 = Text(pop2, height = 5, width = 35, font = ("Times", 15))
    text3.pack(pady = 40)
    text3.insert(END, decMess)


def rsaEncrypt():
    rsaPage = Toplevel(mainWindow)
    rsaPage.geometry("725x200")
    rsaPage.title("RSA Encryption")
    rsaPage.config(bg = "#d46f4d")
    global rsaEntry1
    rsaEntry1 = tk.Entry(rsaPage, text = "", font = ("Times", 20))
    rsaEntry1.grid(row = 0, column = 0, padx = 50, pady =30)
    global rsaEntry2
    rsaEntry2 = tk.Entry(rsaPage, text = "", font = ("Times", 20))
    rsaEntry2.grid(row = 0, column = 1)

    button2 = tk.Button(rsaPage, text = "Encrypt", font = ("Times", 15), command = rsa_encrypt)
    button2.grid(row = 1, column = 0)

    button3 = tk.Button(rsaPage, text = "Decrypt", font = ("Times", 15), command = rsa_decrypt)
    button3.grid(row = 1, column = 1)



mainWindow = tk.Tk()
mainWindow.geometry("500x300")
mainWindow.title("NCRYPT")

mainWindow.config(bg = "#08c5d1")
labely = tk.Label(mainWindow, text = "I am NCRYPT.", font = ("Times", 40), justify = "center", bg = "#ffbf66")
labely.pack(pady = 15)
labelf = tk.Label(mainWindow, text = "I have a Random Password Generation Tool, \nalong with various Encryption/Decryption Methods", font = ("Times", 15), bg = "#ffbf66")
labelf.pack(pady = (0, 15))
labelx = tk.Label(mainWindow, text = "Click the Options Dropdown \nto Navigate Where You Want to Go.", bg = "#ffbf66", font = ("Times", 15), justify = "center")
labelx.pack(pady = (0, 15))



menuDrop = Menu(mainWindow)
mainWindow.config(menu=menuDrop)
optionDrop = Menu(menuDrop, tearoff = 0)
menuDrop.add_cascade(label = "Options", menu = optionDrop)
optionDrop.add_command(label = "Generate Password", command = passW)
optionDrop.add_command(label = "Image Encryption", command = imageE)
optionDrop.add_command(label = "RSA Encryption", command = rsaEncrypt)

mainWindow.mainloop()
