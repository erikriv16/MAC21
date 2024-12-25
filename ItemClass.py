#creating 5 lumber products, adding it to database, attempting to connect with TK FILE - TEST USE
import sqlite3

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
        

item1 = Item("1x2-8 SPF Kiln Dried ", 1.99, "012603", 580, "lumber", "dimensional_lumber", "1208", False)
item2 = Item("1x2-10 SPF Kiln Dried ", 3.49, "012606", 657, "lumber", "dimensional_lumber", "1210", False)
item3 = Item("1x2-8 #2 Treated MCA .06 ", 3.19, "011336", 105, "lumber", "dimensional_lumber", "1208", False)
item4 = Item("1x2-8 Western Red Cedar S1S2E", 4.69, "012000", 142, "lumber", "dimensional_lumber", "1208", False)
item5 = Item("1x2-10 Western Red Cedar S1S2E", 5.79, "012002", 169, "lumber", "dimensional_lumber", "1210", False)



db_path = "/Users/erikrivera-sanchez/Documents/Python Related Projects/MAC21/dimensional_lumber.db"
##ADDING 5 ITEMS TO DATABASE(already added, thats why everything is commented out)
# #===============================================================
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# #setting up table structure (columns)
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS dimensional_lumber (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     price REAL NOT NULL,
#     skew TEXT NOT NULL,
#     quantity INTEGER NOT NULL,
#     category TEXT NOT NULL,
#     subcategory TEXT NOT NULL,
#     alpha TEXT NOT NULL,
#     yardItem BOOLEAN NOT NULL  
# )    
# ''')
# #inserting item1
# cursor.execute('''
# INSERT INTO dimensional_lumber (name, price, skew, quantity, category, subcategory, alpha, yardItem)
# VALUES (?, ?, ?, ?, ?, ?, ?, ?)
# ''', (item1.getName(), item1.getPrice(), item1.getSkew(), item1.getQuantity(), item1.getCategory(), item1.getSubCategory(), item1.getAlpha(), item1.getYardItem())
# )
# #inserting item2
# cursor.execute('''
# INSERT INTO dimensional_lumber (name, price, skew, quantity, category, subcategory, alpha, yardItem)
# VALUES (?, ?, ?, ?, ?, ?, ?, ?)
# ''', (item2.getName(), item2.getPrice(), item2.getSkew(), item2.getQuantity(), item2.getCategory(), item2.getSubCategory(), item2.getAlpha(), item2.getYardItem())
# )
# #inserting item3
# cursor.execute('''
# INSERT INTO dimensional_lumber (name, price, skew, quantity, category, subcategory, alpha, yardItem)
# VALUES (?, ?, ?, ?, ?, ?, ?, ?)
# ''', (item3.getName(), item3.getPrice(), item3.getSkew(), item3.getQuantity(), item3.getCategory(), item3.getSubCategory(), item3.getAlpha(), item3.getYardItem())
# )
# #inserting item4
# cursor.execute('''
# INSERT INTO dimensional_lumber (name, price, skew, quantity, category, subcategory, alpha, yardItem)
# VALUES (?, ?, ?, ?, ?, ?, ?, ?)
# ''', (item4.getName(), item4.getPrice(), item4.getSkew(), item4.getQuantity(), item4.getCategory(), item4.getSubCategory(), item4.getAlpha(), item4.getYardItem())
# )
# #inserting item5
# cursor.execute('''
# INSERT INTO dimensional_lumber (name, price, skew, quantity, category, subcategory, alpha, yardItem)
# VALUES (?, ?, ?, ?, ?, ?, ?, ?)
# ''', (item5.getName(), item5.getPrice(), item5.getSkew(), item5.getQuantity(), item5.getCategory(), item5.getSubCategory(), item5.getAlpha(), item5.getYardItem())
# )
# conn.commit()
# conn.close()
##=====================================

def viewLumberDB():
    #not working=======
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    #probably this line=====
    cursor.execute('PRAGMA table_info("dimensional_lumber.db")')
    columns = cursor.fetchall()

    print("Table structure:")
    for column in columns:
        print(column)

    conn.close()
    #not working======



    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM dimensional_lumber')
    rows = cursor.fetchall()

    print("Table Data:")
    for row in rows:
        print(row)

    conn.close()

def resetIDCountLumberDB():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    #resets ID count so it won't keep repeating if you use the deleteItemsLumberDB fn
    cursor.execute('DELETE FROM sqlite_sequence WHERE name="dimensional_lumber"')
    conn.commit()
    conn.close()
def deleteItemsLumberDB():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM dimensional_lumber')

    conn.commit()
    conn.close()

# deleteItemsLumberDB()
# resetIDCountLumberDB()
viewLumberDB()