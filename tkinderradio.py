from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Registration Form")
H1=Label(root,text="REGISTRATION FORM",fg="black",font=("Helvetica bold",20))
L1=Label(root,text="Your Name")
L2=Label(root,text="Email")
L3=Label(root,text="Gender")
L4=Label(root,text="Age")

Name=Entry()
Email=Entry()
Age=Entry()

R1=Radiobutton(root,text="Male")
R2=Radiobutton(root,text="Female")

Name.place(x=120,y=120)
Email.place(x=120,y=150)
Age.place(x=120,y=210)

H1.place(x=100,y=70)
L1.place(x=55,y=120)
L2.place(x=55,y=150)
L3.place(x=55,y=180)
L4.place(x=55,y=200)

R1.place(x=110,y=180)
R2.place(x=165,y=180)
root.mainloop();
