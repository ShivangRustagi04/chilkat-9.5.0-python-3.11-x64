import tkinter as tk
from tkinter import filedialog

global fname

def UploadAction(event=None):
    fname = filedialog.askopenfilename()
    print('Selected:', fname)

def ConvertAction():
    print('Selected:')    

root = tk.Tk()
button1 = tk.Button(root, text='Open', command=UploadAction)
button2 = tk.Button(root, text='convert', command=ConvertAction)
button1.pack()
button2.pack()

root.mainloop()