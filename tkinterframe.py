from tkinter import *
root=Tk()
frame=Frame(root)
frame.pack()
redbutton=Button(frame,text="Red", fg="Red")
redbutton.pack(side=LEFT)
greenbutton=Button(frame,text="Green", fg="Green")
greenbutton.pack(side=RIGHT)
root.mainloop()
