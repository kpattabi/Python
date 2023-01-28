import db_art
import sqlite3
import os
import time
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkfont
from PIL import Image, ImageTk
 
expense =0
income=0
amount=0
 
LARGE_FONT = ("Verdana", 32)

class Authenticate:
    
    def __init__(self, master):
        self.frame = Frame(width=380, height=305, bg="SlateBlue", colormap="new")
        self.frame.pack()
        self.main_window()
        self.treeview=None
         
        self.users = {}  # empty dictionary
        self.loadUsers() # and load the user base    
           
        
    def loadUsers(self):
    # Lofadup all of the usernames and passwords into a dictionary
        with open("LoginDetails.txt", 'r') as f:
            for row in f:
                user, password = row.split(" ")
                password=password.replace("\n","")
                self.users[user] = password # Puts this user & password into the dictionary
                

###MAIN WINDOW###    
        
    def main_window(self):        
      
        self.userNameVar = StringVar()
        self.passwordVar = StringVar()
        self.l1 = Label(self.frame, text="User Name", background='SlateBlue' , width=10,  borderwidth=0,font=("Calibri",18)).grid(row = 15, column = 3 )  
        self.l2 = Label(self.frame, text="Password", background = 'SlateBlue', width=10,  borderwidth=0,font=("Calibri",18)).grid(row = 18, column = 3)
        self.b1=Button(self.frame,text="Login", background='Red',command=self.checkValidUserPass).grid(row = 20, column = 7)
        self.b2=Button(self.frame,text="Create Account", background='Red',command=lambda:(self.Create()) ).grid(row = 20, column = 3)
        self.e1 = Entry(self.frame, textvariable=self.userNameVar,highlightthickness=2,  highlightbackground="#FF4500")
        self.e1.grid(row=15, column=7 )
        self.e1.focus_set()
        self.e2 = Entry(self.frame, textvariable=self.passwordVar, show="*", highlightthickness=2,  highlightbackground="#FF4500" )
        self.e2.grid(row=18, column=7 ) 
        self.i=PhotoImage(file='logo.png')
        Label(self.frame, image=self.i).grid(row = 0, column = 0)
         
 
    def Create(self):
         
        self.l1 = Label(self.frame, text="Enter User Name", background='SlateBlue' , width=20, foreground='gold', borderwidth=0,font=("Calibri",18)).grid(row = 15, column = 3 )  
        self.l2 = Label(self.frame, text="Enter Password", background = 'SlateBlue', width=20,foreground='gold'  ,borderwidth=0,font=("Calibri",18)).grid(row = 18, column = 3)
        self.e1 = Entry(self.frame, textvariable=self.userNameVar,highlightthickness=2,  highlightbackground="#FF4500")
        self.e1.grid(row=15, column=7 )
        self.e2 = Entry(self.frame, textvariable=self.passwordVar, show="*", highlightthickness=2,  highlightbackground="#FF4500" )
        self.e2.grid(row=18, column=7 )
        
        def passwordcheck(user,psswd):
            lower, upper, special, digits = 0, 0, 0, 0   # initialise variables = 0

            '''hi these are comments
            to show that multiple lines can be commented in python
            line3 as an example
            '''
              # below are to validate if password satisfies the conditions
            if (len((psswd)) >= 8):                 # whether my password is having 8 and above characters
                for j in psswd:                   # loops through each and every character in the word   Ex: Ind!@123?
              
                    # counting lowercase alphabets  
                    if (j.islower()):          #islower()      
                        lower+=1            
              
                    # counting uppercase alphabets 
                    if (j.isupper()):         #isupper()
                        upper+=1            
              
                    # counting digits 
                    if (j.isdigit()):         #isdigit()
                        digits+=1            
              
                    # counting the mentioned special characters 
                    if(j=='@'or j=='$' or j=='_' or j=='!' or j=='?'): 
                        special+=1
                        
            if (lower >=1 and upper>=1 and special>=1 and digits>=1):
                print("Valid Password")
                messagebox.showinfo("User Account Creation", "Account Created Successfully!")
                file=open('LoginDetails.txt','a')
                file.write('\n'+user+' ' +psswd)
                file.close()
                                            
            else: 
                print("Invalid Password")
                messagebox.showinfo("User Account Creation", "Please input valid password!")
                
        b=Button(self.frame,text="Create New User Account ", background='Gold',command=lambda:(passwordcheck(self.e1.get(),self.e2.get()))).grid(row = 20, column = 3) 
       
    def confirmExit(self,frame):
            response=messagebox.askquestion('LogOut and Exit', "Do you really want to exit the program?")
           
            if response=='yes':
                 Label(frame,text=response).grid(row=5,column=5)
                 for item in self.frame.winfo_children():
                      item.destroy()
                 exit()
 
            else:
                pass
        
    def logout(self,frame):
       
            response=messagebox.askquestion('LogOut', "Do you really want to log out?")
           
            if response=='yes':
                 Label(frame,text=response).grid(row=5,column=5)
                 for item in self.frame.winfo_children():
                      item.destroy()
                 self.main_window()
 
            else:
                pass
         
    def checkValidUserPass(self):
                
        user = self.userNameVar.get() 
        attemptPassword= self.passwordVar.get()
            
        try:
            realPassword= self.users[user]
            #print(realPassword, 'is realpsswd',attemptPassword, 'is attemptpsswd',user,'is user')
            
            if  str(attemptPassword) == str(realPassword):
                #print('Valid user...')
                self.login()
 
            else:
                print ('Username or password does not match...')

        except KeyError:  # That user name is not in our dictionary of users
            self.invalidUser()

    def invalidUser(self):
        print("Oh! That is a bad username. Please try again!")
        # Turn this into a message box, or other UX
        

    def login(self):
        
         
        top = Toplevel(self.frame,bg="SlateBlue")
        top.geometry('356x250')
        top.title('Main Menu')
        i=PhotoImage(file='logo.png')
        Label(top, image=self.i).grid(row = 1, column = 1)
        l2 = Label(top, text="MAIN MENU", background='SlateBlue', foreground = 'Gold', width=10,  borderwidth=0,font=("Calibri",18)).grid(row = 2, column = 3 )
        b3=Button(top,text="Log Out", background='Red', width=13, command=lambda:(self.logout(top))).place( x=251,y=5)             
        b4=Button(top,text="Log Out and Exit", background='Red' ,width=13,command=lambda:(self.confirmExit(top))).place( x=251,y=40)           
        b5=Button(top,text="Raw Material Details", background='Red' ,width=15, command=self.raw_materials).grid(row = 23, column = 1)
        b6=Button(top,text="Artwork Details", background='Red',width=15, command=self.artwork_details ).grid(row = 23, column = 8)
        b7=Button(top,text="Inventory Level", background='Red' ,width=15,command=self.issued_items).place( x=0,y=200) 
        b8=Button(top,text="Income and Expense", background='Red', width=15, command =self.income ).place( x=237,y=200) 
        
