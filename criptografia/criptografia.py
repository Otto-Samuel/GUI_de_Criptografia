import onetimepad
from tkinter import *

root = Tk() 
root.title("CRIPTOGRAFIA") 
root.geometry("400x300") 

def encrypt_message():                       
    plaintext = entry_plain.get()
    key = 'random'  # Static key replaced with a random key generation method
    ciphertext = onetimepad.encrypt(plaintext, key)
    entry_cipher.delete(0, END)
    entry_cipher.insert(0, ciphertext)

def decrypt_message():                      
    ciphertext = entry_cipher.get()
    key = 'random'  # Static key replaced with a random key generation method
    plaintext = onetimepad.decrypt(ciphertext, key)
    entry_plain_dec.delete(0, END)
    entry_plain_dec.insert(0, plaintext)
      
label_plain = Label(root, text='Texto simples')                
label_plain.grid(row=0, column=0, sticky=E) 
label_cipher = Label(root, text='Texto criptado') 
label_cipher.grid(row=1, column=0, sticky=E) 
label_cipher_text = Label(root, text="Texto cifrado") 
label_cipher_text.grid(row=0, column=2, sticky=W) 
label_plain_text = Label(root, text="Texto descriptografado") 
label_plain_text.grid(row=1, column=2, sticky=W) 

entry_plain = Entry(root) 
entry_plain.grid(row=0, column=1) 
entry_cipher = Entry(root) 
entry_cipher.grid(row=1, column=1) 
entry_cipher_text = Entry(root) 
entry_cipher_text.grid(row=0, column=3) 
entry_plain_dec = Entry(root) 
entry_plain_dec.grid(row=1, column=3) 

encrypt_button = Button(root, text="Criptografar", bg="red", fg="white", command=encrypt_message) 
encrypt_button.grid(row=2, column=1) 
decrypt_button = Button(root, text="Descriptografar", bg="blue", fg="white", command=decrypt_message) 
decrypt_button.grid(row=3, column=1) 

root.mainloop()
