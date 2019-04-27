from tkinter import*
from datetime import datetime
import tkinter.messagebox

class CalDate:

      def __init__(self, root):

            self.root = root
            self.root.title("Date Calculator - (Thilina Karunarathne)")
            self.root.geometry("1350x750+0+0")
            self.root.configure(background="powder blue")

            MainFrame = Frame(self.root)
            MainFrame.grid()

            TopMain1 = Frame(MainFrame, bd=14, width=1850, height=750, pady=10, relief=RIDGE,
                             bg="cadet blue")
            TopMain1.grid(row=4, column=2)

            TopMain2 = Frame(TopMain1, bd=14, width=1300, height=700, pady=10, relief=RIDGE,
                             bg="cadet blue")
            TopMain2.grid(row=4, column=2)

            TopMain3 = Frame(TopMain2, bd=14, width=1250, height=650, pady=10, relief=RIDGE,
                             bg="cadet blue")
            TopMain3.grid(row=4, column=2)

            TopMain4 = Frame(TopMain3, bd=14, width=1200, height=600, pady=10, relief=RIDGE,
                             bg="cadet blue")
            TopMain4.grid(row=4, column=2)

            TopMain5 = Frame(TopMain4, bd=14, width=1150, height=550, pady=10, relief=RIDGE,
                             bg="cadet blue")
            TopMain5.grid(row=4, column=2)

            TopFrame = Frame(TopMain5, bd=14, width=1000, height=500, pady=10, relief=RIDGE,
                             bg="cadet blue")
            TopFrame.grid(row=4, column=2)

            def iExit ():
                  iExit = tkinter.messagebox.askyesnoesno ("Date Calculator", "Confirm if you want to exit")
                  if iExit > 0:
                        root.destroy()
                        return

            def iReset ():
                  CheckInDate.set("")
                  CheckOutDate.set("")
                  TotalDays.set("")



            def iDate ():
                  d1 = CheckInDate.get()
                  d2 = CheckOutDate.get()
                  d1 = datetime.strptime(d1, "%d/%m/%Y")
                  d2 = datetime.strptime(d2, "%d/%m/%Y")
                  TotalDays.set(abs((d2 - d1).days))

            CheckInDate=StringVar()
            CheckOutDate=StringVar()
            TotalDays=StringVar()
            
            #===============================================================================================================================

            self.lblTitle = Label(TopFrame,font=('arial', 40,'bold'), text="Date Calulator",padx=2,pady=2,bg="cadetBlue", fg="white")
            self.lblTitle.grid(row=0, column=0, columnspan=4)

            self.lblCheck_In_Date = Label(TopFrame,font=('arial', 24,'bold'), text="Check in Date:",padx=2,pady=2,bg="cadetBlue", fg="white")
            self.lblCheck_In_Date.grid(row=1,column=0, sticky=W)
            self.txtCheck_In_Date = Entry(TopFrame,font=('arial', 24,'bold'), textvariable=CheckInDate,bd=7, width=41)
            self.txtCheck_In_Date.grid(row=1, column=1, pady=4, padx=21, columnspan=3)


            self.lblCheck_Out_Date = Label(TopFrame,font=('arial', 24,'bold'), text="Check Out Date:",padx=2,pady=2,bg="cadetBlue", fg="white")
            self.lblCheck_Out_Date.grid(row=2,column=0, sticky=W)
            self.txtCheck_Out_Date = Entry(TopFrame,font=('arial', 24,'bold'), textvariable=CheckOutDate,bd=7, width=41)
            self.txtCheck_Out_Date.grid(row=2, column=1, pady=4, padx=21, columnspan=3)


            self.lblTotalCost = Label(TopFrame,font=('arial', 24,'bold'), text="Calculated Date:", padx=2,pady=2,bg="cadetBlue", fg="white")
            self.lblTotalCost.grid(row=3, column=0, sticky=W)
            self.txtTotalCost = Entry(TopFrame,font=('arial', 24,'bold'), textvariable=TotalDays,bd=7, width=41)
            self.txtTotalCost.grid(row=3, column=1, pady=9, padx=21, columnspan=3)

            #=================================================================================================================================

            self.btnTotal = Button(TopFrame,font=('arial', 24,'bold'),padx=16,pady=9,bg="powder blue", fg="black",
                                   width=10, height=1,text="Total", command = iDate).grid(row=5, column=1,padx=4)

            self.btnReset = Button(TopFrame,font=('arial', 24,'bold'),padx=16,pady=9,bg="powder blue", fg="black",
                                   width=10, height=1,text="Reset", command = iReset).grid(row=5, column=2,padx=5)

            self.btnExit = Button(TopFrame,font=('arial', 24,'bold'),padx=16,pady=9,bg="powder blue", fg="black",
                                   width=10, height=1,text="Exit", command = iExit).grid(row=5, column=3,padx=5)

            #==================================================================================================================================

            

            
if __name__=="__main__":
      root = Tk()
      application = CalDate (root)
      root.mainloop()