###############    
 
    def insert(self, database, val1, val2, val3, val4):  
        item_name = val1.get()
        quantity = val2.get()
        unit_price = val3.get()
        amount = val4.get()
        insertion = database(item_name, quantity, unit_price, amount)
        return insertion
    def delete(self,database, val1):
        ID= val1       
        deletion = database(ID)
        return deletion
    def fetch(self,database, val1):
        ID= val1.get()           
        selection = database(ID)
        return selection
    def fetchdate(self,database, val1,val2):
        fromdate= val1.get()
        todate=val2.get()
        selection = database(fromdate,todate)
        return selection
 
    def update(self,database, val1,val2,val3,val4,val5):
        item_name = val1.get()
        quantity = val2.get()
        unit_price = val3.get()
        amount = val4.get()
        ID= val5#.get()           
        updation = database(item_name, quantity, unit_price, amount, ID)
        return updation
    
    def insert_art(self, database, val1, val2, val3, val4,val5,val6):
        
        product = val1.get()       
        medium = val2.get()
        artist = val3.get()
        price = val4.get()
        date =val5.get()
        img=val6.cget('image')
        insertion=database(product, medium,artist, price,date,img)
        return insertion
    
    def update_art(self, database, val1, val2, val3, val4,val5,val6):  
        product = val1.get()
        artist = val2.get()
        medium = val3.get()
        price = val4.get()
        status =val5.get()
        ID =val6.get()
        #date =val7.get()
        updation=database(product, artist, medium, price,status,ID)
        return updation
    
    def added(self, boxaile):
        myLabel = Label(boxaile, text="The value has been inserted")
        myLabel.grid(row=5, column=0)
    def deleted(self,boxaile):
        myLabel = Label(boxaile, text="The value was deleted")
        myLabel.grid(row=4, column=0)
        #self.after(3000,lambda: boxaile.destroy())
    def fetched(self, boxaile):
        myLabel = Label(boxaile, text="The value has been fetched successfully")
        myLabel.grid(row=4, column=0)

    def updated(self, boxaile):
        myLabel = Label(boxaile, text="The value has been updated successfully", background='green3')
        myLabel.grid(row=8, column=0)
    def notupdated(self, boxaile):
        myLabel = Label(boxaile, text="No records found for updates")
        myLabel.grid(row=6, column=0)
    def added_art(self, boxaile):
        myLabel = Label(boxaile, text="The value has been inserted")
        myLabel.grid(row=8, column=1)

   

####################

    def incomereport(self):
        
        top = Toplevel(self.frame,  bg="SlateBlue" )
        top.geometry('880x360')
        i=PhotoImage(file='logo.png')
        Label(top, image=self.i).grid(row=0,column=0)       
        l1 = Label(top, text="Income Report", background='SlateBlue', foreground = 'Gold', width=20,  borderwidth=0,font=("Calibri",18)).place(x=290,y=20) 


        a=Label(top, width=20, borderwidth = 3, relief='groove',text='Product Id', background='green3')
        a.grid (row=15, column =1)
        b=Label(top, width=20,borderwidth = 3, relief='groove',  text='Product Name', background='green3')
        b.grid (row=15, column =2)
        c=Label(top, width=20,borderwidth = 3, relief='groove', text='Artist Name', background='green3')
        c.grid (row=15, column =3)
        d=Label(top, width=20,borderwidth = 3, relief='groove',  text='Medium Used', background='green3')
        d.grid (row=15, column =4)
        e=Label(top, width=20,borderwidth = 3, relief='groove',  text='Product Price', background='green3')
        e.grid (row=15, column =5)
        j=1
        i=15
        result=db_art.select_trv_artwork1().fetchall()
        if result !=[]:
            
            for record in result:          
                for j in range (5):# for the 6 columns to display from artworkdetails                
                    e = Label(top, width=20, borderwidth = 3, relief="flat", text=record[j],pady=5)   
                    e.grid(row=i+1, column=j+1) 
                i=i+1
            g = Label(top, width=16, borderwidth = 1, relief="flat",text='Total Income',pady=5, font=('Arial',12),fg='blue') 
            g.grid(row=i+1,column=j-3)
            g1 = Label(top, width=16, borderwidth = 1, relief="flat",text=' ',pady=5, font=('Arial',12),fg='blue') 
            g1.grid(row=i+1,column=j-2)
            g2 = Label(top, width=16, borderwidth = 1, relief="flat",text=' ',pady=5, font=('Arial',12),fg='blue') 
            g2.grid(row=i+1,column=j-1)
            g3 = Label(top, width=16, borderwidth = 1, relief="flat",text=' ',pady=5, font=('Arial',12),fg='blue') 
            g3.grid(row=i+1,column=j)
            h = Label(top, width=16, borderwidth = 1, relief="flat", text=income,  pady=5, font=('Arial',12),fg='blue')
            h.grid(row=i+1,column=j+1)
        else:
            g = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g.grid(row=i+1,column=j)
            g1 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g1.grid(row=i+1,column=j+1)
            g2 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g2.grid(row=i+1,column=j+2)
            g3 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g3.grid(row=i+1,column=j+3)
            g4 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g4.grid(row=i+1,column=j+4)
            h= Label(top, width=20, borderwidth = 3, relief="flat", text='Total Income',pady=5 )
            h.grid(row=i+2,column=j)
            #k= Label(top, width=20, borderwidth = 3, relief="flat", text='0',pady=5,background='slateblue',foreground = 'Gold')
            k= Label(top, width=20, borderwidth = 3, relief="flat", text='0',pady=5)
            k.grid(row=i+2,column=j+4)
            
