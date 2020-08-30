#python code to encrypt and decrypt
from tkinter import *

cipher = []
root = Tk()
entry = Entry(root)

def outputter(ciphertext):
	entry.insert(END, ciphertext)

def encrypt():
	entry.delete(0, END)
	plaintext = variable.get()
	key = variable2.get()
	plaintext = list(plaintext)
	alphabet = list('abcdefghijklmnopqrstuvwxyz')
	cipher = []
	for c in plaintext:
		if c in alphabet:
			new_pos = int(alphabet.index(c) + key)
			if new_pos > 25:
				new_pos = new_pos - 26			
			c_new = list('abcdefghijklmnopqrstuvwxyz').pop(new_pos)
			cipher.append(c_new)
			ciphertext = ''.join(cipher)
	outputter(ciphertext)

def decrypt():
	entry.delete(0, END)
	plaintext = variable.get()
	outputter(plaintext)


label = Label(root, text="Encyption algorithm")
label.pack()

variable = StringVar()
variable2 = IntVar()
plaintext = Entry(root, textvariable=variable)
key = Entry(root, textvariable=variable2)
 
label1 = Label(root, text="Enter Text (lowercase text): ")
label1.pack()
plaintext.pack(expand="30")

label2 = Label(root, text="Key Digit (0-37): ")
label2.pack()
key.pack(expand=30)

label3 = Label(root, text="Output: ")
label3.pack()
entry.pack(expand=30)

encryptbutton = Button(text="Encrypt", command=encrypt)
decryptbutton = Button(text="Decrypt", command=decrypt)
encryptbutton.pack()
decryptbutton.pack(expand="100")
root.mainloop()		
	


