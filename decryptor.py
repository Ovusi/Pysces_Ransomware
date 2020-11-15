#!/usr/bin/python3.8
import getpass
import os
import tkinter
from tkinter import messagebox

from cryptography.fernet import Fernet

f_name = []
targets = '.crypy'


def find_file():
    print('Looking for files to decrypt......')
    usr = getpass.getuser()
    # Get files to encrypt from current user
    path = 'C:/Users/' + usr + '/'
    for r, d, files in os.walk(path):
        for file in files:
            if file.endswith(targets):
                f_name.append(os.path.join(r, file))
                print(f_name)
                break


def decrypt_file():
    key = "aWC5hXgG06c4lCmPpWxEuczPacxTa1TId-yw3hjZI9E="
    for fn in f_name:
        k = key
        f = Fernet(k)
        try:
            with open(fn, "rb") as file:
                file_data = file.read()
                decrypted_data = f.decrypt(file_data)
            with open(fn[:-6], "wb") as file:
                file.write(decrypted_data)
                print(file)
                os.remove(fn)
                print('Done Decrypting Your Files.........')
        except Exception as e:
            print(e)
            pass


def message():
    # this function prompts a window containing the ransom message
    window = tkinter.Tk()
    window.wm_withdraw()
    header = "HELLO... YOUR FILES HAVE BEEN DECRYPTED"
    body = "THANK YOU"
    messagebox.showinfo(title=header, message=body)


def main():
    find_file()
    decrypt_file()
    message()


if __name__ == '__main__':
    main()
