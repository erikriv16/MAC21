from tkinter import *
from datetime import datetime
import sqlite3

'''''
def screen2CashSale():
    quit 
'''

BLUE = "#27374D"



        

class CASHSALE:
    def __init__(self):
        self.masterSC2 = Tk()
        self.masterSC2.title("CASHSALE")
        self.masterSC2.geometry()
        self.itemList = []
        self.itemCount = 0
        self.escapePress = False
        screen_width = self.masterSC2.winfo_screenwidth()
        screen_height = self.masterSC2.winfo_screenheight()
        self.masterSC2.geometry(f"{screen_width}x{screen_height}+0+0") #setting window full screen, 0+0 sets position to top-left corner
        self.masterSC2.config(bg=BLUE)
        self.newLabel1 = None
        self.newEntry1 = None



        #same as validateFnEntry on ScreenFunctions.py
    def validateLineEntry(self, text):
        return len(text) <= 2


    #when calling fn from button press, event parameter is needed
    def lineNumEnter(self, event):
        text = self.optionEntry.get()
        print("YAY, we entered", text)
        text = int(text)
        self.escapePress = False
        self.newLabel1 = None
        self.newEntry1 = None
        self.toggleNewLabel()

    def escPressed(self, event):
        self.escapePress = True
        self.toggleNewLabel()

    def toggleNewLabel(self):
        if not self.escapePress:
            if self.newLabel1 is None:
                self.newLabel1 = Label(self.frame3, fg=BLUE, bg="white", text="01", font=("Arial", 25))
                self.newLabel1.grid(row=1, column=0, sticky="nwse")

                self.newEntry1 = Entry(self.frame3, fg="white", bg=BLUE, text="Entry:a;sjndf", font=("Arial", 25), bd=0, highlightthickness=0, insertbackground="white")
                self.newEntry1.grid(row=1, column=1, sticky="nswe")
                self.newEntry1.bind("<Escape>", self.escPressed)

                self.newEntry1.focus()

                descpEntryVar = StringVar()
                self.newEntry1.config(textvariable=descpEntryVar)
                self.newEntry1.bind("<Return>", lambda event: self.handleSearchBySkew(descpEntryVar.get(), "transcMenu"))

        else:
            if self.newLabel1 is not None:
                self.newLabel1.destroy()
                self.newEntry1.destroy()
                self.newLabel1 = None
                self.optionEntry.focus()


    
    #event is skew, function only activates if ENTER is pressed on newEntry1
    def searchItemBySkew(self, skew):
        conn = sqlite3.connect("dimensional_lumber.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dimensional_lumber WHERE skew = ?", (skew))

        #getting the result
        row = cursor.fetchall()

        conn.close()

        if row:
            return row
        else:
            return None



    def handleSearchBySkew(self, skew, typeOfSearch):
        item = self.searchItemBySkew(skew)
        if item and (typeOfSearch == "transcMenu"): 
            item_id, name, price, skew, quantity, category, subcategory, alpha, yardItem = item

            item = Item(name, price, skew, quantity, category, subcategory, alpha, yardItem)
            self.addToItemList(item)

            

    def addToItemList(self, item):
        self.itemList[self.itemCount + 1] = item
        self.itemCount = self.itemCount + 1








    def masterConfig(self):
        self.masterSC2.columnconfigure(0, weight=1)
        self.masterSC2.rowconfigure(0, weight=1)
        self.masterSC2.rowconfigure(1, weight=1)
        self.masterSC2.rowconfigure(2, weight=12)
        self.masterSC2.rowconfigure(3, weight=3)
        self.masterSC2.rowconfigure(4, weight=1)
    
    def frame1Config(self):
        frame1 = Frame(self.masterSC2, bg=BLUE)
        frame1.grid(row=0, column=0, sticky="nwse")

        ##FRAME1 LABELS
        frame1.rowconfigure(0, weight=1)

        clerkLabel = Label(frame1, fg="white", bg=BLUE, text="CLERK-00000", font=("Arial", 25))
        clerkLabel.grid(row=0, column=0, sticky="nsw", padx=(0, 30))

        scrnLabel = Label(frame1, fg="white", bg=BLUE, text="SCRN-2", font=("Arial", 25))
        scrnLabel.grid(row=0, column=1, sticky="nsw", padx=(150, 150))

        transcName = Label(frame1, fg="white", bg=BLUE, text="CASH SALE", font=("Arial", 25))
        transcName.grid(row=0, column=2, padx=(60, 0))

        orderNumber = Label(frame1, fg="white", bg=BLUE, text="ORDER: ######", font=("Arial", 25))
        orderNumber.grid(row=0, column=3)

    def frame2Config(self):
        frame2 = Frame(self.masterSC2, bg=BLUE)
        frame2.grid(row=1, column=0, sticky="nwse")
        ##FRAME2 LABELS 
        frame2.rowconfigure(0, weight=1)

        accountNumberLabel =  Label(frame2, fg="white", bg=BLUE, text="#########", font=("Arial", 25))
        accountNumberLabel.grid(row=0, column=0, sticky="nse")

        accountNameLabel =  Label(frame2, fg="white", bg=BLUE, text="ACCOUNTNAME", font=("Arial", 25))
        accountNameLabel.grid(row=0, column=1)

    def frame3Config(self):
        self.frame3 = Frame(self.masterSC2, bg=BLUE)
        self.frame3.grid(row=2, column=0, sticky="nwse")
        #FRAME3
        self.frame3.columnconfigure(0, weight=1)
        self.frame3.columnconfigure(1, weight=3)
        self.frame3.columnconfigure(2, weight=5)
        self.frame3.columnconfigure(3, weight=2)
        self.frame3.columnconfigure(4, weight=3)
        self.frame3.columnconfigure(5, weight=3)
        #frame3.rowconfigure(0, weight=1)   -might need to change lets see how it works first 

        # = Frame(frame3, bg="white")
        #whiteRowFrame.grid(row=0, column=0, columnspan=6, sticky="nwse")

        LNLabel = Label(self.frame3, fg=BLUE, bg="white", text="LN", font=("Arial", 25))
        itemLabel = Label(self.frame3, fg=BLUE, bg="white", text="1-Item", font=("Arial", 25))
        descLabel = Label(self.frame3, fg=BLUE, bg="white", text="2-Description", font=("Arial", 25))
        qtyLabel = Label(self.frame3, fg=BLUE, bg="white", text="3-Qty", font=("Arial", 25))
        unitPriceLabel = Label(self.frame3, fg=BLUE, bg="white", text="4-Unit Price", font=("Arial", 25))
        extPriceLabel = Label(self.frame3, fg=BLUE, bg="white", text="Ext. Price", font=("Arial", 25))

        LNLabel.grid(row=0, column=0, sticky="nswe")
        itemLabel.grid(row=0, column=1, sticky="nswe")
        descLabel.grid(row=0, column=2, sticky="nswe")
        qtyLabel.grid(row=0, column=3, sticky="nswe")
        unitPriceLabel.grid(row=0, column=4, sticky="nswe")
        extPriceLabel.grid(row=0, column=5, sticky="nswe")

    def frame45Config(self):
        frame45Super = Frame(self.masterSC2, bg=BLUE)
        frame4 = Frame(frame45Super, bg=BLUE)
        frame5 = Frame(frame45Super, bg=BLUE)

        #FRAME4/5 SUPER LABELS/CONFIG
        frame45Super.rowconfigure(0, weight=1)
        frame45Super.columnconfigure(0, weight=2)
        frame45Super.columnconfigure(1, weight=2)
        frame4.grid(row=0, column=0, sticky="nswe")
        frame5.grid(row=0, column=1, sticky="nswe")
        frame45Super.grid(row=3, column=0, sticky="nwse")


        frame4.columnconfigure(0, weight=1)
        frame4.columnconfigure(1, weight=1)
        frame4.columnconfigure(2, weight=1)
        frame4.rowconfigure(0, weight=2)
        frame4.rowconfigure(1, weight=2)

        #======================================================================================================================================================

        optionLabel = Label(frame4, fg="white", bg=BLUE, text="Option - [", font=("Arial", 25))

        vcmd = frame4.register(self.validateLineEntry)
        self.optionEntry = Entry(frame4, font = ("Arial", 28), fg="white", bg=BLUE, width=2, validate="key", validatecommand=(vcmd, "%P"), bd=0, highlightthickness=0, insertbackground="white")
        closingOptionLabel = Label(frame4, fg="white", bg=BLUE, text="]", font=("Arial", 25))
        cancelLabel = Label(frame4, fg="white", bg=BLUE, text="Are you sure you want to cancel - [ ]", font=("Arial", 25))
        self.optionEntry.focus_set()

        self.optionEntry.bind("<Return>", self.lineNumEnter)
        self.frame3.bind("<Escape>", self.escPressed)

        optionLabel.grid(row=0, column=0, sticky="nsw")
        self.optionEntry.grid(row=0, column=1, sticky="nsw")
        closingOptionLabel.grid(row=0, column=2, sticky="nsw")
        cancelLabel.grid(row=1, column=0, sticky="nsw", columnspan=3)

        #======================================================================================================================================================


        frame5.columnconfigure(0, weight=1)
        frame5.columnconfigure(1, weight=1,)
        frame5.columnconfigure(2, weight=3)
        frame5.rowconfigure(0, weight=1)
        frame5.rowconfigure(1, weight=1)
        frame5.rowconfigure(2, weight=1)

        weightLabel = Label(frame5, text="W: 0000", font=("Arial", 25), fg="white", bg=BLUE)
        weightLabel.grid(row=2, column=0, sticky="e")

        subtotalLabel = Label(frame5, text="Subtotal:", font=("Arial", 25), fg="white", bg=BLUE)
        subtotalLabel.grid(row=0, column=1, sticky="e")

        taxLabel = Label(frame5, text="8.2500 Tax:", font=("Arial", 25), fg="white", bg=BLUE)
        taxLabel.grid(row=1, column=1, sticky="e")

        totalLabel = Label(frame5, text="Total Order:", font=("Arial", 25), fg="white", bg=BLUE)
        totalLabel.grid(row=2, column=1, sticky="e")

        subtotalNum = Label(frame5, text="0.0", font=("Arial", 25), fg="white", bg=BLUE)
        taxNum = Label(frame5, text="0.0", font=("Arial", 25), fg="white", bg=BLUE)
        totalNum = Label(frame5, text="0.0", font=("Arial", 25), fg="white", bg=BLUE)

        subtotalNum.grid(row=0, column=2, sticky="e")
        taxNum.grid(row=1, column=2, sticky="e")
        totalNum.grid(row=2, column=2, sticky="e")
    
    def frame6Config(self):
        frame6 = Frame(self.masterSC2, bg="white")
        frame6.grid(row=4, column=0, sticky="nwse")           

        #FRAME 6 LABELS
        frame6.columnconfigure(0, weight=2)
        frame6.columnconfigure(1, weight=5)
        frame6.rowconfigure(0, weight=1)

        inquiryF3Label = Label(frame6, text="F3-INQUIRY MENU", font=("Arial", 25), fg=BLUE, bg="white")
        inquiryF3Label.grid(row=0, column=0, sticky="e")

        totalF4Label = Label(frame6, text="F4-TOTAL", font=("Arial", 25), fg=BLUE, bg="white", padx=30)
        totalF4Label.grid(row=0, column=1, sticky="w")

    def callAllFrames(self):
        self.masterConfig()
        self.frame1Config()
        self.frame2Config()
        self.frame3Config()
        self.frame45Config()
        self.frame6Config()







