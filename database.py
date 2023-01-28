import sqlite3
import datetime

CREATE_raw_materials = "CREATE TABLE IF NOT EXISTS raw_materials (id INTEGER PRIMARY KEY,item_name TEXT, quantity INTEGER, unit_price INTEGER, amount INTEGER, date date);"
CREATE_issued_items = "CREATE TABLE IF NOT EXISTS issued_items (id INTEGER PRIMARY KEY,item_name TEXT, quantity_issued INTEGER, unit_price INTEGER, amount INTEGER, date date);"
CREATE_artwork_details = "CREATE TABLE IF NOT EXISTS artwork_details (Product_Id INTEGER PRIMARY KEY,Product_Name TEXT, Artist_Name TEXT, Medium_Used TEXT, Product_Price INTEGER, Status TEXT, image blob,date date);"
CREATE_additional_expenses = "CREATE TABLE IF NOT EXISTS artwork_details (Expense_ID INTEGER PRIMARY KEY,  Type       TEXT, Cost INTEGER);"
#CREATE_closing_balance = "CREATE TABLE IF NOT EXISTS closing_balance (ID INTEGER PRIMARY KEY,Item TEXT,Quantity INTEGER,Unit Price INTEGER, Amount  INTEGER);"

INSERT_raw_materials = "INSERT INTO raw_materials (item_name, quantity, unit_price, amount) VALUES(?,?,?,?);"
INSERT_artwork_details = "INSERT INTO artwork_details (Product_Name, Artist_Name, Medium_Used, Product_Price, date,image) VALUES(?,?,?,?,?,?);"

SELECT_ALL1 = "SELECT * FROM raw_materials;"
SELECT_TRV= "SELECT id,item_name,quantity,unit_price,amount FROM raw_materials;"
SELECT_TRV1= "SELECT id,item_name,quantity,unit_price,amount FROM raw_materials where date between (?) and (?);"
SELECT_TRV2= "SELECT a.id,a.item_name,a.quantity_issued,a.unit_price,a.amount FROM issued_items a, raw_materials b where a.id = b.id;"
SELECT_TRV_D= "SELECT a.id,a.item_name,a.quantity_issued,a.unit_price,a.amount FROM issued_items  a, raw_materials b where a.id = b.id and a.date between (?) and (?);"
SELECT_TRV3= "SELECT Product_Id, Product_Name,Artist_Name, Medium_Used, Product_Price, Status FROM artwork_details;"
SELECT_TRV3_d= "SELECT Product_Id, Product_Name,Artist_Name, Medium_Used, Product_Price, Status FROM artwork_details where date between (?) and (?);"

SELECT_TRV4 = "SELECT Product_Id, Product_Name,Artist_Name, Medium_Used, Product_Price    FROM artwork_details where Status = 'Sold';"
SELECT_TRV5 = "SELECT Product_Id, Product_Price    FROM artwork_details where Status='Sold';"
SELECT_TRV6 = "SELECT sum(Product_Price) FROM artwork_details where Status='Sold';"
SELECT_TRV7 = "SELECT Expense_ID, Type, Cost FROM additional_expenses;"
SELECT_TRV8 = "SELECT sum(Cost) FROM additional_expenses ;"
SELECT_TRV9 = "SELECT sum(amount) FROM raw_materials ;"
SELECT_TRV10= "SELECT a.id, a.item_name, (a.quantity - b.quantity_issued) as quantity,a.unit_price, (a.quantity - b.quantity_issued) * a.unit_price as amount FROM  raw_materials a,issued_items b where a.id=b.id ;"
SELECT_TRV10_d= "SELECT a.id, a.item_name, (a.quantity - b.quantity_issued) as quantity,a.unit_price, (a.quantity - b.quantity_issued) * a.unit_price as amount FROM  raw_materials a,issued_items b where a.id=b.id and b.date between ? and ?;"
 

SELECT_raw_materials = "SELECT * FROM raw_materials WHERE ID = ?;" # will be used later or merged with TRV queries above later
SELECT_issued_items= "SELECT * FROM issued_items where ID=?;"
SELECT_issued_items_all= "SELECT id,item_name,quantity_issued,unit_price,amount FROM issued_items ;"
SELECT_artwork_details = "SELECT * FROM artwork_details WHERE Product_Id = ?;"

