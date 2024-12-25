from tkinter import *
from datetime import datetime
import sqlite3


BLUE = "#27374D"
HIGHLIGHT_COLOR = "#4CAF50"

class OrderEntryHeader:
    def __init__(self):
        self.orderHeader = Tk()
        second_monitor_x_offset = 1920
        screen_width = self.orderHeader.winfo_screenwidth()
        screen_height = self.orderHeader.winfo_screenheight()
        self.orderHeader.geometry(f"{screen_width}x{screen_height}+{second_monitor_x_offset}+0") #setting window full screen, 0+0 sets position to top-left corner
        self.orderHeader.config(bg=BLUE)
        self.db_path = "/Users/erikrivera-sanchez/Documents/Python Related Projects/MAC21/dimensional_lumber.db"
        self.selectedRow = 0


    def configMaster(self):
        self.orderHeader.columnconfigure(0, weight=1)
        self.orderHeader.rowconfigure(0, weight=1)
        self.orderHeader.rowconfigure(1, weight=1)
        self.orderHeader.rowconfigure(2, weight=5)
        self.orderHeader.rowconfigure(3, weight=7)
        self.orderHeader.rowconfigure(4, weight=2)
        self.orderHeader.rowconfigure(5, weight=2)
        self.orderHeader.rowconfigure(6, weight=1)

        self.frame1 = Frame(self.orderHeader, bg=BLUE)
        self.frame2 = Frame(self.orderHeader, bg="white")
        self.frame3 = Frame(self.orderHeader, bg=BLUE)
        self.frame4 = Frame(self.frame3, bg=BLUE)
        self.frame5 = Frame(self.frame3, bg=BLUE)
        self.frame6 = Frame(self.orderHeader, bg=BLUE)
        self.frame7 = Frame(self.frame6, bg=BLUE)
        self.frame8 = Frame(self.frame6, bg=BLUE)
        self.frame9 = Frame(self.orderHeader, bg=BLUE)
        self.frame10 = Frame(self.frame9, bg=BLUE)
        self.frame11 = Frame(self.frame9, bg=BLUE)
        self.frame12 = Frame(self.orderHeader, bg=BLUE)
        self.frame13 = Frame(self.orderHeader, bg="white")

        self.frame1.grid(row=0, column=0, sticky="nswe")
        self.frame2.grid(row=1, column=0,sticky="nswe")
        self.frame3.grid(row=2, column=0, sticky="nswe")
        self.frame6.grid(row=3, column=0, sticky="nswe")
        self.frame9.grid(row=4, column=0, sticky="nswe")
        self.frame12.grid(row=5, column=0, sticky="nswe")
        self.frame13.grid(row=6, column=0, sticky="nswe")

    def configFrame1(self):
        self.frame1.rowconfigure(0, weight=1)
        ################TIME LABEL 
        currentDate = datetime.now().strftime("%B %d, %Y").upper() #gets current date on computer
        dateLabel = Label(self.frame1, font=("Arial", 25), text=currentDate, bg=BLUE, fg="white")
        dateLabel.grid(row=0, column=0, sticky="nwse", padx=0, pady=0)

        ###########UNDECIDED LABEL 
        nameLabel = Label(self.frame1, font=("Arial", 25), text="ORDER ENTRY HEADER", bg=BLUE, fg="white")
        nameLabel.grid(row=0, column=1, sticky="nswe", padx=300, pady=0)

        ######SCR LABEL 
        scrLabel = Label(self.frame1, font=("Arial", 25), text="SCNR-1.5", bg=BLUE, fg="white")
        scrLabel.grid(row=0, column=2, sticky="nswe", padx=0, pady=0)


    def configFrame2(self):
        self.frame2.rowconfigure(0, weight=1)

        clerk = Label(self.frame2, font=("Arial", 25), text="CLERK-[######] NAME", bg="white", fg=BLUE)
        orderNum = Label(self.frame2, font=("Arial", 25), text="11-ORDER#", bg="white", fg=BLUE)
        transcType = Label(self.frame2, font=("Arial", 25), text="TypeOfTransc", bg="white", fg=BLUE)

        clerk.grid(row=0, column=0, sticky="nswe", padx=(0, 750))
        orderNum.grid(row=0, column=1, sticky="nswe")
        transcType.grid(row=0, column=2, sticky="nswe")

    def configFrame3(self):
        self.frame3.columnconfigure(0, weight=5)
        self.frame3.columnconfigure(1, weight=5)

        self.frame4.config(bg="red")
        self.frame5.config(bg="green")

        self.frame4.grid(row=0, column=0, sticky="nswe")
        self.frame5.grid(row=0, column=1, sticky="nswe")

        self.frame4.rowconfigure(0, weight=1)
        self.frame4.rowconfigure(1, weight=1)
        self.frame4.rowconfigure(2, weight=1)
        self.frame4.rowconfigure(3, weight=1)
        self.frame4.rowconfigure(4, weight=1)

        billTo = Label(self.frame4, font=("Arial", 25), text="Bill to: 11-(Account#)", bg=BLUE, fg="white")
        phoneNum = Label(self.frame4, font=("Arial", 25), text="000-000-0000", bg=BLUE, fg="white")
        accountName = Label(self.frame4, font=("Arial", 25), text="ACCOUNT NAME", bg=BLUE, fg="white")
        accountAddress = Label(self.frame4, font=("Arial", 25), text="ACCOUNT ADDRESS", bg=BLUE, fg="white")
        accountCityState = Label(self.frame4, font=("Arial", 25), text="CITY, STATE", bg=BLUE, fg="white")
        accountZip = Label(self.frame4, font=("Arial", 25), text="ZIPCODE", bg=BLUE, fg="white")

        billTo.grid(row=0, column=0, sticky="nsw")
        phoneNum.grid(row=0, column=1, sticky="nse", padx=(250, 0))
        accountName.grid(row=1, column=0, sticky="nsw")
        accountAddress.grid(row=2, column=0, sticky="nsw")
        accountCityState.grid(row=4, column=0, sticky="nsw")
        accountZip.grid(row=4, column=1, sticky="nse")

        label01 = Label(self.frame5, font=("Arial", 25), text="01=[", bg=BLUE, fg="white")
        entry01 = Entry(self.frame5, font=("Arial", 25), bg=BLUE, fg="white")
        label01close = Label(self.frame5, font=("Arial", 25), text="]", bg=BLUE, fg="white")

        label02 = Label(self.frame5, font=("Arial", 25), text="02=[", bg=BLUE, fg="white")
        entry02 = Entry(self.frame5, font=("Arial", 25), bg=BLUE, fg="white")
        label02close = Label(self.frame5, font=("Arial", 25), text="]", bg=BLUE, fg="white")

        label03 = Label(self.frame5, font=("Arial", 25), text="03=[", bg=BLUE, fg="white")
        entry03 = Entry(self.frame5, font=("Arial", 25), bg=BLUE, fg="white")
        label03close = Label(self.frame5, font=("Arial", 25), text="]", bg=BLUE, fg="white")

        label04 = Label(self.frame5, font=("Arial", 25), text="04=[", bg=BLUE, fg="white")
        entry04 = Entry(self.frame5, font=("Arial", 25), bg=BLUE, fg="white")
        label04close = Label(self.frame5, font=("Arial", 25), text="]", bg=BLUE, fg="white")

        label05 = Label(self.frame5, font=("Arial", 25), text="05=[", bg=BLUE, fg="white")
        entry05 = Entry(self.frame5, font=("Arial", 25), width=30, bg=BLUE, fg="white")
        label05close = Label(self.frame5, font=("Arial", 25), text="]", bg=BLUE, fg="white")
        
        label05_01 = Label(self.frame5, font=("Arial", 25), text="[", bg=BLUE, fg="white")
        entry05_01 = Entry(self.frame5, font=("Arial", 25), width=2, bg=BLUE, fg="white")
        label05_01close = Label(self.frame5, font=("Arial", 25), text="]", bg=BLUE, fg="white")

        label05_02 = Label(self.frame5, font=("Arial", 25), text="[", bg=BLUE, fg="white")
        entry05_02 = Entry(self.frame5, font=("Arial", 25), width=11, bg=BLUE, fg="white")
        label05_02close = Label(self.frame5, font=("Arial", 25), text="]", bg=BLUE, fg="white")


        label01.grid(row=0, column=0, padx =(10,0), sticky="nsw")
        entry01.grid(row=0, column=1, columnspan=7, sticky="nswe")
        label01close.grid(row=0, column=8, sticky="nse")

        label02.grid(row=1, column=0, padx =(10,0), sticky="nsw")
        entry02.grid(row=1, column=1, columnspan=7, sticky="nswe")
        label02close.grid(row=1, column=8, sticky="nse")

        label03.grid(row=2, column=0, padx =(10,0), sticky="nsw")
        entry03.grid(row=2, column=1, columnspan=7, sticky="nswe")
        label03close.grid(row=2, column=8, sticky="nse")

        label04.grid(row=3, column=0, padx =(10,0), sticky="nsw")
        entry04.grid(row=3, column=1, columnspan=7, sticky="nswe")
        label04close.grid(row=3, column=8, sticky="nse")

        label05.grid(row=4, column=0, padx =(10,0), sticky="nsw")
        entry05.grid(row=4, column=1, sticky="nsew")
        label05close.grid(row=4, column=2, sticky="nse")
        label05_01.grid(row=4, column=3, sticky="nsw")
        entry05_01.grid(row=4, column=4, sticky="nswe")
        label05_01close.grid(row=4, column=5, sticky="nse")
        label05_02.grid(row=4, column=6, sticky="nsw")
        entry05_02.grid(row=4, column=7, sticky="nswe")
        label05_02close.grid(row=4, column=8, sticky="nse")




    def callAllFrames(self):
        self.configMaster()
        self.configFrame1()
        self.configFrame2()
        self.configFrame3()




if __name__ == "__main__":
    app = OrderEntryHeader()
    app.callAllFrames()
    app.orderHeader.mainloop()