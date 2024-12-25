from tkinter import *
from datetime import datetime
import sqlite3
from ItemClass import *
#from alphaSearchV2 import *

BLUE = "#27374D"



        

class TransCode01:
    def __init__(self, parent, alphaReturn):
        #self.masterSC2 = Tk()
        #self.masterSC2.title("CASHSALE")
        #second_monitor_x_offset = 1920
        #screen_width = self.masterSC2.winfo_screenwidth()
        #screen_height = self.masterSC2.winfo_screenheight()
        #self.masterSC2.geometry(f"{screen_width}x{screen_height}+{second_monitor_x_offset}+0")
        #self.masterSC2.geometry(f"{screen_width}x{screen_height}+0+0")

        self.parent = parent     #setting Tk instance that was passed in as self.parent


        self.cashsale = Frame(self.parent.masterSC1, bg=BLUE)      #setting self.parent.MASTERSC1 as main frame    "masterSC1" is attribute from MAC21
        self.cashsale.grid(row=0, column=0, sticky="nswe")

        self.alphaReturn = alphaReturn

        self.itemList = []
        self.itemCount = 0
        self.escapePress = False
        self.db_path = "/Users/erikrivera-sanchez/Documents/Python Related Projects/MAC21/dimensional_lumber.db"
        self.errorConfirmed = False #flag to see if user entered in "C" or "c" to confirm their input was invalid

        self.currentLabel = None
        self.currentEntry = None



        #same as validateFnEntry on ScreenFunctions.py
    def validateLineEntry(self, text):
        return len(text) <= 2
    
    def validateLineEntryError(self, text):

        return len(text) <= 1
    
    def cancelTransc(self):
        self.newFrame = Frame(self.frame4, bg=BLUE, border=0)
        self.newFrame.columnconfigure(0, weight=0)
        self.newFrame.rowconfigure(0, weight=1)
        self.newFrame.grid(row=1, column=0, columnspan=3)

        cancelLabel = Label(self.newFrame, fg="white", bg=BLUE, text="Are you sure you want to cancel(Y/N): [", font=("Arial", 25))
        cancelLabel.grid(row=0, column=0, sticky="e")
        vcmdInvalidSkew = self.newFrame.register(self.validateLineEntryError)
        cancelEntry = Entry(self.newFrame, fg="white", bg=BLUE, width=2, validate="key", font=("Arial", 25), validatecommand=(vcmdInvalidSkew, "%P"), bd=0, highlightthickness=0, insertbackground="white")
        cancelEntry.grid(row=0, column=1, sticky="e")
        closingLabel = Label(self.newFrame, fg="white", bg=BLUE, text="]", font=("Arial", 25))
        closingLabel.grid(row=0, column=2, sticky="e")
        cancelEntry.focus()

        self.cancelVar = StringVar()
        cancelEntry.config(textvariable=self.cancelVar)
        print(type(self.parent))

        cancelEntry.bind("<Return>", self.checkCancelConfirm)
      
    def checkCancelConfirm(self, event):
        if self.cancelVar.get() == 'Y' or self.cancelVar.get() == 'y':
            self.cashsale.destroy()
            self.parent.callAllFrames()


        elif self.cancelVar.get() == "N" or self.cancelVar.get() == "n": 
            self.newFrame.destroy()
            self.optionEntry.delete(0, END)
            self.optionEntry.focus()

        else:
            self.cancelVar.set("")
    #when calling fn from button press, event parameter is needed
    def lineNumEnter(self, event):
        text = self.optionEntry.get()
        print("YAY, we entered", text)
        if str(text) == "C" or str(text) == "c":
            self.cancelTransc()

        elif text == str(text):
            self.optionEntry.delete(0, END)    #deletes text in optionEntry if its a string

        text = int(text) #dosent let characters be inputted in optionEntry
        self.escapePress = False
        
        self.currentLabel = None
        self.currentEntry = None
        self.toggleNewLabel()

    def escPressed(self, event):
        self.escapePress = True
        self.toggleNewLabel()

    def toggleNewLabel(self):
        if not self.escapePress:
            if self.currentLabel is None:
                newLabel = Label(self.frame3, fg=BLUE, bg="white", text=str(self.itemCount + 1), font=("Arial", 25))
                self.currentLabel = newLabel
                self.currentLabel.grid(row=(self.itemCount+1), column=0, sticky="nwse")

                newEntry = Entry(self.frame3, fg="white", bg=BLUE, font=("Arial", 25), bd=0, highlightthickness=0, insertbackground="white")
                self.currentEntry = newEntry
                self.currentEntry.grid(row=(self.itemCount+1), column=1, sticky="nswe")
                self.currentEntry.bind("<Escape>", self.escPressed)

                self.currentEntry.focus()

                self.descpEntryVar = StringVar()
                self.currentEntry.config(textvariable=self.descpEntryVar)
                self.currentEntry.bind("<Return>", lambda event: self.handleSearchBySkew(self.descpEntryVar.get(), "transcMenu"))
                self.currentEntry.bind("<F9>", lambda event: self.handleSearchByAlpha(self.descpEntryVar.get(), "transcMenu"))


        else:
            if self.currentLabel is not None:
                self.currentLabel.destroy()
                self.currentEntry.destroy()
                self.currentLabel = None
                self.optionEntry.delete(0, END)
                self.optionEntry.focus()  
    #event is skew, function only activates if ENTER is pressed on newEntry1
    def searchItemBySkew(self, skew):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dimensional_lumber WHERE skew = ?", (skew,))

        #getting the result
        row = cursor.fetchall()

        conn.close()


        if row:
            return row
        else:
            return None

    def searchItemByAlpha(self, alpha):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dimensional_lumber WHERE alpha = ?", (alpha,))

        #getting result
        row = cursor.fetchall()
        
        conn.close()


        if row:
            return row
        else:
            return None

    def handleSearchBySkew(self, skew, typeOfSearch):
        skew = str(skew)
        item = self.searchItemBySkew(skew)
        if item and (typeOfSearch == "transcMenu"): 
            item = item[0]
            item_id, name, price, skew, quantity, category, subcategory, alpha, yardItem = item

            item = Item(name, price, skew, quantity, category, subcategory, alpha, yardItem)
            item.setItemID(self.itemCount+1)

            self.addToItemList(item)
            self.addItemToScreen()



        elif item == None:
            self.displayNotFoundErrorMessageSC2()
    
    def handleSearchByAlpha(self, alpha, typeOfSearch):
        alpha = str(alpha)
        item = self.searchItemByAlpha(alpha)
        if item and (typeOfSearch == "transcMenu"):
            self.hideAllFrames()
            self.cashsale.columnconfigure(0, weight=1)
            self.cashsale.rowconfigure(0, weight=1)
            self.cashsale.rowconfigure(1, weight=0)
            self.cashsale.rowconfigure(2, weight=0)
            self.cashsale.rowconfigure(3, weight=0)
            self.cashsale.rowconfigure(4, weight=0)

            from alphaSearch import AlphaSearch
            alphaSearch = AlphaSearch(self.parent, alpha)
            alphaSearch.callAllFrames()



        elif item == None:
            self.displayNotFoundErrorMessageSC2()
            

    def hideAllFrames(self):
        if self.frame1:
            self.frame1.grid_forget()
        if self.frame2:
            self.frame2.grid_forget()
        if self.frame3:
            self.frame3.grid_forget()
        if self.frame45Super:
            self.frame45Super.grid_forget()
        if self.frame6:
            self.frame6.grid_forget()

            

    def addToItemList(self, item):
        if self.itemCount == 0:
            self.itemList.append(item)
            self.itemCount = self.itemCount + 1
        else:
            self.itemList.append(item)
            self.itemCount = self.itemCount + 1

    def addItemToScreen(self):
        print(self.itemCount)
        latestItemAdded = self.itemList[self.itemCount-1]
        priceLabel = Label(self.frame3, fg="white", bg=BLUE, text=latestItemAdded.getPrice(), font=("Arial", 25))
        priceLabel.grid(row=(self.itemCount), column=4, sticky="nswe")

        descrpLabel = Label(self.frame3, fg="white", bg=BLUE, text=latestItemAdded.getName(), font=("Arial", 25))
        descrpLabel.grid(row=(self.itemCount), column=2, sticky="nswe")

        skewLabel = Label(self.frame3, fg="white", bg=BLUE, text=latestItemAdded.getSkew(), font=("Arial", 25))
        skewLabel.grid(row=(self.itemCount), column=1, sticky="nswe")
        
        qtyEntry = Entry(self.frame3, fg="white", bg=BLUE, font=("Arial", 25), bd=0, highlightthickness=0, insertbackground="white")
        qtyEntry.grid(row=(self.itemCount), column=3, sticky="nswe", padx=(0, 0))
        qtyEntry.focus()


        qtyEntryVar = StringVar()
        qtyEntry.config(textvariable=qtyEntryVar)
        qtyEntry.bind("<Return>", lambda event: self.enterOnQty(qtyEntry))

    def enterOnQty(self, qtyEntry):
        qty = qtyEntry.get()
        qty = float(qty)
        item = self.itemList[self.itemCount-1]
        item.setQuantity(qty)
        price = item.getPrice()
        price = float(price)

        extCost = round(price * qty, 2)
        extCost = str(extCost)
        extCostLabel =  Label(self.frame3, fg="white", bg=BLUE, text=extCost, font=("Arial", 25))
        extCostLabel.grid(row=self.itemCount, column=5, sticky="nwse")
        self.updateSubTaxTotal()
        self.optionEntry.delete(0, END)
        self.optionEntry.focus()
        self.toggleNewLabel()

    def escOnOptionPress(self, event):
        #delete text on optionEntry
        self.optionEntry.delete(0, END)

    def updateSubTaxTotal(self):
        subtotal = 0.0
        for item in self.itemList:
            price = item.getPrice()
            qty = item.getQuantity()
            subtotal = subtotal + (price*qty)

        subtotal = round(subtotal, 2)
        tax = round(subtotal * 0.0825, 2)
        total = round(subtotal + tax, 2)
        

        self.subtotalNum.config(text=str(subtotal))
        self.taxNum.config(text=str(tax))
        self.totalNum.config(text=str(total))
        self.currentLabel = None
        self.currentEntry = None

    def displayNotFoundErrorMessageSC2(self):
        self.errorConfirmed = False
        self.newFrame = Frame(self.frame4, bg=BLUE, border=0)
        self.newFrame.columnconfigure(0, weight=0)
        self.newFrame.rowconfigure(0, weight=1)
        self.newFrame.grid(row=1, column=0, columnspan=3)

        notfoundLabel = Label(self.newFrame, fg="white", bg=BLUE, text="INVALID INPUT-Press C to continue: [", font=("Arial", 25))
        notfoundLabel.grid(row=0, column=0, sticky="e")
        vcmdInvalidSkew = self.newFrame.register(self.validateLineEntryError)
        notFoundEntry = Entry(self.newFrame, fg="white", bg=BLUE, width=2, validate="key", font=("Arial", 25), validatecommand=(vcmdInvalidSkew, "%P"), bd=0, highlightthickness=0, insertbackground="white")
        notFoundEntry.grid(row=0, column=1, sticky="e")
        closingLabel = Label(self.newFrame, fg="white", bg=BLUE, text="]", font=("Arial", 25))
        closingLabel.grid(row=0, column=2, sticky="e")
        notFoundEntry.focus()

        self.errorVar = StringVar()
        notFoundEntry.config(textvariable=self.errorVar)

        notFoundEntry.bind("<Return>", self.checkErrorConfirm)

    def checkErrorConfirm(self, event):
        if self.errorVar.get() == 'C' or self.errorVar.get() == 'c':
            self.errorConfirmed = True
            self.newFrame.destroy()
            self.currentEntry.focus()
            self.descpEntryVar.set("")


        else: 
            self.errorConfirmed = False

    def masterConfig(self):
        self.cashsale.columnconfigure(0, weight=1)
        self.cashsale.rowconfigure(0, weight=1)
        self.cashsale.rowconfigure(1, weight=1)
        self.cashsale.rowconfigure(2, weight=12)
        self.cashsale.rowconfigure(3, weight=3)
        self.cashsale.rowconfigure(4, weight=1)
    
    def frame1Config(self):
        self.frame1 = Frame(self.cashsale, bg=BLUE)
        self.frame1.grid(row=0, column=0, sticky="nwse")

        ##FRAME1 LABELS
        self.frame1.rowconfigure(0, weight=1)

        clerkLabel = Label(self.frame1, fg="white", bg=BLUE, text="CLERK-00000", font=("Arial", 25))
        clerkLabel.grid(row=0, column=0, sticky="nsw", padx=(0, 30))

        scrnLabel = Label(self.frame1, fg="white", bg=BLUE, text="SCRN-2", font=("Arial", 25))
        scrnLabel.grid(row=0, column=1, sticky="nsw", padx=(150, 150))

        transcName = Label(self.frame1, fg="white", bg=BLUE, text="CASH SALE", font=("Arial", 25))
        transcName.grid(row=0, column=2, padx=(60, 0))

        orderNumber = Label(self.frame1, fg="white", bg=BLUE, text="ORDER: ######", font=("Arial", 25))
        orderNumber.grid(row=0, column=3)

    def frame2Config(self):
        self.frame2 = Frame(self.cashsale, bg=BLUE)
        self.frame2.grid(row=1, column=0, sticky="nwse")
        ##FRAME2 LABELS 
        self.frame2.rowconfigure(0, weight=1)

        accountNumberLabel =  Label(self.frame2, fg="white", bg=BLUE, text="#########", font=("Arial", 25))
        accountNumberLabel.grid(row=0, column=0, sticky="nse")

        accountNameLabel =  Label(self.frame2, fg="white", bg=BLUE, text="ACCOUNTNAME", font=("Arial", 25))
        accountNameLabel.grid(row=0, column=1)

    def frame3Config(self):
        self.frame3 = Frame(self.cashsale, bg=BLUE)
        self.frame3.grid(row=2, column=0, sticky="nwse")
        #FRAME3
        self.frame3.columnconfigure(0, weight=1)
        self.frame3.columnconfigure(1, weight=3)
        self.frame3.columnconfigure(2, weight=5)
        self.frame3.columnconfigure(3, weight=1)
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
        self.frame45Super = Frame(self.cashsale, bg=BLUE)
        self.frame4 = Frame(self.frame45Super, bg=BLUE)
        self.frame5 = Frame(self.frame45Super, bg=BLUE)

        #FRAME4/5 SUPER LABELS/CONFIG
        self.frame45Super.rowconfigure(0, weight=1)
        self.frame45Super.columnconfigure(0, weight=2)
        self.frame45Super.columnconfigure(1, weight=2)
        self.frame45Super.grid(row=3, column=0, sticky="nwse")
        self.frame4.grid(row=0, column=0, sticky="nswe")
        self.frame5.grid(row=0, column=1, sticky="nswe")


        self.frame4.columnconfigure(0, weight=1)
        self.frame4.columnconfigure(1, weight=1)
        self.frame4.columnconfigure(2, weight=1)
        self.frame4.rowconfigure(0, weight=1)
        self.frame4.rowconfigure(1, weight=3)

        #======================================================================================================================================================

        optionLabel = Label(self.frame4, fg="white", bg=BLUE, text="Option - [", font=("Arial", 25))

        vcmd = self.frame4.register(self.validateLineEntry)
        self.optionEntry = Entry(self.frame4, font = ("Arial", 28), fg="white", bg=BLUE, width=2, validate="key", validatecommand=(vcmd, "%P"), bd=0, highlightthickness=0, insertbackground="white")
        closingOptionLabel = Label(self.frame4, fg="white", bg=BLUE, text="]", font=("Arial", 25))
        cancelLabel = Label(self.frame4, fg="white", bg=BLUE, text="Are you sure you want to cancel - [ ]", font=("Arial", 25))
        self.optionEntry.focus_set()

        self.optionEntry.bind("<Return>", self.lineNumEnter)
        self.optionEntry.bind("<Escape>", self.escOnOptionPress), 
        self.frame3.bind("<Escape>", self.escPressed)

        optionLabel.grid(row=0, column=0, sticky="w")
        self.optionEntry.grid(row=0, column=1, sticky="w")
        closingOptionLabel.grid(row=0, column=2, sticky="w")
        #cancelLabel.grid(row=1, column=0, sticky="nsw", columnspan=3)

        #======================================================================================================================================================


        self.frame5.columnconfigure(0, weight=1)
        self.frame5.columnconfigure(1, weight=1,)
        self.frame5.columnconfigure(2, weight=3)
        self.frame5.rowconfigure(0, weight=1)
        self.frame5.rowconfigure(1, weight=1)
        self.frame5.rowconfigure(2, weight=1)

        weightLabel = Label(self.frame5, text="W: 0000", font=("Arial", 25), fg="white", bg=BLUE)
        weightLabel.grid(row=2, column=0, sticky="e")

        subtotalLabel = Label(self.frame5, text="Subtotal:", font=("Arial", 25), fg="white", bg=BLUE)
        subtotalLabel.grid(row=0, column=1, sticky="e")

        taxLabel = Label(self.frame5, text="8.2500 Tax:", font=("Arial", 25), fg="white", bg=BLUE)
        taxLabel.grid(row=1, column=1, sticky="e")

        totalLabel = Label(self.frame5, text="Total Order:", font=("Arial", 25), fg="white", bg=BLUE)
        totalLabel.grid(row=2, column=1, sticky="e")

        self.subtotalNum = Label(self.frame5, text="0.0", font=("Arial", 25), fg="white", bg=BLUE)
        self.taxNum = Label(self.frame5, text="0.0", font=("Arial", 25), fg="white", bg=BLUE)
        self.totalNum = Label(self.frame5, text="0.0", font=("Arial", 25), fg="white", bg=BLUE)

        self.subtotalNum.grid(row=0, column=2, sticky="e")
        self.taxNum.grid(row=1, column=2, sticky="e")
        self.totalNum.grid(row=2, column=2, sticky="e")
    
    def frame6Config(self):
        self.frame6 = Frame(self.cashsale, bg="white")
        self.frame6.grid(row=4, column=0, sticky="nwse")           

        #FRAME 6 LABELS
        self.frame6.columnconfigure(0, weight=2)
        self.frame6.columnconfigure(1, weight=5)
        self.frame6.rowconfigure(0, weight=1)

        inquiryF3Label = Label(self.frame6, text="F3-INQUIRY MENU", font=("Arial", 25), fg=BLUE, bg="white")
        inquiryF3Label.grid(row=0, column=0, sticky="e")

        totalF4Label = Label(self.frame6, text="F4-TOTAL", font=("Arial", 25), fg=BLUE, bg="white", padx=30)
        totalF4Label.grid(row=0, column=1, sticky="w")

    def callAllFrames(self):
        self.masterConfig()
        self.frame1Config()
        self.frame2Config()
        self.frame3Config()
        self.frame45Config()
        self.frame6Config()


        
if __name__ == "__main__":
    app = TransCode01()
    app.callAllFrames()
    app.masterSC2.mainloop()


