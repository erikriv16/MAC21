from tkinter import *
from datetime import datetime

'''''
def screen2CashSale():
    quit 
'''

BLUE = "#27374D"



class MAC21:
    def __init__(self):
        self.masterSC1 = Tk()
        self.masterSC1.title("MAC21")
        self.masterSC1.geometry()

        screen_width = self.masterSC1.winfo_screenwidth()
        screen_height = self.masterSC1.winfo_screenheight()

        self.masterSC1.geometry(f"{screen_width}x{screen_height}+0+0") #setting window full screen, 0+0 sets position to top-left corner
        self.masterSC1.config(bg=BLUE)


        #setting ratio of rows top, middle, and bottom to 10%, 80%, 10% respectively to keep proportions, set on master screen
        self.masterSC1.grid_columnconfigure(0, weight=1)
        self.masterSC1.grid_rowconfigure(0, weight=1)
        self.masterSC1.grid_rowconfigure(1, weight=8)
        self.masterSC1.grid_rowconfigure(2, weight=1)


        #Top Frame 
        topFrame = Frame(self.masterSC1, bg=BLUE)
        topFrame.grid(row=0, column=0, sticky='nswe')


        #configuring columns for top frame
        topFrame.columnconfigure(0, weight=1)
        topFrame.columnconfigure(1, weight=5)
        topFrame.columnconfigure(2, weight=3)
        topFrame.grid_rowconfigure(0, weight=5)
        topFrame.grid_rowconfigure(1, weight=5)

        #DATE LABEL
        currentDate = datetime.now().strftime("%B %d, %Y").upper() #gets current date on computer
        dateLabel = Label(topFrame, font=("Arial", 32), text=currentDate, bg=BLUE, fg="white")
        dateLabel.grid(row=0, column=0, sticky="nws")

        #PAGE LABEL
        pageLabel = Label(topFrame, font=("Arial", 32), text="ORDER ENTRY", bg=BLUE, fg="white")
        pageLabel.grid(row=0, column=1, sticky="nwes")

        #SCRN#LABEL
        screenNumLabel = Label(topFrame, font=("Arial", 32), text="SCRN - 1", bg=BLUE, fg="white")
        screenNumLabel.grid(row=0, column=2, sticky="nesw")

        #SALESCLERK#LABEL
        salesClerkNumberLabel = Label(topFrame,text="SALES CLERK# - [00000]", font=("Arial", 32), fg=BLUE, bg="white")
        salesClerkNumberLabel.grid(row=1, column=0, sticky="nws")

        #CLERK LABEL
        clerkLabel = Label(topFrame, text="ERIK R", font=("Arial", 32), fg=BLUE, bg="white")
        clerkLabel.grid(row=1, column=1, sticky="nesw")

        #FILLER LABEL to get that white background 
        fillerLabel = Label(topFrame, bg="white")
        fillerLabel.grid(row=1, column=2, sticky="nwes")





        #Middle Frame 
        middleFrame = Frame(self.masterSC1, bg="red")
        middleFrame.grid(row=1, column=0, sticky='nswe')

        #setting up middleFrame to be 2 pcs, left and right middle
        middleFrame.grid_columnconfigure(0, weight=5)
        middleFrame.grid_columnconfigure(1, weight=5)
        middleFrame.grid_rowconfigure(0, weight=1)

        #Left Middle Frame
        leftMiddleFrame = Frame(middleFrame, bg="purple")
        leftMiddleFrame.grid(row=0, column=0, sticky="nswe")
        leftMiddleFrame.columnconfigure(0, weight=1)     #setting leftMiddleFrame to stretch all the way on column/row
        leftMiddleFrame.rowconfigure(0,weight=1)         #done so transaction codes can be in the middle
        leftMiddleLabel = Label(leftMiddleFrame, font=("Arial", 32), text= " 01 = Cash Sale \n 02 = Named Cash Sale \n 07 = C.O.D Delivery \n 08 = Will Call Cash \n 09 = Will Call Charge \n 20 = Deposit Acc Sale \n 21 = Deposit Acc Payment \n 40 = Charge Acc Sale \n 46 = Charge Acc Payment", fg="white", bg="purple", justify="left")
        leftMiddleLabel.grid(row=0, column=0, sticky="nswe")   #grid at 0,0 b/c its lable is set inside leftMiddleFrame, and that frame was configured 2 lines above

        #Right Middle Frame
        rightMiddleFrame = Frame(middleFrame, bg="orange")
        rightMiddleFrame.grid(row="0", column="1", sticky="nswe")
        rightMiddleFrame.columnconfigure(0, weight=1)   #setting rightMiddleFrame to stretch all the way on column/row
        rightMiddleFrame.rowconfigure(0, weight=1)      #done so transaction codes can be in the middle
        rightMiddleLabel = Label(rightMiddleFrame, font=("Arial", 32), text= " 01 = Cash Sale \n 02 = Named Cash Sale \n 07 = C.O.D Delivery \n 08 = Will Call Cash \n 09 = Will Call Charge \n 20 = Deposit Acc Sale \n 21 = Deposit Acc Payment \n 40 = Charge Acc Sale \n 46 = Charge Acc Payment", fg="white", bg="orange", justify="left")
        rightMiddleLabel.grid(row=0, column=0, sticky="nwse")   #grid at 0,0 b/c its label is set inside rightMiddleFrame, and that frame was configured 2 lines above

        #Bottom Frame
        bottomFrame = Frame(self.masterSC1, bg="yellow")
        bottomFrame.grid(row=2, column=0, sticky='nswe')
        #Label(bottomFrame,text="BOTTOM FRAME", font=("Arial", 14), fg="white", bg="yellow").pack()

        bottomFrame.grid_columnconfigure(0, weight=1)
        bottomFrame.grid_rowconfigure(0, weight=5)
        bottomFrame.grid_rowconfigure(1, weight=5)

        bottomWhiteFrame = Frame(bottomFrame, bg="white")
        bottomWhiteFrame.grid(row=0, column=0, sticky="nwse")

        bottomStaticWhiteLabel = Label(bottomWhiteFrame, bg="white", fg=BLUE, text = "Enter Transaction Code - [", font=("Arial", 28))
        bottomStaticWhiteLabel.grid(row=0, column=0, sticky="w")

        def validateFnEntry(text):
            return len(text) <= 2
        
        #parameters required for trace_add method even though not used in this function
        def processUserInput(var, index, mode):
            text = entry_var.get()
            if len(text) == 2:
                if text == "01":
                    #clear text
                    pass
                    print("hello 01")
                elif text == "02":
                    #clear text
                    pass
                    print("hello 02")
                elif text == "07":
                    #clear text
                    pass
                    print("hello 07")
                elif text == "08":
                    #clear text     
                    pass
                    print("hello 08")
                elif text == "09":
                    #clear text
                    pass
                    print("hello 09")
                elif text == "20":
                    #clear text
                    pass
                    print("hello 20")
                elif text == "21":
                    #clear text
                    pass
                    print("hello 21")
                elif text == "40":
                    #clear text
                    pass
                    print("hello 40")
                elif text == "46":
                    #clear text
                    pass
                    print("hello 46")



        vcmd = bottomWhiteFrame.register(validateFnEntry)
        entryFunction = Entry(bottomWhiteFrame, font = ("Arial", 28), width=2, validate="key", validatecommand=(vcmd, "%P"), bg="white", fg=BLUE, bd=0, highlightthickness=0, insertbackground=BLUE)
        entryFunction.grid(row=0, column=1, sticky="w")
        #sets focus to entry widget without clicking on its
        entryFunction.focus_set()


        entry_var = StringVar()   #new instance of StringVar called entry_var, StringVar class used to manage value of a widget
        entryFunction.config(textvariable=entry_var)  #configures entry_var as text variable for entryFunction widget, any changes to entry widget text will be reflected in entry_var as well
        entry_var.trace_add("write", processUserInput) #trace_add used to trigger callback function whenever text in entry_var changes


        closingLabel = Label(bottomWhiteFrame, font=("Arial", 28), text="]", bg="white", fg=BLUE)
        closingLabel.grid(row=0, column=2, sticky="w")

        lowestLabel = Label(bottomFrame, bg=BLUE, fg="white", text="F3 = INQUIRY MENU               F6 = BRANCH INFO", font=("Arial", 28))
        lowestLabel.grid(row=1, column=0, sticky="nswe")



        

if __name__ == "__main__":
    app = MAC21()
    app.masterSC1.mainloop()