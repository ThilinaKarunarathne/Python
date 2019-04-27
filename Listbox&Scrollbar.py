from tkinter import*

root = Tk()
root.title("Listbox & Scrollbar")

iList = Listbox(root, height = 18, width = 20, font = ('arial',20,'bold'), justify = CENTER, bg = "powder blue")
scroll = Scrollbar(root, command = iList.yview)

iList.configure(yscrollcommand = scroll.set)
iList.pack(side=LEFT)

scroll.pack(side = RIGHT, fill = Y)

#==============================================================================
for q in range(501):
                              # Algorithm
      iList.insert(END,q)
#==============================================================================

root.mainloop()
                   
