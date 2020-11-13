import tkinter


def gui():
    window = tkinter.Tk()
    window.grid()
    window.title('You have been hacked')
    window.configure(background='black')

    # FIRST FRAME ########################################
    fullframe = tkinter.Frame(window)
    fullframe.grid(row=0, column=1, pady='0.05', padx='2')
    fullframe.configure(bg='red', borderwidth=1)

    tkinter.Label(fullframe,
                  text="""
YOU HAVE BEEN HACKED.
                         """,
                  fg='green',
                  bg='black',
                  padx='20',
                  font='hack',
                  pady='10',
                  height='1'
                  ).grid(ipadx='91', ipady='1', pady='1', padx='10', row=0, column=1)

    # SECOND FRAME ########################################
    frame = tkinter.Frame(window)
    frame.grid(row=0, column=1, pady='10')
    frame.configure(borderwidth=5, pady='2')

    tkinter.Label(fullframe,
                  text="""
Purchase Decryption key in Bitcoin.
WE HAVE COMPROMISED YOUR COMPUTER AND ENCRYPTED YOUR FILES.
                  """,
                  fg='green',
                  bg='black',
                  pady='20',
                  padx='60',
                  font=('hack', 8, 'bold'),
                  height='1'
                  ).grid(pady='1', row=2, column=1)

    # THIRD FRAME ########################################
    tframe = tkinter.Frame(window)
    tframe.grid(row=0, column=2, pady='10')
    tframe.configure(borderwidth=2, pady='2', bg='white')

    tkinter.Label(fullframe,
                  text="""
INFO
                  """,
                  fg='black',
                  bg='white',
                  pady='20',
                  padx='65',
                  font=('hack', 8, 'bold'),
                  height='1'
                  ).grid(padx='5', ipady='1', pady='2', row=0, column=3)

    window.mainloop()

gui()
