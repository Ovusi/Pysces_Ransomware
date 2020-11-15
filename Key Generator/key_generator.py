#!/usr/bin/python3.8
import os
from cryptography.fernet import Fernet


def new_key():
    current_dir = os.getcwd()
    print("\nCurrent directory is " + current_dir)

    key = Fernet.generate_key()
    with open(input("\nEnter name of new encryption key: "), "wb") as key_file:
        key_file.write(key)
        print("Key created successfully. Please keep safely.")


def main():
    new_key()


if __name__ == '__main__':
    main()