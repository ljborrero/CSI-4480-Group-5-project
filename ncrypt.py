import tkinter as tk #for gui
from tkinter import * #for gui
from tkinter import messagebox #for messagebox
from tkinter.filedialog import askopenfile
import string #for password
import random #for password
import rsa #for encryption
import math #for image encryption
import numpy as np #for image encryption
from PIL import Image, ImageTk #for image encryption


pubKey, privKey = rsa.newkeys(1024)

encKey = '1234'
decKey = '56789'
def generatePassword():
    length = int(userEntry.get())
    password = []
    values = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    if length >= 12:
        for x in range(length):
            randomize = random.choice(values)
            password.append(randomize)
        generatedP = Toplevel(mainWindow)
        generatedP.geometry("400x200")
        generatedP.title("Your new Password is:")
        generatedP.config(bg = "black")
        text = Text(generatedP, height = 5, width = 35)
        text.pack(pady = 50)
        text.insert(END, "".join(password))
    else:
        #messagebox.showerror("Try Again", "Invalid length. A strong password should be at least 12 digits long.")
        messagebox.askokcancel("askokcancel", "want to continue?")
    #generatedP = Toplevel(mainWindow)
    #generatedP.geometry('400x400')
def passW():
    print("Password")
    passWindow = Toplevel(mainWindow)
    passWindow.geometry('400x400')
    passWindow.title('Password Creation')

    label = tk.Label(passWindow, text = "Specify the desired length of your password: ")
    label.pack()
    global userEntry
    userEntry = tk.Entry(passWindow, text = '', show = '*')
    userEntry.pack()
    button = tk.Button(passWindow, text = 'Generate Password', command = generatePassword)
    button.pack()

def encrypt():
    mess = userEntry2.get()
    global encMess
    encMess = rsa.encrypt(mess.encode(), pubKey)
    pop = Toplevel(mainWindow)
    pop.geometry('400x400')
    pop.title('Encrypted Text')
    text2 = Text(pop, height = 5, width = 35)
    text2.pack()
    text2.insert(END, encMess)
def decrypt():
    decMess = rsa.decrypt(encMess, privKey).decode()
    pop2 = Toplevel(mainWindow)
    pop2.geometry('400x400')
    pop2.title('Decrypted Text')
    text3 = Text(pop2, height = 5, width = 35)
    text3.pack()
    text3.insert(END, decMess)

def tEnc():
    if userEntryd.get() == encKey:
        print('Key Matches')
    else:
        print('Key for Encryption is Incorrect')
def tDec():
    if userEntryd.get() == decKey:
        print('Key for Decryption Matches')
    else:
        print('Decryption Key is Incorrect')

    
def fileText():
    print('Text')
    new = Toplevel(mainWindow)
    new.geometry('400x400')
    new.title('Text Encryption')
    new.config(bg = 'yellow')
    userEntryb = tk.Entry(new, text = '')
    userEntryb.grid(row = 0, column = 0, padx = 10)

    userEntryg = tk.Entry(new, text = '')
    userEntryg.grid(row = 0, column = 1)

    userEntryu = tk.Entry(new, text = '')
    userEntryu.grid(row = 0, column = 2)
    button4 = tk.Button(new, text = 'Encrypt', command = tEnc)
    button4.grid(row = 1, column = 0)
##    userEntryc = tk.Entry(new, text = '')
##    userEntryc.pack()
    button5 = tk.Button(new,text = 'Decrypt', command = tDec)
    button5.grid(row = 1, column = 1)
    global userEntryd
    userEntryd = tk.Entry(new, text = '', show = '*')
    userEntryd.grid(row = 2, column = 0)
    
    #labelt = tk.Label(new, text = 'Encryption Key')
    #labelt.pack()
    #userEntrye = tk.Entry(new, text = '')
    #userEntrye.pack()
    #labels = tk.Label(new, text = 'Decryption Key')
    #labels.pack()
def fileE():
    print('file encrypt')
    file = askopenfile(mode = 'r', filetypes = [('All Files', '*.*')])
    if file is not None:
        content = file.read()
        print(content)
    with open('decrypted.txt', 'w') as f:
        f.write(content)
        
    