####################

    def artworkstatusreport(self):
        
        top = Toplevel(self.frame,  bg="SlateBlue", colormap="new")
        top.geometry('1150x400')
        i=PhotoImage(file='logo.png')
        Label(top, image=self.i).grid(row=0,column=0)         
        l1 = Label(top, text="ArtWork Status Report", background='SlateBlue', foreground = 'Gold', width=20,  borderwidth=0,font=("Calibri",18)).place(x=450,y=20) 

        a=Label(top, width=20, borderwidth = 3, relief="groove",text='ID', background='green3')
        a.grid (row=15, column =2)
        b=Label(top, width=20,borderwidth = 3, relief="groove", text='Product', background='green3')
        b.grid (row=15, column =3)
        c=Label(top, width=20,borderwidth = 3, relief="groove", text='Artist', background='green3')
        c.grid (row=15, column =4)
        d=Label(top, width=20,borderwidth = 3, relief="groove", text='Medium Used', background='green3')
        d.grid (row=15, column =5)
        e=Label(top, width=20,borderwidth = 3, relief="groove", text='Price', background='green3')
        e.grid (row=15, column =6)
        f=Label(top, width=20,borderwidth = 3, relief="groove", text='Status', background='green3')
        f.grid (row=15, column =7)
 
        #j=1
        i=15
        result=db_art.select_trv_artwork().fetchall()
        if result !=[]:
            
            for record in result:          
                for j in range (6):# for the 6 columns to display from artworkdetails                
                    e = Label(top, width=20, borderwidth = 3, relief="flat", text=record[j],pady=5)   
                    e.grid(row=i+1, column=j+2) 
                i=i+1
 
        else:
            g = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g.grid(row=i+1,column=j+1)
            g1 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g1.grid(row=i+1,column=j+2)
            g2 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g2.grid(row=i+1,column=j+3)
            g3 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g3.grid(row=i+1,column=j+4)
            g4 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g4.grid(row=i+1,column=j+5)
            g5 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g5.grid(row=i+1,column=j+6)
            g6 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g6.grid(row=i+1,column=j+7)
        
 
            #######
         
    def raw_materials(self):
        
        top = Toplevel(self.frame,  bg="SlateBlue")
        top.geometry('1300x440')
        scrollbar = Scrollbar(top, orient=VERTICAL)
        self.treeview = ttk.Treeview(top,yscrollcommand=scrollbar.set,columns=("ID","Itemname","quantity","unit","amount"), show='headings', height='12')
        style=ttk.Style()
        style.configure('Treeview.Heading', background="green3")
        i=PhotoImage(file='logo.png')
        Label(top, image=self.i).place (x=0, y =0)
        b1 = Button(top, text='Main Menu', background='Red',command=self.login).place(x=120,y=0) 
        l1 = Label(top, text="Raw Material Details", background='SlateBlue', foreground = 'Gold', width=40,  borderwidth=0,font=("Calibri",18)).pack(side=TOP )
        l2 = Label(top, text="Period:", background='SlateBlue', width=7, font=("Calibri",18)).place(x=650,y=35)
        ep=Entry(top)
        ep.place(x=750,y=40)
        l3 = Label(top, text="To:", background='SlateBlue', width=3,  font=("Calibri",18)).place(x=960,y=35)
        et=Entry(top)
        et.place(x=1000,y=40)       
        self.treeview.heading('ID',text='ID' )
        self.treeview.heading('Itemname',text='Item Name')
        self.treeview.heading('quantity',text='Quantity')
        self.treeview.heading('unit',text='Unit')
        self.treeview.heading('amount',text='Amount')
        font = tkfont.nametofont('TkTextFont')
        font.configure(size=12, slant='roman')
        self.treeview.tag_configure('TkTextFont', font=tkfont.nametofont('TkTextFont'))
        self.treeview.tag_configure('color',foreground='blue')

        result=db_art.select_trv().fetchall()
        global total
        total =0
        for x in result:
            self.treeview.insert('', 'end', values=x)
        for child in self.treeview.get_children():
            total += float(self.treeview.item(child, 'values')[4])
        self.treeview.insert('', 'end',  text='Total', tags=('TkTextFont',  'color', 'bg'),values =('','','','Total Expense',total))
        scrollbar.config(command=self.treeview.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.treeview.place(x=200,y=100)
        def dateselect(e1,e2):
            total1=0
            if (len(e1)  == 0 and len(e2) != 0 ) or ( len(e1) !=0 and len(e2) ==0) or (len(e2) ==0 and len(e1) ==0):
                  messagebox.showinfo("Raw Materials report", "Enter a valid date range!")
            else:
                  for item in self.treeview.get_children(): #removing old data view
                      self.treeview.delete(item)
                  result=db_art.select_trv1(e1 ,e2).fetchall()                 
                  for x in result:
                    self.treeview.insert('', 'end', values=x)
                  for item in self.treeview.get_children():
                    total1 += float(self.treeview.item(item, 'values')[4])
                    
            self.treeview.insert('', 'end',  text='Total', tags=('TkTextFont',  'color', 'bg'),values =('','','','Total Expense',total1))
        
        top.bind('<Return>', lambda event: (top.config(bg='SlateBlue'), self.fetchdate(dateselect,ep,et)))
              
        b2 = Button(top, text='ADD', width=6, background='Red',command=self.insert_data).place(x=200,y=380)
        b3 = Button(top, text='UPDATE', width=8, background='Red',command=self.update_data).place(x=280,y=380) 
        b4 = Button(top, text='DELETE', width=8, background='Red', command=self.delete_data).place(x=380,y=380) 
        #b5=Button(top, text='Fetch', background='Red',command=lambda:(self.fetchdate(dateselect,ep,et))).pack(side=TOP, padx=3, pady=4)
        
    def raw_materials_report(self):
        
        top = Toplevel(self.frame,  bg="SlateBlue")
        top.geometry('1200x300')
        scrollbar = Scrollbar(top, orient=VERTICAL)
        self.treeview = ttk.Treeview(top,yscrollcommand=scrollbar.set,columns=("ID","Itemname","quantity","unit","amount"), show='headings', height='6')
        i=PhotoImage(file='logo.png')
        Label(top, image=self.i).place (x=0, y =0)
       
        l1 = Label(top, text="Raw Material Expense Report", background='SlateBlue', foreground = 'Gold', width=40,  borderwidth=0,font=("Calibri",18)).place(x=400,y=20)
       
        self.treeview.heading('ID',text='ID')
        self.treeview.heading('Itemname',text='Item name')
        self.treeview.heading('quantity',text='Quantity')
        self.treeview.heading('unit',text='Unit Price')
        self.treeview.heading('amount',text='Amount')
        total=0
        result=db_art.select_trv_closing().fetchall()

        for x in result:
            self.treeview.insert('', 'end', values=x)

         
        scrollbar.config(command=self.treeview.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.treeview.place(x=150,y=100)
        
         
    def issued_items(self):
        
        top = Toplevel(self.frame,  bg="SlateBlue", colormap="new")
        top.geometry("1400x300")
        scrollbar = Scrollbar(top, orient=VERTICAL)
        self.treeview = ttk.Treeview(top,yscrollcommand=scrollbar.set,columns=("ID","Itemname","quantityissued","unit","amount"), show='headings', height='6')
        style=ttk.Style()
        style.configure('Treeview.Heading', background="green3")
        font = tkfont.nametofont('TkTextFont')
        font.configure(size=12, slant='roman')
        self.treeview.tag_configure('TkTextFont', font=tkfont.nametofont('TkTextFont'))
        self.treeview.tag_configure('color', foreground='blue')        

        i=PhotoImage(file='logo.png')
        Label(top, image=self.i).pack(side=TOP, anchor=W)
        l1 = Label(top, text="Issued Items Details", background='SlateBlue', foreground = 'Gold', width=22,  borderwidth=0,font=("Calibri",18)).place(x=530,y=20) 
        l2 = Label(top, text="Period:", background='SlateBlue', width=7, font=("Calibri",18)).place(x=650,y=60)
        ep=Entry(top)
        ep.place(x=750,y=60)
        l3 = Label(top, text="To:", background='SlateBlue', width=3,  font=("Calibri",18)).place(x=968,y=60)
        et=Entry(top)
        et.place(x=1000,y=60)   
        self.treeview.heading('ID',text='ID')
        self.treeview.heading('Itemname',text='Item Name')
        self.treeview.heading('quantityissued',text='Quantity Issued')
        self.treeview.heading('unit',text='Unit Price')
        self.treeview.heading('amount',text='Amount')
        result=db_art.select_trv_issued().fetchall()
        total=0
        for x in result:
              self.treeview.insert('', 'end', values=x)  # populates rows from table
        for child in self.treeview.get_children():
            total += float(self.treeview.item(child, 'values')[4])
        self.treeview.insert('', 'end',  text='Total', tags=('TkTextFont',  'color', 'bg'),values =('','','','Total ',total))
        scrollbar.config(command=self.treeview.yview)        
        scrollbar.pack(side=RIGHT, fill=Y)        
        self.treeview.place(x=200,y=100) 
        
        def dateselect(e1,e2):
            total=0
            if (len(e1)  == 0  and len(e2) ==0):
                  for item in self.treeview.get_children(): #removing old data view
                      self.treeview.delete(item)
                  result=db_art.select_trv_issued().fetchall()                 
                  for x in result:
                    self.treeview.insert('', 'end', values=x)
                 
                    total = total + int(x[4])
                    
                  self.treeview.insert('', 'end',  text='Total', tags=('TkTextFont',  'color', 'bg'),values =('','','','Total ',total))
 
            elif(len(e1)  != 0 and len(e2) != 0 ):
                  for item in self.treeview.get_children(): #removing old data view
                      self.treeview.delete(item)
                  result=db_art.select_trv_issued_date(e1 ,e2).fetchall()
                  for x in result:
                    self.treeview.insert('', 'end', values=x)
            else:
                 messagebox.showinfo("Issued Item Details", "Enter a valid from and to date!")
                
        
        top.bind('<Return>', lambda event: (top.config(bg='SlateBlue'), self.fetchdate(dateselect,ep,et)))
        b1 = Button(top, text='Main Menu', background='Red', command=self.login).place(x=120,y=10) 
        b2 = Button(top, text='UPDATE', background='Red',command=self.update_issued).place(x=205,y=271) 
        b3 = Button(top, text='CLOSING BALANCE DETAILS', command=lambda:(self.closing_balance()), background='Red').place(x=1040,y=271)

    def closing_balance(self):

        i=PhotoImage(file='logo.png')
        top = Toplevel(self.frame,  bg="SlateBlue") 
        top.geometry("900x540")
        Label(top, image=self.i).grid(row=0,column=0) 
        l1 = Label(top, text="Closing Balance Details", background='SlateBlue', foreground = 'Gold', width=40,  borderwidth=0,font=("Calibri",18)).place(x=250,y=20)
      
        a=Label(top, width=20, borderwidth = 3, relief='groove', text='Id', background='green3')
        a.grid (row=15, column =1)
        b=Label(top, width=20,borderwidth = 3, relief='groove',  text='Item Name', background='green3')
        b.grid (row=15, column =2)
        c=Label(top, width=20,borderwidth = 3, relief='groove',  text='Quantity', background='green3')
        c.grid (row=15, column =3)
        d=Label(top, width=20,borderwidth = 3, relief='groove',  text='Unit Price', background='green3')
        d.grid (row=15, column =4)
        e=Label(top, width=20,borderwidth = 3, relief='groove',  text='Amount', background='green3')
        e.grid (row=15, column =5)        
        j=1
        i=15
        result=db_art.select_trv_closing().fetchall()         
        if result !=[]:
            sum_a = 0             
            for record in result:
                sum_a = sum_a + int(record[4])
                for j in range (5):# for the 5 columns to display from the join on artworkdetails and issued_items       
                    e = Label(top, width=20, borderwidth = 3, relief="flat", text=record[j],pady=5)   
                    e.grid(row=i+1, column=j+1) 
                i=i+1
            g = Label(top, width=16, borderwidth = 1, relief="flat", text='Total',pady=5, font = ("Arial", 12),fg='blue')
            g.grid(row=i+1,column=j-3)
            g1 = Label(top, width=16, borderwidth = 1, relief="flat",text=' ',pady=5, font=('Arial',12),fg='blue') 
            g1.grid(row=i+1,column=j-2)  
            g2 = Label(top, width=16, borderwidth = 1, relief="flat",text=' ',pady=5, font=('Arial',12),fg='blue') 
            g2.grid(row=i+1,column=j-1)
            g3 = Label(top, width=16, borderwidth = 1, relief="flat",text=' ',pady=5, font=('Arial',12),fg='blue') 
            g3.grid(row=i+1,column=j)
            h = Label(top, width=16, borderwidth = 1, relief="flat", text=sum_a, pady=5,font = ("Arial",12) ,fg='blue')
            h.grid(row=i+1,column=j+1)
        else:
            g = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g.grid(row=i+1,column=j)
            g1 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g1.grid(row=i+1,column=j+1)
            g2 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g2.grid(row=i+1,column=j+2)
            g3 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g3.grid(row=i+1,column=j+3)
            g4 = Label(top, width=20, borderwidth = 3, relief="flat", text='      ',pady=5)
            g4.grid(row=i+1,column=j+4)
            h= Label(top, width=800, borderwidth = 3, relief="flat", text='Total ',pady=5)
            h.grid(row=i+2,column=j)
            k= Label(top, width=20, borderwidth = 3, relief="flat", text='0',pady=5)
            k.grid(row=i+2,column=j+4)
            

        b1 = Button(top, text='Main Menu', background='Red',command=self.login).place(x=120,y=0)
        b2 = Button(top, text='Print Raw Material Expense Report', background='Red',command=self.raw_materials_report ).place(x=660,y=500)

      ##### #####

    def additionalexpense(self):


        top = Toplevel(self.frame,  bg="SlateBlue")
        top.geometry('770x400')
        i=PhotoImage(file='logo.png')
        Label(top, image=self.i).grid(row=0, column=0)
        l1 = Label(top, text="Additional Expense Details", background='SlateBlue', foreground = 'Gold', width=28,  borderwidth=0,font=("Calibri",18)).place(x=250,y=30)
        
        a=Label(top, width=30, borderwidth = 4, relief='groove', text='Expense_ID', background='green3',fg='black', height=-3)
        a.grid (row=1, column =1)
        b=Label(top, width=30,borderwidth = 4, relief='groove', text='Type', background='green3',fg='black', height=-3)
        b.grid (row=1, column =2) 
        c=Label(top, width=30, borderwidth = 4, relief='groove', text='Cost', background='green3',fg='black', height=-3)
        c.grid (row=1, column =3) 
        i=1   # row setup
        result=db_art.select_trv_artwork4().fetchall()             
        for record in result:          
            for j in range (3):# for the three columns to display from expenses                
                e = Label(top, width=30, borderwidth = 4,  text=record[j], fg='black', height=-3,pady=5)   
                e.grid(row=i+1, column=j+1) 
               # e.insert(END, record[j])
            i=i+2

        result=db_art.select_trv_artwork5().fetchall()
        global expense
        expense = result[0][0]    
       
        def showexpense():
            m=Label(top, width=23, borderwidth = 5, text='Total Expense', fg='blue',   font = ('Arial', 11) )
            m.grid(row=i+2,column=1 )         
            d=Label(top, width=23, borderwidth = 5, text='',fg='blue' , font = ('Arial', 11) )
            d.grid(row=i+2,column=2)
                   
            for x in result:
               e=Label(top, width=23,borderwidth = 5, text=x, fg='blue', font = ('Arial', 11)  )
               e.grid(row=i+2,column =3 )
        
         
        b1 = Button(top, text='Main Menu', background='Red',command=self.login).place(x=120,y=5)
        b2 = Button(top, text='Previous', background='Red' ,width=15,command=self.income).place(x=150, y=350) 
        b3 = Button(top, text='Next', background='Red' ,width=15,command=self.finalincomeexpense).place(x=370, y=350) 

        b4 = Button(top, text='Calculate', background='Red' ,width=15,command=lambda:(showexpense())).place(x=590, y=350) 
       
            
         #######
        

    def finalincomeexpense(self):
  

        top = Toplevel(self.frame,  bg="SlateBlue", colormap="new")
        top.geometry('600x300')
        i=PhotoImage(file='logo.png')
        Label(top, image=self.i).grid(row=0, column=0)
        l1 = Label(top, text="Income and Expense Details", background='SlateBlue', foreground = 'Gold', width=28,  font=("Calibri",18)).place(x=190,y=30)#grid (row=2, column =3)
       
        a=Label(top, width=30, borderwidth = 3, text='Total Income', background='green3',fg='black', height=-3)
        a.grid (row=1, column =1) 
        b=Label(top, width=30,borderwidth = 3,  text='less Total Expenses', background='green3',fg='black', height=-3)
        b.grid (row=2, column =1) 
        c=Label(top, width=30, borderwidth = 3, text='Raw Material Expense', background='green3',fg='black', height=-3)
        c.grid (row=3, column =1) 
        d=Label(top, width=30, borderwidth = 3, text='add Additional Expenses', background='green3',fg='black', height=-3)
        d.grid (row=4, column =1) 
        e=Label(top, width=27,  text='Output', background='green3',fg='blue' , borderwidth = 0,  font = ('Helvetica', 10) )
        e.grid(row=5,column=1)
        r=Label(top, width=27,  text=' ',  borderwidth = 0,  font = ('Helvetica', 10) )
        r.grid(row=5,column=2)


        result =db_art.select_trv_artwork6().fetchall()
        amount=result[0][0]

        a_ =Label(top, width=30, borderwidth = 3, text=income,   height=-3)
        a_.grid (row=1, column =2) 
        b_ =Label(top, width=30, borderwidth = 3, text=expense+amount, height=-3)
        b_.grid (row=2, column =2) 
        c_ =Label(top, width=30, borderwidth = 3, text=amount,   height=-3)
        c_.grid (row=3, column =2)
        d_ =Label(top, width=30, borderwidth = 3, text=expense,   height=-3)
        d_.grid (row=4, column =2) 
        
        
        def showincomeexpense():
 
              
            totalexpense = income-(expense+amount)
            e_=Label(top, width=27, text=totalexpense,  fg='blue' , borderwidth = 0,  font = ('Helvetica', 10) ) 
            e_.grid(row=5,column =2)                
     
        b1 = Button(top, text='Main Menu', background='Red',command=self.login).place(x=120,y=0)
        b2 = Button(top, text='Previous', background='Red',command=self.additionalexpense).place(x=110, y=250)#grid (row=7, column =0)
        b3 = Button(top, text='Calculate', background='Red', command=lambda:(showincomeexpense()) ).place(x=190, y=250)#grid (row=7, column =1)
        b4 = Button(top, text='Print Total Expense Report', background='Red' ,command=self.totalexpensereport).place(x=270, y=250)#grid (row=7, column =2)       
        b5 = Button(top, text='Print Output Report', background='Red' ,command=self.incomeexpensereport).place(x=450, y=250)#grid (row=7, column =3)

        

        ###########

    def incomeexpensereport(self):
  

            top = Toplevel(self.frame,  bg="SlateBlue", colormap="new")
            top.geometry('600x300')
            i=PhotoImage(file='logo.png')
            Label(top, image=self.i).grid(row=0, column=0)
            l1 = Label(top, text="Income and Expense Report", background='SlateBlue', foreground = 'Gold', width=28,  borderwidth=0,font=("Calibri",18)).place(x=190,y=30)#grid (row=2, column =3)
           
            a=Label(top, width=30, borderwidth = 3, text='Total Income',  fg='blue', height=-3)
            a.grid (row=1, column =1) 
            b=Label(top, width=30,borderwidth = 3,   text='less Total Expenses',  fg='blue', height=-3)
            b.grid (row=2, column =1) 
            c=Label(top, width=30, borderwidth = 3,  text='Raw Material Expense',  fg='blue', height=-3)
            c.grid (row=3, column =1) 
            d=Label(top, width=30, borderwidth = 3,  text='add Additional Expenses',  fg='blue', height=-3)
            d.grid (row=4, column =1) 
            e=Label(top, width=30, borderwidth = 3, text='Total Income/Expense Report',  fg='blue', height=-3)
            e.grid(row=5,column=1)

            result =db_art.select_trv_artwork6().fetchall()
            amount=result[0][0]

            a_ =Label(top, width=30, borderwidth = 3,  text=income,   height=-3)
            a_.grid (row=1, column =2) 
            b_ =Label(top, width=30, borderwidth = 3,  text=expense+amount, height=-3)
            b_.grid (row=2, column =2) 
            c_ =Label(top, width=30, borderwidth = 3,  text=amount,   height=-3)
            c_.grid (row=3, column =2)
            d_ =Label(top, width=30, borderwidth = 3,  text=expense,   height=-3)
            d_.grid (row=4, column =2) 
                  
            totalexpense = income-(expense+amount)
            if totalexpense >0:
                e_=Label(top, width=30, text=totalexpense, background='green3',  height=-3)
                e_.grid(row=5,column =2)
            else:
                e_=Label(top, width=30, text=totalexpense, background='red',  height=-3)
                e_.grid(row=5,column =2)

            
         
    def totalexpensereport(self):
          

        top = Toplevel(self.frame,  bg="SlateBlue", colormap="new")
        top.geometry('770x400')
        i=PhotoImage(file='logo.png')
        Label(top, image=self.i).grid(row=0, column=0)
        l1 = Label(top, text="Total Expense Report", background='SlateBlue', foreground = 'Gold', width=28,  borderwidth=0,font=("Calibri",18)).place(x=250,y=30) 
       
        a=Label(top, width=30, borderwidth = 4, text='Expense_ID', relief='groove',background='green3',fg='black', height=-3)
        a.grid (row=1, column =1)
        b=Label(top, width=30,borderwidth = 4,  text='Type', relief='groove', background='green3',fg='black', height=-3)
        b.grid (row=1, column =2) 
        c=Label(top, width=30, borderwidth = 4, text='Cost',relief='groove', background='green3',fg='black', height=-3)
        c.grid (row=1, column =3) 
       
        
       
        i=1   # row setup
        sum_a=0
        result=db_art.select_trv_artwork4().fetchall()             
        for record in result:
            sum_a =sum_a+int(record[2])
            
            for j in range (3):# for the three columns to display from expenses                
                e = Label(top, width=30, borderwidth = 4,  text=record[j], fg='black', height=-3,pady=5)   
                e.grid(row=i+1, column=j+1) 
               # e.insert(END, record[j])
            i=i+2



        result=db_art.select_trv().fetchall()
        total =0
    

        for record in result:
                total = total + int(record[4])
        d=Label(top, width=30, borderwidth = 4, text='6',fg='black', height=-3,pady=5)
        d.grid(row=i+1,column=j-1)
        f=Label(top, width=30, borderwidth = 4, text='Raw Material',fg='black', height=-3,pady=5)
        f.grid(row=i+1,column=j)
        g=Label(top, width=30, borderwidth = 4, text= total,fg='black', height=-3,pady=5)
        g.grid(row=i+1,column=j+1)
        m=Label(top, width=30, borderwidth = 4, text= 'Total Expenses', foreground='blue', font=('Arial',9),pady=5,height=-3)
        
        m.grid(row=i+2,column=j-1)
        h=Label(top, width=30, borderwidth = 4,text= '',fg='black',font=('Arial',9), pady=5,height=-3)
        h.grid(row=i+2,column=j)
        k=Label(top, width=30, borderwidth = 4, text= total+sum_a,fg='blue',  font=('Arial',9),pady=5,height=-3)
        k.grid(row=i+2,column=j+1)


        ##############
        
    def artwork_details(self):
        
        top = Toplevel(self.frame,  bg="SlateBlue" )
        top.geometry('1425x303')
        
        scrollbar = Scrollbar(top, orient=VERTICAL)
        self.treeview = ttk.Treeview(top,yscrollcommand=scrollbar.set,columns=("id","item","artist","medium","pprice","status"), show='headings', height='6')
        i=PhotoImage(file='logo.png')        
        Label(top, image=self.i).pack(side=TOP, anchor=W)    
        b1 = Button(top, text='Main Menu', background='Red',command=self.login).place (x=120,y=10) 
        l1 = Label(top, text="ArtWork Details", background='SlateBlue', foreground = 'Gold', width=18,  font=("Calibri",18)).place (x=580,y=10)
        l2 = Label(top, text="Period:", background='SlateBlue', width=7, font=("Calibri",18)).place(x=750,y=46)
        l3 = Label(top, text="To:", background='SlateBlue', width=7, font=("Calibri",18)).place(x=960,y=46)

        e1=Entry(top)
        e1.place(x=850,y=55)
        e2=Entry(top)
        e2.place(x=1050,y=55)
        self.treeview.heading('id',text='ProductId')
        self.treeview.heading('item',text='Item Name')
        self.treeview.heading('artist',text='Artist Name')
        self.treeview.heading('medium',text='Medium Used')
        self.treeview.heading('pprice',text='Product Price')
        self.treeview.heading('status',text='Status')
        result=db_art.select_trv_artwork().fetchall()
        for x in result:
            self.treeview.insert('', 'end', values=x)
        def dateselect1(e1,e2):
           
            if (len(e1)  == 0 and len(e2) == 0 ):
                  for item in self.treeview.get_children(): #removing old data view
                      self.treeview.delete(item)
                  result=db_art.select_trv_artwork().fetchall()
                  for x in result:
                    self.treeview.insert('', 'end', values=x)
                   
            elif(len(e1)  != 0 and len(e2) != 0 ):
                  for item in self.treeview.get_children(): #removing old data view
                      self.treeview.delete(item)
                  result=db_art.select_trv_artwork_date(e1 ,e2).fetchall()                 
                  for x in result:
                    self.treeview.insert('', 'end', values=x)


            else:
                messagebox.showinfo("ArtWork Details report", "Enter a valid date!")
                
        top.bind('<Return>', lambda event: (top.config(bg='SlateBlue'), self.fetchdate(dateselect1,e1,e2)))
                
        scrollbar.config(command=self.treeview.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.treeview.place (x=200,y=100) 
        b2 = Button(top, text='INPUT', background='Red',width = 10, command=self.insert_artwork).place (x=200,y=271) 
        b3 = Button(top, text='UPDATE', background='Red',width = 12, command=self.update_artwork).place (x=350,y=271) 
        b4 = Button(top, text='DELETE', background='Red', width = 12, command=self.delete_artwork).place (x=500,y=271) 
        b5 = Button(top, text='Print Status Report', background='Red', width = 30, command=self.artworkstatusreport).place (x=1180,y=271) 
        
        #####################

    def income(self):
        
        global income
        top = Toplevel(self.frame,  bg="SlateBlue" )
        top.title('Income Details')
        top.geometry("650x400")
        scrollbar = Scrollbar(top, orient=VERTICAL)
        self.treeview = ttk.Treeview(top,yscrollcommand=scrollbar.set,columns=("id","pprice"), show='headings', height='6')
        style=ttk.Style()
        style.configure('Treeview.Heading', background="green3")
        i=PhotoImage(file='logo.png')
        Label(top, image=self.i).place(x=0,y=0)
        lb = Label(top, text="Product Status : SOLD", background='SlateBlue', width=20, font=("arial italic",13)).place(x=390,y=58)
        b1 = Button(top, text='Main Menu', background='Red',command=self.login).place(x=120,y=0)
        
        l1 = Label(top, text="Income Details", background='SlateBlue', foreground = 'Gold', width=16, font=("Calibri",18)).place(x=290,y=15) 


        self.treeview.heading('id',text='ProductId')
        self.treeview.heading('pprice',text='Product Price')
 
        result=db_art.select_trv_artwork2().fetchall()
        for x in result:
            self.treeview.insert('', 'end', values=x)
             
        scrollbar.config(command=self.treeview.yview)
        self.treeview.tag_configure('TkTextFont', font=tkfont.nametofont('TkTextFont'),  background="SlateBlue")
        self.treeview.tag_configure('color',foreground='blue')
        
        self.treeview.place(x=200,y=100) #pack(side=TOP,anchor=S,fill=X)
       
        scrollbar.pack(side=RIGHT, fill=Y)
        result=db_art.select_trv_artwork3().fetchall()
        font = tkfont.nametofont('TkTextFont')
        font.configure(size=12, slant='roman')

         
        income = result[0][0]
        if type(None) ==type( income):
            income=0             
        def showincome():
            total=0
            for x in result:               
              if type(None) ==type(x[0]):   # x is a tuple of records from database      
                  self.treeview.insert('', 'end',  text='Total' , tags=('TkTextFont','color'), values =('Total Income',0))                     
              else:
                  for child in self.treeview.get_children():
                      if self.treeview.item(child)['text'] =='Total':                            
                          self.treeview.delete(child)            #delete display of total in treeview if exists prior to recalculation 
                      total=db_art.select_trv_artwork3().fetchall()        
                  self.treeview.insert('', 'end',  text='Total' , tags=('TkTextFont',  'color'),values =('Total Income',total))    #tags='TkTextFont',                
                
        b4 = Button(top, text='Next', background='Red' ,command =self.additionalexpense).place(x=570, y=350)
        b3 = Button(top, text='Print Income Report', background='Red' ,command = lambda:(self.incomereport())).place(x=490, y=310) 
        b2 = Button(top, text='CALCULATE', background='Red' ,command=lambda:(showincome())).place(x=530, y=270) 

        
##########
       
    def insert_data(self):
        top = Toplevel(self.frame,  bg="SlateBlue", colormap="new")
        top.title('Add Raw Materials')
        style=ttk.Style()
        style.configure('Treeview.Heading', background="green3")
 
        l1 = Label(top, text="Name of item").grid(row = 1, column = 0, sticky = W, pady = 2)
        l2 = Label(top, text="Quantity").grid(row = 2, column = 0, sticky = W, pady = 2)
        l3 = Label(top, text="Unit price").grid(row = 3, column = 0, sticky = W, pady = 2)
        l4 = Label(top, text="Amount").grid(row = 4, column = 0, sticky = W, pady = 2)
        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)
        e4 = Entry(top)
        e4.grid(row=4, column=1, sticky=W, pady=2)
 
        
        
        def insert_raw_view():
            total1=0
            for item in self.treeview.get_children(): #removing old data view
              self.treeview.delete(item)
               
            result=db_art.select_trv().fetchall()
            for x in result:
                self.treeview.insert('', 'end', values=x)  # populates all revised rows from table
            for child in self.treeview.get_children():
                total1 += float(self.treeview.item(child, 'values')[4])
            self.treeview.insert('', 'end',  text='Total', tags=('TkTextFont',  'color', 'bg'),values =('','','','Total Expense',total1))
     
        #BUTTONS###
        B1 = Button(top, text="Insert Values", command=lambda: (top.config(bg='SlateBlue'), self.insert(db_art.insert_raw_materials,e1,e2,e3,e4), self.added(top),insert_raw_view()))  
        B1.grid(row=1, column=2)
       
              
    def delete_data(self):
        total=0
        top = Toplevel(self.frame,  bg="SlateBlue", colormap="new")
        top.title('Delete Raw Materials')

        try:
            selected_item = self.treeview.selection()[0]
           
        
            for item in self.treeview.get_children(): #removing old data view
                if  selected_item == item: 
                    ID= (self.treeview.item(item).get('values')[0])  # extract record from dictionary to be deleted
                    #self.treeview.delete(item)
                    self.delete(db_art.delete_raw_materials,str(ID))
                    self.deleted(top)

            for item in self.treeview.get_children(): #removing old data view
                self.treeview.delete(item)
            result=db_art.select_trv().fetchall()
            for x in result:
                self.treeview.insert('', 'end', values=x)  # populates all revised rows from table
            for item in self.treeview.get_children():
                    total += float(self.treeview.item(item, 'values')[4])
                    
            self.treeview.insert('', 'end',  text='Total', tags=('TkTextFont',  'color', 'bg'),values =('','','','Total Expense',total))

            
                    
        except:
            Label(top,text="Select a raw material to be deleted",background='slateblue',height=10,foreground = 'Gold').grid(row=10, column=2, sticky=W, pady=2)
            
        
             
    def update_data(self):
         top = Toplevel(self.frame,  bg="SlateBlue", colormap="new", width=100, height=200)
         top.title('Update Raw Materials')
         l1 = Label(top, text="Enter the ID of the item").grid(row = 1, column = 0, sticky = W, pady = 2)
         e1 = Entry(top)
         e1.grid(row=1, column=1, sticky=W, pady=2)
          
         B1 = Button(top, text="Fetch Records", command=lambda:(top.config(bg='SlateBlue'),self.fetch(self.update_data_sub,e1),top.destroy()))                        
         B1.grid(row=1, column=2)

    def update_data_sub(self, ID):

         top = Toplevel(self.frame,  bg="SlateBlue", colormap="new")
         top.title('Update Raw Materials Records')
         try:
             row = self.treeview.selection()[0]
         except:
            #print('no record selected')
            pass
         result=(db_art.select_raw_material(ID)).fetchall()
         if result == []:
             self.notupdated(top)
         else:
             
             l0 = Label(top, text="Item ID").grid(row = 1, column = 0, sticky = W, pady = 2)
             l1 = Label(top, text="Item Name").grid(row = 2, column = 0, sticky = W, pady = 2)
             l2 = Label(top, text="Quantity").grid(row = 3, column = 0, sticky = W, pady = 2)
             l3 = Label(top, text="Unit Price").grid(row = 4, column = 0, sticky = W, pady = 2)
             l4 = Label(top, text="Amount").grid(row = 5, column = 0, sticky = W, pady = 2)
             e0=Entry(top,state='disabled')
             e0.grid(row=1, column=1, sticky=W, pady=2)
             e1 = Entry(top)
             e1.grid(row=2, column=1, sticky=W, pady=2)
             e2 = Entry(top)
             e2.grid(row=3, column=1, sticky=W, pady=2)
             e3 = Entry(top)
             e3.grid(row=4, column=1, sticky=W, pady=2)
             e4 = Entry(top)
             e4.grid(row=5, column=1, sticky=W, pady=2)
                 
             for record in result:
                # e0.insert(0,record[0])
                 e1.insert(0,record[1])
                 e2.insert(0,record[2])
                 e3.insert(0,record[3])
                 e4.insert(0,record[2]*record[3])
                 
             def update_raw_view():
                   total=0

                   result=(db_art.select_raw_material(ID)).fetchall()
                   if int(e4.get()) != (int(e2.get())*int(e3.get())):
                       messagebox.showinfo("Raw Material Update", "Invalid Amount entered!")
                   else:
                       for item in self.treeview.get_children(): #removing old data view
                          self.treeview.delete(item)
                       self.update(db_art.update_raw_materials,e1,e2,e3,e4,record[0])
                       self.updated(top)
               
                       result=db_art.select_trv().fetchall()
                       for x in result:
                           self.treeview.insert('', 'end', values=x)  # populates all revised rows from table
                       for child in self.treeview.get_children():
                           total += float(self.treeview.item(child, 'values')[4])
                       self.treeview.insert('', 'end',  text='Total', tags=('TkTextFont',  'color', 'bg'),values =('','','','Total Expense',total))

            
                       
             B1 = Button(top, text="Save Record", command=lambda: (top.config(bg='SlateBlue'), update_raw_view())).grid(row=1, column=2)
                   
        
####################
    def update_issued(self):
         top = Toplevel(self.frame,  bg="SlateBlue", colormap="new")
         top.title('Update Issued Item Details')
         l1 = Label(top, text="Enter the ID of the item").grid(row = 1, column = 0, sticky = W, pady = 2)
         e1 = Entry(top)
         e1.grid(row=1, column=1, sticky=W, pady=2)
          
         B1 = Button(top, text="Fetch Records", command=lambda: (top.config(bg='SlateBlue'),self.fetch(self.update_issued_sub,e1)))
 
         B1.grid(row=1, column=2)

    def update_issued_sub(self, ID):
         top = Toplevel(self.frame,  bg="SlateBlue", colormap="new")
         top.title('Update Issued Item Records')
             
         result=(db_art.select_issued_item(ID)).fetchall()
         if result == []:
             self.notupdated(top)
         else:
             l0 = Label(top, text="Item ID").grid(row = 1, column = 0, sticky = W, pady = 2)
             l1 = Label(top, text="Name of item").grid(row = 2, column = 0, sticky = W, pady = 2)
             l2 = Label(top, text="Quantity Issued").grid(row = 3, column = 0, sticky = W, pady = 2)
             l3 = Label(top, text="Unit price").grid(row = 4, column = 0, sticky = W, pady = 2)
             l4 = Label(top, text="Amount").grid(row = 5, column = 0, sticky = W, pady = 2)
             e0=Entry(top,state='disabled')
             e0.grid(row=1, column=1, sticky=W, pady=2)
             e1 = Entry(top)
             e1.grid(row=2, column=1, sticky=W, pady=2)
             e2 = Entry(top)
             e2.grid(row=3, column=1, sticky=W, pady=2)
             e3 = Entry(top)
             e3.grid(row=4, column=1, sticky=W, pady=2)
             e4 = Entry(top)
             e4.grid(row=5, column=1, sticky=W, pady=2)
             result1=(db_art.select_raw_material(ID)).fetchall()
             
 
             for record in result:
                 
              
                # e0.insert(0,record[0])
                 e1.insert(0,record[1])
                        
                 e2.insert(0,record[2])
                 
                 e3.insert(0,record[3])
                 e4.insert(0,record[4])

             def chk_qty():
                   result1=(db_art.select_raw_material(ID)).fetchall()
                   if int(e2.get())>result1[0][2]:
                       messagebox.showinfo("Issued Item Details Update", "Quantity Issued cannot exceed raw material quantity!")
                   else:
                        
                       self.update(db_art.update_issued_item,e1,e2,e3,e4,record[0])
                       self.updated(top)
              #B1 = Button(top, text="Save Record", command=lambda: (top.config(bg='SlateBlue'), chk_qty(), self.update(db_art.update_issued_item,e1,e2,e3,e4,record[0]), self.updated(top)))             
                       
             B1 = Button(top, text="Save Record", command=lambda: (top.config(bg='SlateBlue'), chk_qty())).grid(row=1, column=2)
                   
            
            

         
         ##############

    def openimg(self,frame,e1,e2,e3,e4,e5):
        
        img = filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file", filetypes=(("PNG file", "*.png"),("JPG File", "*.jpg"),("All Files", "*.*")))
        image1 = PhotoImage(file=img)
        Label(frame, image=image1).grid(row=8,column=0)  
        lbl= Label(frame, image=image1)
        lbl.image = image1
        B3 = Button(frame, text="Input Details", background='green',command =lambda:(self.insert_art(db_art.insert_artwork_details,e1,e2,e3,e4,e5,lbl), self.added_art(frame)))
        B3.grid(row = 7, column = 1, sticky = W, pady = 2)
            
    def insert_artwork(self):
         
        top1 = Toplevel(self.frame,  bg="SlateBlue",    width=3000, height=250)
        top1.title('Add Art Work Details')
        l1 = Label(top1, text="Artwork Name").grid(row = 1, column = 0, sticky = W, pady = 2) 
        e1 = Entry(top1)
        e1.grid(row = 1, column = 1, sticky = W, pady = 2)
        l2 = Label(top1, text="Medium Used").grid(row = 2, column = 0, sticky = W, pady = 2)
        e2 = Entry(top1)
        e2.grid(row = 2, column = 1, sticky = W, pady = 2)
        l3 = Label(top1, text="Artist Name").grid(row = 3, column = 0, sticky = W, pady = 2)
        e3 = Entry(top1)
        e3.grid(row = 3, column = 1, sticky = W, pady = 2)
        l4 = Label(top1, text="Artwork Price").grid(row = 4, column = 0, sticky = W, pady = 2)
        e4 = Entry(top1)
        e4.grid(row = 4, column = 1, sticky = W, pady = 2)
        l5 = Label(top1, text="Date").grid(row = 5, column = 0, sticky = W, pady = 2)
        e5 = Entry(top1)
        e5.grid(row = 5, column = 1, sticky = W, pady = 2)
        l0 = Label(top1, text="Insert Image", background='SlateBlue', foreground = 'Gold', width=15,  borderwidth=0,font=("Calibri",18)).grid(row = 7, column = 0, sticky = W, pady = 2)   
        B0 = Button(top1, text="Browse Image",command = lambda:self.openimg(top1,e1,e2,e3,e4,e5))
        B0.grid(row = 6, column = 0, sticky = W, pady = 2)
 
 ###########
        
    def delete_artwork(self):
        top = Toplevel(self.frame,  bg="SlateBlue", colormap="new")
        top.title('Delete ArtWork Details')
        
        try:
            selected_item = self.treeview.selection()[0]
        
            for item in self.treeview.get_children(): 
                if selected_item == item:      
                    ID= (self.treeview.item(item).get('values')[0])  # extracts the selected record from dictionary to be deleted
                    self.treeview.delete(item) #removing old data view
                    self.delete(db_art.delete_artwork_details,str(ID))
                    self.deleted(top)
        except:
            Label(top,text="Select a product to be deleted", foreground = 'Gold').grid(row=10, column=2, sticky=W, pady=2)
          
 ##########

    def update_artwork(self):
         top = Toplevel(self.frame,  bg="SlateBlue", colormap="new")
         top.title('Update ArtWork Details')
         l1 = Label(top, text="Enter the ID of the item").grid(row = 1, column = 0, sticky = W, pady = 2)
         e1 = Entry(top)
         e1.grid(row=1, column=1, sticky=W, pady=2)          
         B1 = Button(top, text="Fetch Records", command=lambda: (top.config(bg='SlateBlue'),self.fetch(self.update_artwork_sub,e1)))                        
         B1.grid(row=1, column=2)

    def update_artwork_sub(self, ID):
         top = Toplevel(self.frame,  bg="SlateBlue", colormap="new")
         top.title('Update ArtWork Records')
         result=(db_art.select_artwork_detail(ID)).fetchall()
         if result==[]:
             self.notupdated(top)
         else:
             l0 = Label(top, text="Product ID").grid(row = 1, column = 0, sticky = W, pady = 2)
             l1 = Label(top, text="Product Name").grid(row = 2, column = 0, sticky = W, pady = 2)
             l2 = Label(top, text="Artist Name").grid(row = 3, column = 0, sticky = W, pady = 2)
             l3 = Label(top, text="Medium used").grid(row = 4, column = 0, sticky = W, pady = 2)
             l4 = Label(top, text="Product Price").grid(row = 5, column = 0, sticky = W, pady = 2)
             l5 = Label(top, text="Status").grid(row = 6, column = 0, sticky = W, pady = 2)
             #I6 = Label(top, text="Date").grid(row = 7, column = 0, sticky = W, pady = 2)
             e0=Entry(top)
             e0.grid(row=1, column=1, sticky=W, pady=2)
             e1 = Entry(top)
             e1.grid(row=2, column=1, sticky=W, pady=2)
             e2 = Entry(top)
             e2.grid(row=3, column=1, sticky=W, pady=2)
             e3 = Entry(top)
             e3.grid(row=4, column=1, sticky=W, pady=2)
             e4 = Entry(top)
             e4.grid(row=5, column=1, sticky=W, pady=2)
             e5 = Entry(top)
             e5.grid(row=6, column=1, sticky=W, pady=2)
             
            
             for record in result:
                 
                 e0.insert(0,record[0])
                 e1.insert(0,record[1])
                 e2.insert(0,record[2])
                 e3.insert(0,record[3])
                 e4.insert(0,record[4])
                 e5.insert(0,record[5])
 
     
             B1 = Button(top, text="Save Record", command=lambda: (top.config(bg='SlateBlue'), self.update_art(db_art.update_artwork_detail,e1,e2,e3,e4,e5,e0), self.updated(top)))
             B1.grid(row=1, column=2)
             
 
##############
        
def main():
  
    root = Tk()
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="green3", foreground="black")
    
    root.geometry("480x210+300+300")
    root.title("Expense Tracker")
    root['bg']="SlateBlue"
    root.iconbitmap(r'logo.ico')
    tracker = Authenticate(root)
    
    #root.resizable(width=False, height=False)
    root.mainloop()
     
main()
