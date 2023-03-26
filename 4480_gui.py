import tkinter as tk

def encryptText():
    #encryptionAlgorithm goes here
    #button['text'] = 'Encrypted'
    #below is placeholder code to test that buttons work
    enteredText = userEntry.get()
    inputText = enteredText[::-1]
    textbox = tk.Message(text = 'Encrypted Text: ' + inputText, width = 200, font = '16')
    textbox.place(x = 155, y = 150)
    promptDecrypt(inputText)

def promptDecrypt(text):
    #creates Decrypt Label and Button
    #Decrypt Button calls decryptText function
    decryptLabel = tk.Label(text = 'Decrypt: ' + text) #creates label displaying what text to decrypt
    decryptLabel.place(x = 200, y = 175) #places label in window
    decryptButton = tk.Button(text = 'Decrypt', command = decryptText) #creates Button to call decryption function/algorithm
    decryptButton.place(x = 105, y = 215, width = 250, height = 35) #places Button in window

def decryptText():
    #decryptionAlgorithm goes here
    #below is placeholder code to test that buttons work
    userText = userEntry.get()
    reverseUT = userText[::-1]
    originalUT = reverseUT[::-1]
    
    decryptionMessage = tk.Message(text = 'Decrypted Text: ' + originalUT, width = 200, font = '16') #creates text to show user the decrypted text
    decryptionMessage.place(x = 145, y = 260) #places text in window


window = tk.Tk() #creates main window
window.geometry('500x500') #sizes window
window.title('Secret Messages') #title of the window

encryptPrompt = tk.Label(text = 'Enter Text You Wish to Encrypt:') #creates label to prompt user to enter text to encrypt
encryptPrompt.place(x = 150, y = 20, height = 25) #places label in window

userEntry = tk.Entry(text = '') #creates entry box for user to input text
userEntry.place(x = 180, y = 50, width = 110, height = 25) #places entry box in window

encryptButton = tk.Button(text = 'Encrypt', command = encryptText) #creates Button to call Encryption function/algorithm
encryptButton.place(x = 105, y = 100, width = 250,  height = 35) #places Button in window

stopButton = tk.Button(text = 'Stop', command = window.destroy) #creates Button to stop the program and close the window
stopButton.place(x = 40, y = 400, width = 400, height = 30) #palces the Stop Button in window

window.mainloop() #calls mainloop to create window
