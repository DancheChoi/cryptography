from tkinter import messagebox, simpledialog, Tk
import random

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + ' '
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message) / 2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

def encrypt(message):
    swapped_message = swap_letters(message)
    encrypted_list = []
    fake_letters = ['a', 'c', 'e', 'g', 'i']
    for counter in range(0, len(message)):
        encrypted_list.append(swapped_message[counter])
        encrypted_list.append(random.choice(fake_letters))
    new_message = ''.join(encrypted_list)
    return new_message

def decrypt(message):
    unreversed_message = reversed(message)
    decryptedlayer1 = swap_letters(unreversed_message)
    even_letters = get_even_letters(decryptedlayer1)
    new_message = ''.join(even_letters)
    return new_message

def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt, decrypt or quit?')
    return task

def get_message(mode):
    if mode == 'encrypt':
        message = simpledialog.askstring('Message', 'Message:')
        return message
    if mode == 'decrypt':
        message = simpledialog.askstring('Message', 'Encrypted message:')
        return message

root = Tk()

while True:
    task = get_task()
    if task == 'encrypt':
        file = get_message('encrypt')
        encrypted = encrypt(file)
        messagebox.showinfo('Cipertext is :', encrypted)

    elif task == 'decrypt':
        message = get_message('decrypt')
        decrypted = decrypt(message)
        messagebox.showinfo('Plaintext is:', decrypted)

    elif task == 'quit':
        break
    
root.mainloop()
        