DELETE_raw_material = "DELETE FROM raw_materials WHERE ID = ?;"
DELETE_artwork_details = "DELETE FROM artwork_details WHERE Product_Id = ?; " 
UPDATE_raw_materials = "UPDATE raw_materials set item_name=?, quantity=?, unit_price=?, amount=? where ID =?;"
UPDATE_issued_items ="UPDATE issued_items set item_name=?, quantity_issued=?, unit_price=?, amount=? where ID =?;"
#UPDATE_artwork_details ="UPDATE artwork_details set Product_Name=?, Artist_Name=?, Medium_Used=?, Product_Price=?, Status=?, date=? where Product_Id = ?;"
UPDATE_artwork_details ="UPDATE artwork_details set Product_Name=?, Artist_Name=?, Medium_Used=?, Product_Price=?, Status=? where Product_Id = ?;"



def select_trv():
    conn = sqlite3.connect('data.db')
    with conn:
         return conn.execute(SELECT_TRV)

def select_trv1(from_date,to_date):
    conn = sqlite3.connect('data.db')
    with conn:        
        return conn.execute(SELECT_TRV1,(from_date,to_date))

def select_trv_issued_date(from_date,to_date):
    conn = sqlite3.connect('data.db')
    with conn:        
        return conn.execute(SELECT_TRV_D,(from_date,to_date))
    
def select_trv_issued():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(SELECT_TRV2)
def select_trv_artwork():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(SELECT_TRV3)
    
def select_trv_artwork_date(from_date,to_date):
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(SELECT_TRV3_d,(from_date,to_date))
    
def select_trv_artwork1():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(SELECT_TRV4)
def select_trv_artwork2():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(SELECT_TRV5)
def select_trv_artwork3():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(SELECT_TRV6)
def select_trv_artwork4():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(SELECT_TRV7)
def select_trv_artwork5():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(SELECT_TRV8)
def select_trv_artwork6():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(SELECT_TRV9)
def select_trv_closing():
    conn = sqlite3.connect('data.db')
    with conn:
         return conn.execute(SELECT_TRV10)
def select_trv_closing_date(e1,e2):
    conn = sqlite3.connect('data.db')
    with conn:
         return conn.execute(SELECT_TRV10_d)
 
     
    

def select_raw_material(ID):
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(SELECT_raw_materials, (ID,))
    
def select_issued_item(ID):
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(SELECT_issued_items, (ID,))
def select_issued_item_all():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(SELECT_issued_items_all)
    
def select_artwork_detail(ID):
    conn = sqlite3.connect('data.db')
    with conn:
         return conn.execute(SELECT_artwork_details, (ID,))
        

###create for every table###
def create_tables():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(CREATE_OTHER)

def create_raw():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(CREATE_raw_materials)

create_raw()
###INSERT VALUES###

def insert_raw_materials(item_name, quantity, unit_price, amount):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_raw_materials, (item_name, quantity, unit_price, amount))
        conn.commit()
        c.close()



def insert_artwork_details(product, artist, medium, price,date,img):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_artwork_details, (product, artist, medium, price,date,img))
        conn.commit()
        c.close()

 

###SELECT_ALL###
 
def select_all_raw_materials():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL1)
        #have to store data into a list of Tuple
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output




###SELECT SPECIFIC###

##        # have to store data into a list of Tuple
##        list = c.fetchall()
##        c.close()
##        output = ''
##        for x in list:
##            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
##        return output 
## 
 


###DELETE VALUE###
def delete_raw_materials(ID):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
         
        c.execute(DELETE_raw_material, (ID,))
        conn.commit()
        c.close()

def delete_artwork_details(ID):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_artwork_details, (ID,))
        conn.commit()
        c.close()

##### UPDATE RECORDS
def update_raw_materials(item_name, quantity, unit_price, amount, ID):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(UPDATE_raw_materials, (item_name, quantity, unit_price, amount, ID))
        conn.commit()
        c.close()

def update_issued_item(item_name, quantity, unit_price, amount, ID):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(UPDATE_issued_items, (item_name, quantity, unit_price, amount, ID))
        conn.commit()
        c.close()

def update_artwork_detail(product_name, artist_name, medium_used, product_price,status,ID):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(UPDATE_artwork_details, (product_name, artist_name, medium_used, product_price,status,ID))
        conn.commit()
        c.close()