class Item:
    def __init__(self, name, price, skew, quantity, category, subcategory, alpha, yardItem):
        self.__name = name 
        self.price = price
        self.__skew = skew
        self.quantity = quantity
        self.__category = category
        self.__subcategory = subcategory
        self.__alpha = alpha
        self.yardItem = yardItem

    def setName(self, inputName):
        self.__name = inputName
    def getName(self):
        return self.__name  
    def setPrice(self, inputPrice):
        self.price = inputPrice
    def getPrice(self):
        return self.price
    def setSkew(self, inputSkew):
        self.__skew = inputSkew
    def getSkew(self):
        return self.__skew  
    def setQuantity(self, inputQty):
        self.quantity = inputQty
    def getQuantity(self):
        return self.quantity
    def setCategory(self, inputCatergory):
        self.__category = inputCatergory
    def getCategory(self):
        return self.__category
    def setSubCategory(self, inputSub):
        self.__subcategory = inputSub
    def getSubCategory(self):
        return self.__subcategory
    def setAlpha(self, inputAlpha):
        self.__alpha = inputAlpha
    def getAlpha(self):
        return self.__alpha
    def getYardItem(self):
        return self.yardItem
        
if __name__ == "__main__":
    app = CASHSALE()
    app.callAllFrames()
    app.masterSC2.mainloop()



