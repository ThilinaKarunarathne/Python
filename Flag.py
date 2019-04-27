from tkinter import*

root = Tk()
root.geometry("1350x750+0+0")
root.resizable(1,1)
root.title("Flag (P.M.Thilina Pabasara Karunarathne)")


#=========================================================================================================
ora = Label(root, text="Orange", bg="orange", fg="black",width=31, height=9)
ora.grid(row=0,column=5)

ora = Label(root, text="Orange", bg="orange", fg="black",width=31, height=9)
ora.grid(row=1,column=5)

ora = Label(root, text="Orange", bg="orange", fg="black",width=31, height=9) # Oreange Column
ora.grid(row=2,column=5)

ora = Label(root, text="Orange", bg="orange", fg="black",width=31, height=9)
ora.grid(row=3,column=5)

ora = Label(root, text="Orange", bg="orange", fg="black",width=31, height=9)
ora.grid(row=4,column=5)

#===========================================================================================================

whit = Label(root, text="White", bg="white", fg="black",width=31, height=9)
whit.grid(row=0,column=4)

whit = Label(root, text="White", bg="white", fg="black",width=31, height=9)
whit.grid(row=1,column=4)

whit = Label(root, text="White", bg="white", fg="black",width=31, height=9)     # White Column
whit.grid(row=2,column=4)

whit = Label(root, text="White", bg="white", fg="black",width=31, height=9)
whit.grid(row=3,column=4)

whit = Label(root, text="White", bg="white", fg="black",width=31, height=9)
whit.grid(row=4,column=4)

#===========================================================================================================

red = Label(root, text="Red", bg="red", fg="black",width=31, height=9)
red.grid(row=0,column=3)

red = Label(root, text="Red", bg="red", fg="black",width=31, height=9)
red.grid(row=1,column=3)

red = Label(root, text="Red", bg="red", fg="black",width=31, height=9)
red.grid(row=2,column=3)

red = Label(root, text="Red", bg="red", fg="black",width=31, height=9)
red.grid(row=3,column=3)

red = Label(root, text="Red", bg="red", fg="black",width=31, height=9)
red.grid(row=4,column=3)

#===========================================================================================================

yell = Label(root, text="Yellow", bg="yellow", fg="black",width=31, height=9)
yell.grid(row=0,column=2)

yell = Label(root, text="Yellow", bg="yellow", fg="black",width=31, height=9)
yell.grid(row=1,column=2)

yell = Label(root, text="Yellow", bg="yellow", fg="black",width=31, height=9)
yell.grid(row=2,column=2)

yell = Label(root, text="Yellow", bg="yellow", fg="black",width=31, height=9)
yell.grid(row=3,column=2)

yell = Label(root, text="Yellow", bg="yellow", fg="black",width=31, height=9)
yell.grid(row=4,column=2)

#===========================================================================================================

blue = Label(root, text="Blue", bg="blue", fg="black", width=31, height=9)
blue.grid(row=0,column=1)

blue = Label(root, text="Blue", bg="blue", fg="black", width=31, height=9)
blue.grid(row=1,column=1)

blue = Label(root, text="Blue", bg="blue", fg="black", width=31, height=9)
blue.grid(row=2,column=1)

blue = Label(root, text="Blue", bg="blue", fg="black", width=31, height=9)
blue.grid(row=3,column=1)

blue = Label(root, text="Blue", bg="blue", fg="black", width=31, height=9)
blue.grid(row=4,column=1)

#============================================================================================================

blue = Label(root, text="Blue", bg="blue", fg="black", width=32, height=9)
blue.grid(row=0, column=6)

yell = Label(root, text="Yellow", bg="yellow", fg="black",width=32, height=9)
yell.grid(row=1,column=6)

red = Label(root, text="Red", bg="red", fg="black",width=32, height=9)
red.grid(row=2,column=6)

whit = Label(root, text="White", bg="white", fg="black",width=32, height=9)
whit.grid(row=3,column=6)

ora = Label(root, text="Orange", bg="orange", fg="black",width=32, height=9)
ora.grid(row=4,column=6)


root.mainloop()