def encryptImage():
    key = '1234'
    if ok.get() == key:
        # ST = num characters in plaintext file
         # EI size = width x length x # channels
                
        numSquares = 4# in case you want to change the format and thus need to change the number of channels in the image
                
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
                            labelS = tk.Label(imP, text = "Sorry, I expected more color layers than there were.")
                            labelS.pack()
                        i += 1 # increment i
                
                
        rgba_values = []#creates a new array
        #adds each red, greeen, blue, transparency value to each pixel in the new array
        for j in range(STsize):
            for k in range(STsize):
                rgba_values.append((red[j][k], green[j][k], blue[j][k], transparency[j][k]))
                #print("row: " + str(j) + " column: " + str(k) + " rgba: " + str(rgba_values[j][k]))
                
                
        from PIL import Image
        img = Image.new("RGBA", (STsize, STsize), color=3)#creates a new image with RGBA format, since PIL plays nicer with RBGA than with CYMK
        img.putdata(rgba_values) #assigns each pixel color
        img.save("encryptedImage.png") #saves the image
                
                        

        labelT = tk.Label(imP, text = "File successfully converted to image!")
        labelT.pack()
        encImg = Image.open("encryptedImage.png")
        encImg = encImg.resize((250, 250), Image.ANTIALIAS)
        encImg = ImageTk.PhotoImage(encImg)
        panel = Label(imP, image = encImg)
        panel.image = encImg
        panel.pack()
        #print("File successfully converted to image!")
        #other sources used in this code = the pillow documentation at pillow.readthedocs.io/en/stable
    else:
        lab = tk.Label(imP, text = 'Key does not match, Try Again')
        lab.pack()
def decryptImage():
    dKey = '678'
    if ok.get() == dKey:
    
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
        sLabel = tk.Label(imP, text = 'File Successfully Decrypted')
        sLabel.pack()
    else:
        nLabel = tk.Label(imP, text = 'Key for Decryption does not Match')
        nLabel.pack()
def imageE():
    print('image encrypt')
    global imP
    imP = Toplevel(mainWindow)
    imP.geometry('500x500')
    imP.title('Image Encryption')
    wow = tk.Label(imP, text = 'Enter the Key for Encryption')
    wow.pack()
    global ok
    ok = tk.Entry(imP, text = '', show = '*')
    ok.pack()
    button0 = tk.Button(imP, text = 'Encrypt', command = encryptImage)
    button0.pack()
    button9 = tk.Button(imP, text = 'Decrypt', command = decryptImage)
    button9.pack()




def rsaEncrypt():
    print('RSA Encrypt')
    textEncrypt = Toplevel(mainWindow)
    textEncrypt.geometry("400x150")
    textEncrypt.title("RSA Encryption")
    textEncrypt.config(bg = 'blue')
    global userEntry2
    userEntry2 = tk.Entry(textEncrypt, text = '')
    userEntry2.grid(row = 0, column = 0, padx = 50, pady =30)
    global userEntry3
    userEntry3 = tk.Entry(textEncrypt, text = '')
    userEntry3.grid(row = 0, column = 1)

    button2 = tk.Button(textEncrypt, text = 'Encrypt', command = encrypt)
    button2.grid(row = 1, column = 0)

    button3 = tk.Button(textEncrypt, text = 'Decrypt', command = decrypt)
    button3.grid(row = 1, column = 1)



mainWindow = tk.Tk()
mainWindow.geometry('500x300')
mainWindow.title('NCRYPT')
#mainWindow.config(bg = '#00ffff')
mainWindow.config(bg = '#08c5d1')
labely = tk.Label(mainWindow, text = "I am NCRYPT.", font = '25', justify = 'center')
labely.pack(pady = 15)
labelf = tk.Label(mainWindow, text = "I have a Random Password Generation Tool, \nalong with various Encryption/Decryption Methods", bg = '#ffbf66')
labelf.pack(pady = (0, 15))
labelx = tk.Label(mainWindow, text = "Click the Options Dropdown to Navigate Where You Want to Go.", bg = '#ffbf66', font = '18', justify = 'center', fg = '#d46f4d')
labelx.pack(pady = (0, 15))



menuDrop = Menu(mainWindow)
mainWindow.config(menu=menuDrop)
optionDrop = Menu(menuDrop, tearoff = 0)
menuDrop.add_cascade(label = 'Options', menu = optionDrop)
optionDrop.add_command(label = 'Create a Password', command = passW)
optionDrop.add_command(label = 'Encryption', command = fileText)
#optionDrop.add_command(label = 'File Encryption', command = fileE)
optionDrop.add_command(label = 'Image Encryption', command = imageE)
optionDrop.add_command(label = 'RSA Encryption', command = rsaEncrypt)

mainWindow.mainloop()











