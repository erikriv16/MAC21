from tkinter import *
from datetime import datetime
import sqlite3
from ItemClass import *



BLUE = "#27374D"
HIGHLIGHT_COLOR = "#4CAF50"

class AlphaSearch:
    def validateLineEntry(self, text):
        return len(text) <= 2

    def searchItemByAlpha(self, alpha):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dimensional_lumber WHERE alpha = ?", (alpha,))

        #getting the result
        row = cursor.fetchall()

        conn.close()

        print(row)
        print("=========================")

        if row:
            return row
        else:
            return None
          
    def storeResults(self):
        items = self.searchItemByAlpha(self.alpha)
        for merchandise in items:
            item_id, name, price, skew, quantity, category, subcategory, alpha, yardItem = merchandise

            item = Item(name, price, skew, quantity, category, subcategory, alpha, yardItem)
            
            self.addToItemList(item)

    def addToItemList(self, item):
        self.itemList.append(item)
        self.itemCount = self.itemCount + 1

    def displayResults(self):
        self.itemLabels = []
        for i, index in enumerate(self.itemList):
            item = self.itemList[i]
            LNItemLabel = Label(self.frame3, font=("Arial", 25), text=str(i+1), bg=BLUE, fg="white")
            itemNumberLabel = Label(self.frame3, font=("Arial", 25), text=str(item.getSkew()), bg=BLUE, fg="white")
            itemDescLabel = Label(self.frame3, font=("Arial", 25), text=str(item.getName()), bg=BLUE, fg="white")
            itemAvailableLabel = Label(self.frame3, font=("Arial", 25), text=str(item.getQuantity()), bg=BLUE, fg="white")
            itemPriceLabel = Label(self.frame3, font=("Arial", 25), text=str(item.getPrice()), bg=BLUE, fg="white")

            LNItemLabel.grid(row=(i+1), column=0, sticky="nswe")
            itemNumberLabel.grid(row=(i+1), column=1, sticky="nswe")
            itemDescLabel.grid(row=(i+1), column=2, sticky="nswe")
            itemAvailableLabel.grid(row=(i+1), column=3, sticky="nswe")
            itemPriceLabel.grid(row=(i+1), column=4, sticky="nswe")

            self.itemLabels.append([LNItemLabel, itemNumberLabel, itemDescLabel, itemAvailableLabel, itemPriceLabel])

        self.updateSelectedRow()
            
    def updateSelectedRow(self):
        for i, labelRow in enumerate(self.itemLabels):
            if i == self.selectedRow:
                for label in labelRow:
                    label.config(bg="white")  
                    label.config(fg=BLUE)

            else:
                for label in labelRow:
                    label.config(bg=BLUE)
                    label.config(fg="white")          

    def selectNextRow(self, event=None):
        if self.selectedRow < self.itemCount and self.selectedRow != (self.itemCount-1):
            print("you pressed DOWN")
            self.selectedRow += 1
            print(self.itemList[self.selectedRow])

        self.updateSelectedRow()

    def selectPreviousRow(self, event=None):
        if self.selectedRow > 0:
            print("you pressed UP")
            self.selectedRow -= 1
            print(self.selectedRow)
            print(self.itemList[self.selectedRow])



        self.updateSelectedRow()
            
    def onF5press(self, event=None):
        selectedItem = (self.itemList[self.selectedRow])
        from TransCode01 import TransCode01
        transCode01Screen = TransCode01(self.parent, selectedItem)
        transCode01Screen.callAllFrames()


    def __init__(self, parent, alpha):
        self.parent = parent
        self.alpha = alpha

        self.alphasearch = Frame(self.parent.masterSC1, bg=BLUE)
        self.alphasearch.grid(row=0, column=0, sticky="nswe")


        self.db_path = "/Users/erikrivera-sanchez/Documents/Python Related Projects/MAC21/dimensional_lumber.db"
        self.itemList = []
        self.itemCount = 0
        self.selectedRow = 0
        self.parent.masterSC1.bind("<Down>", self.selectNextRow)
        self.parent.masterSC1.bind("<Up>", self.selectPreviousRow)
        self.parent.masterSC1.bind("<F5>", self.onF5press)


    def masterConfig(self):
        self.alphasearch.columnconfigure(0, weight=1)
        self.alphasearch.rowconfigure(0, weight=1)
        self.alphasearch.rowconfigure(1, weight=1)
        self.alphasearch.rowconfigure(2, weight=10)
        self.alphasearch.rowconfigure(3, weight=3)
        self.alphasearch.rowconfigure(4, weight=1)

        self.frame1 = Frame(self.alphasearch, bg=BLUE)
        self.frame2 = Frame(self.alphasearch, bg="white")
        self.frame3 = Frame(self.alphasearch, bg=BLUE)
        self.frame4 = Frame(self.alphasearch, bg=BLUE)
        self.frame5 = Frame(self.alphasearch, bg="white")

        self.frame1.grid(row=0, column=0, sticky="nswe")
        self.frame2.grid(row=1, column=0, sticky="nswe")
        self.frame3.grid(row=2, column=0, sticky="nswe")
        self.frame4.grid(row=3, column=0, sticky="nswe")
        self.frame5.grid(row=4, column=0, sticky="nswe")

    def frame1config(self):
        ################TIME LABEL 
        currentDate = datetime.now().strftime("%B %d, %Y").upper() #gets current date on computer
        dateLabel = Label(self.frame1, font=("Arial", 32), text=currentDate, bg=BLUE, fg="white")
        dateLabel.grid(row=0, column=0, sticky="nwse", padx=0)

        ###########UNDECIDED LABEL 
        nameLabel = Label(self.frame1, font=("Arial", 32), text="UNDECIDED", bg=BLUE, fg="white")
        nameLabel.grid(row=0, column=1, sticky="nswe", padx=300)

        ######SCR LABEL 
        scrLabel = Label(self.frame1, font=("Arial", 32), text="SCNR-3", bg=BLUE, fg="white")
        scrLabel.grid(row=0, column=2, sticky="nswe", padx=0)
            
    def frame2config(self):
        inquiryByAlphaLabel = Label(self.frame2, font=("Arial", 32), text=("Inquiry By Alpha:" + self.alpha), bg="white", fg=BLUE)
        inquiryByAlphaLabel.grid(row=1, column=0, sticky="nswe", padx=(1100, 0), pady=0)

    def frame3config(self):
        self.frame3.columnconfigure(0, weight=1)
        self.frame3.columnconfigure(1, weight=3)
        self.frame3.columnconfigure(2, weight=9)
        self.frame3.columnconfigure(3, weight=2)
        self.frame3.columnconfigure(4, weight=2)

        LNLabel = Label(self.frame3, bg=BLUE, fg="white", text="LN", font=("Arial", 25))
        itemLabel = Label(self.frame3, bg=BLUE, fg="white", text="Item-Number", font=("Arial", 25))
        descLabel = Label(self.frame3, bg=BLUE, fg="white", text="--------Description--------", font=("Arial", 25))
        availableLabel = Label(self.frame3, bg=BLUE, fg="white", text="Available", font=("Arial", 25))
        priceLabel = Label(self.frame3, bg=BLUE, fg="white", text="Price", font=("Arial", 25))

        LNLabel.grid(row=0, column=0, sticky="nswe")
        itemLabel.grid(row=0, column=1, sticky="nswe")
        descLabel.grid(row=0, column=2, sticky="nswe")
        availableLabel.grid(row=0, column=3, sticky="nswe")
        priceLabel.grid(row=0, column=4, sticky="nswe")

        print("hello aw;ldfkji0")

        self.frame3.bind("<Down>", self.selectNextRow)
        self.frame3.bind("<Up>", self.selectPreviousRow)
        self.frame3.bind("<F5>", self.onF5press)

    def frame4config(self):
        optionLabel = Label(self.frame4, fg="white", bg=BLUE, text="Option - [", font=("Arial", 32))

        vcmd = self.frame4.register(self.validateLineEntry)
        self.optionEntry = Entry(self.frame4, font = ("Arial", 28), fg="white", bg=BLUE, width=2, validate="key", validatecommand=(vcmd, "%P"), bd=0, highlightthickness=0, insertbackground="white")
        closingOptionLabel = Label(self.frame4, fg="white", bg=BLUE, text="]", font=("Arial", 32))

        optionLabel.grid(row=0, column=0, sticky="nsw")
        self.optionEntry.grid(row=0, column=1, sticky="nsw")
        closingOptionLabel.grid(row=0, column=2, sticky="nsw")
        self.optionEntry.focus()

    def frame5config(self):
        poInquiryLabel = Label(self.frame5, fg=BLUE, bg="white", text="F2 = POInq", font=("Arial", 32))
        branchLabel = Label(self.frame5, fg=BLUE, bg="white", text="F3 = Branch", font=("Arial", 32))
        itemInfoLabel = Label(self.frame5, fg=BLUE, bg="white", text="F6 = ItemInfo", font=("Arial", 32))

        poInquiryLabel.grid(row=0, column=0, sticky="nswe")
        branchLabel.grid(row=0, column=1, sticky="nswe")
        itemInfoLabel.grid(row=0, column=2, sticky="nswe")

        self.storeResults()
        self.displayResults()

    def callAllFrames(self):
        self.masterConfig()
        self.frame1config()
        self.frame2config()
        self.frame3config()
        self.frame4config()
        self.frame5config()
        


            
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
        self.itemID = 0

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
    def setItemID(self, itemID):
        self.itemID = itemID
    def getItemID(self):
        return self.itemID

if __name__ == "__main__":
    app = AlphaSearch()
    app.callAllFrames()
    app.alphaSearch.mainloop()
