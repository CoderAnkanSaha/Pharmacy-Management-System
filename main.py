from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox, ttk
import pymysql
import mysql.connector
# ========== Clear ======================
def clear():
     # refno.delete(0,END)
     # med.delete(0,END)
     refMed_var.set("")
     addmed_var.set("")
   
# ============================ Add Medicine functionality declaration ===============================
def AddMed():
     if refno.get() == '' or med.get()=='':
            messagebox.showerror('Error','All fields are required')
     else:
          conn = mysql.connector.connect(host="localhost", username = "root", password= "*********", database="mydata")
          my_cursor = conn.cursor()
          my_cursor.execute("insert into pharma(Ref, MedName) values(%s,%s)",(
               refMed_var.get(), addmed_var.get()
          ))
          conn.commit()
          fetch_dataMed()
          messagebox.showinfo("Success","Medicine added")
          Medget_Cursor()
          conn.close()

#=========== MedGetcursor=====================

def Medget_Cursor(ev=""):
     cursor_row = medicine_table.focus()
     content = medicine_table.item(cursor_row)
     row = content["values"]
     refMed_var.set(row[0])
     addmed_var.set(row[1])


def fetch_dataMed():
     conn = mysql.connector.connect(host= 'localhost',username='root',password='*******', database= 'mydata')
     mycursor = conn.cursor()
     mycursor.execute('Select * from pharma')
     rows= mycursor.fetchall()
     if len(rows)!=0:
          medicine_table.delete(*medicine_table.get_children())
          for i in rows:
               medicine_table.insert('',END,values=i)
          conn.commit()
     conn.close()

#======= Update Med ======

def UpdateMed():
     if refno.get() == '' or med.get()=='':
            messagebox.showerror('Error','All fields are required')
     else:
          conn = mysql.connector.connect(host= 'localhost',username='root',password='*********', database= 'mydata')
          my_cursor = conn.cursor()
          my_cursor.execute("update pharma set MedName=%s where Ref =%s",(
               addmed_var.get(),
               refMed_var.get()
          ))
          conn.commit()
          fetch_dataMed()
          conn.close()

          messagebox.showinfo("Success",'Medicine has been updated')

def DeleteMed():
     if refno.get() == '' or med.get()=='':
          messagebox.showerror('Error','All fields are required')
     else:
          conn = mysql.connector.connect(host= 'localhost',username='root',password='*********', database= 'mydata')
          my_cursor = conn.cursor()
          sql = "delete from pharma where Ref=%s"
          val= (refMed_var.get(),)
          my_cursor.execute(sql,val)
          conn.commit()
          fetch_dataMed()
          conn.close()
          messagebox.showinfo("Info","Deleted successfully")


 #======= Main Table =========

def add_data():
     if Ref_no_var.get()=="" or LotNo_var.get()=="":
          messagebox.showerror("Error", "All the fields are required")
     else:
          conn = mysql.connector.connect(host="localhost", username = "root", password= "*********", database="mydata")
          my_cursor = conn.cursor()
          my_cursor.execute("insert into pharmacy(Ref_no,CmpName,TypeMed,MedName,LotNo,IssueDate,ExpiryDate,Sideeffect,warning,dosage,Price,product) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
               Ref_no_var.get(),
               CmpName_var.get(),
               TypeMed_var.get(),
               MedName_var.get(),
               LotNo_var.get(),
               IssueDate_var.get(),
               ExpiryDate_var.get(),
               Sideeffect_var.get(),
               warning_var.get(),
               dosage_var.get(),
               Price_var.get(),
               product_var.get(),
               
          ))

                                             
          conn.commit()
          fetch_data()
          conn.close()
          messagebox.showinfo("Success", "data has been inserted")

def fetch_data():
     conn = mysql.connector.connect(host= "localhost",username="root", password = "********", database = "mydata")
     my_cursor = conn.cursor()
     my_cursor.execute("select * from pharmacy")
     row= my_cursor.fetchall()
     if len(row)!=0:
          displaytable.delete(*displaytable.get_children())
          for i in row:
               displaytable.insert("",END,values=i)
          conn.commit
     conn.close()

def get_cursor(ev = ""):
     cursor_row = displaytable.focus()
     content= displaytable.item(cursor_row)
     row= content["values"]

     Ref_no_var.set(row[0]),
     CmpName_var.set(row[1]),
     TypeMed_var.set(row[2]),
     MedName_var.set(row[3]),
     LotNo_var.set(row[4]),
     IssueDate_var.set(row[5]),
     ExpiryDate_var.set(row[6]),
     Sideeffect_var.set(row[7]),
     warning_var.set(row[8]),
     dosage_var.set(row[9]),
     Price_var.set(row[10]),
     product_var.set(row[11])


def Update():
     if ref_combo.get() == '' or LotSearch.get()=='':
            messagebox.showerror('Error','All fields are required')
     else:
          conn = mysql.connector.connect(host= 'localhost',username='root',password='*********', database= 'mydata')
          my_cursor = conn.cursor()
          my_cursor.execute("update pharmacy set CmpName=%s, TypeMed=%s, MedName=%s, LotNo=%s, IssueDate=%s, ExpiryDate=%s, Sideeffect=%s, warning=%s, dosage=%s, Price=%s, product=%s where Ref_no=%s",(
               
               CmpName_var.get(),
               TypeMed_var.get(),
               MedName_var.get(),
               LotNo_var.get(),
               IssueDate_var.get(),
               ExpiryDate_var.get(),
               Sideeffect_var.get(),
               warning_var.get(),
               dosage_var.get(),
               Price_var.get(),
               product_var.get(),
               Ref_no_var.get()
          ))
          conn.commit()
          fetch_data()
          conn.close()

          messagebox.showinfo("Success",'Medicine has been updated')

def Delete():
     if ref_combo.get() == '' or LotSearch.get()=='':
          messagebox.showerror('Error','All fields are required')
     else:
          conn = mysql.connector.connect(host= 'localhost',username='root',password='*******', database= 'mydata')
          my_cursor = conn.cursor()
          sql = "delete from pharmacy where Ref_no=%s"
          val= (Ref_no_var.get(),)
          my_cursor.execute(sql,val)
          conn.commit()
          fetch_data()
          conn.close()
          messagebox.showinfo("Info","Deleted successfully")

def reset():
     CmpName_var.set(""),
     LotNo_var.set(""),
     IssueDate_var.set(""),
     ExpiryDate_var.set(""),
     Sideeffect_var.set(""),
     warning_var.set(""),
     dosage_var.set(""),
     Price_var.set(""),
     product_var.set("")

def search_data():
     conn = mysql.connector.connect(host = "localhost",username = "root", password= "******", database = "mydata") 
     my_cursor= conn.cursor()
     val = searchtxt_var.get()
     my_cursor.execute("Select * from pharmacy where `Ref_no` like %s or `MedName` like %s or `LotNo` like %s", ("%"+val+"%","%"+val+"%","%"+val+"%"))
     rows = my_cursor.fetchall()
     if len(rows)!= 0:
          displaytable.delete(*displaytable.get_children())
          for i in rows:
               displaytable.insert("",END, values=i)
          conn.commit()
     conn.close()

def Exit(event = None):
     result = messagebox.askyesno('Confirm', 'Do You Want to Exit')
     if result:
        root.destroy()
     else:
        pass

root = Tk()
root.title('Pharmacy Management System')
root.geometry("1530x785+5+5")
root.resizable(False,False)
# ========== variable ===========

               
addmed_var = StringVar()
refMed_var = StringVar()

#============= main table variable ========
Ref_no_var = StringVar()
CmpName_var = StringVar()
TypeMed_var = StringVar()
MedName_var = StringVar()
LotNo_var = StringVar()
IssueDate_var = StringVar()
ExpiryDate_var = StringVar()
Sideeffect_var = StringVar()
warning_var = StringVar()
dosage_var = StringVar()
Price_var = StringVar()
product_var = StringVar()



#title frame

lbltitle = Label(root,text="PHARMACY MANAGEMENT SYSTEM", bd=15,relief=RIDGE, bg= 'white', fg='darkgreen', font=('times new roman',50,"bold"),padx=2, pady=4)
lbltitle.pack(side=TOP, fill= X)

img1 = Image.open("D:\PYTHON\Tkinter Tutorials\Pharma software\IMAGES\download.png")
# img1 = img1.resize((80,80),Image.ANTIALIAS) ------> ,Image.ANTIALIAS reduces image quality
img1 = img1.resize((80,80))
photoimg1 = ImageTk.PhotoImage(img1)
b1 = Button(root, image=photoimg1,borderwidth=0)
b1.place(x=50,y=20)

# Data frame
DataFrame = Frame(root,bd=15, relief=RIDGE,padx=20)
DataFrame.place(x=7,y=120,width=1492,height=400)

DataFrameLeft= LabelFrame(DataFrame, bd=10,relief=RIDGE,padx=17,text="Medicine Information", fg="darkgreen", font=("times new roman",12,"bold"))
DataFrameLeft.place(x=0,y=5,width=810,height=350)
       

# Button frame

ButtonFrame = Frame(root, bd=15,relief=RIDGE,padx=20)
ButtonFrame.place(x=7,y=520,width=1492,height=65)

# Main Button

btnAddData= Button(ButtonFrame,text="Medicine Add", font=("times new roman",13,"bold"), width=12,bg="darkgreen", fg="white",padx=2,pady=4, command=add_data)
btnAddData.grid(row=0,column=0)

btnupdateMed= Button(ButtonFrame,text="UPDATE", font=("times new roman",13,"bold"), width=12,bg="darkgreen", fg="white",padx=2,pady=4, command=Update)
btnupdateMed.grid(row=0,column=1)

btnDeleteMed= Button(ButtonFrame,text="DELETE", font=("times new roman",13,"bold"),width=12, bg="darkgreen", fg="white",padx=2,pady=4,command=Delete)
btnDeleteMed.grid(row=0,column=2)

btnResetMed= Button(ButtonFrame,text="RESET", font=("times new roman",13,"bold"),width=12, bg="darkgreen", fg="white",padx=2,pady=4, command=reset)
btnResetMed.grid(row=0,column=3)

btnExitMed= Button(ButtonFrame,text="EXIT", font=("times new roman",13,"bold"),width=12, bg="darkgreen", fg="white",padx=2,pady=4, command=Exit)
btnExitMed.grid(row=0,column=4)

#Search By
lblSearch = Label(ButtonFrame,font=("times new roman",17,"bold"), text="Search By", padx=2,bg="darkgreen",fg="white",pady=4.3,width=10)
lblSearch.grid(row=0,column=5,sticky=W)


# variable
search_var = StringVar()
search_combo= ttk.Combobox(ButtonFrame,textvariable=search_var,width=12,font=("times new roman",19,"bold"),state="readonly")
search_combo['values']=("Ref_no", "MedName", "LotNo")
search_combo.grid(row=0,column=6)
search_combo.current(0)

#variable
searchtxt_var = StringVar()
txtSearch= Entry(ButtonFrame,textvariable=searchtxt_var,bd=2,relief=RIDGE,width=12,font=("times new roman",19,"bold"))
txtSearch.grid(row=0,column=7)

search= Button(ButtonFrame,text="SEARCH", font=("times new roman",13,"bold"),width=13, bg="darkgreen", fg="white",padx=2,pady=4, command=search_data)
search.grid(row=0,column=8)

showAll= Button(ButtonFrame,text="SHOW ALL", font=("times new roman",13,"bold"),width=13, bg="darkgreen", fg="white",padx=2,pady=4, command=fetch_data)
showAll.grid(row=0,column=9)

#label and entry
lblrefno = Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Reference No",padx=2,pady=4)
lblrefno.grid(row=0,column=0,sticky=W)


conn = mysql.connector.connect(host="localhost", username = "root", password= "******", database="mydata")
my_cursor = conn.cursor()
my_cursor.execute("select Ref from pharma")
row = my_cursor.fetchall()

ref_combo= ttk.Combobox(DataFrameLeft,textvariable=Ref_no_var,width=27,font=("times new roman",13,"bold"),state="readonly")
ref_combo['values']= row
ref_combo.grid(row=0,column=1)
ref_combo.current(0)

lblcompName = Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Company Name",padx=2,pady=4)
lblcompName.grid(row=1,column=0,sticky=W)

compSearch= Entry(DataFrameLeft,textvariable=CmpName_var,bd=2,relief=RIDGE,width=29,font=("times new roman",13,"bold"))
compSearch.grid(row=1,column=1)

lbltypeOfmed = Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Type of Medicine",padx=2,pady=4)
lbltypeOfmed.grid(row=2,column=0,sticky=W)

typeofmed_combo= ttk.Combobox(DataFrameLeft,textvariable=TypeMed_var,width=27,font=("times new roman",13,"bold"),state="readonly")
typeofmed_combo['values']= ("Tablets", "Capsules", "Spansules", "Softgels", "Liquids", "Granules", "Powders", "Drops", "Sprays", "Inhalers", "Injections", "Supplements")
typeofmed_combo.grid(row=2,column=1)
typeofmed_combo.current(0)

lblmedname = Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Medicine Name",padx=2,pady=4)
lblmedname.grid(row=3,column=0,sticky=W)

conn = mysql.connector.connect(host= 'localhost',username='root',password='*****', database= 'mydata')
mycursor = conn.cursor()
mycursor.execute('Select MedName from pharma')
m = mycursor.fetchall()

medname_combo= ttk.Combobox(DataFrameLeft,textvariable=MedName_var,width=27,font=("times new roman",13,"bold"),state="readonly")
medname_combo['values']= m
medname_combo.grid(row=3,column=1)
medname_combo.current(0)

lblLotNo = Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Lot No",padx=2,pady=6)
lblLotNo.grid(row=4,column=0,sticky=W)

LotSearch= Entry(DataFrameLeft,textvariable=LotNo_var,bd=2,relief=RIDGE,width=29,font=("times new roman",13,"bold"))
LotSearch.grid(row=4,column=1)

lblissue = Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Issue Date",padx=2,pady=6)
lblissue.grid(row=5,column=0,sticky=W)

Issuedate= Entry(DataFrameLeft,bd=2,textvariable=IssueDate_var,relief=RIDGE,width=29,font=("times new roman",13,"bold"))
Issuedate.grid(row=5,column=1)

lblExpDate = Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Exp Date:",padx=2,pady=6)
lblExpDate.grid(row=6,column=0,sticky=W)

ExpDate= Entry(DataFrameLeft,textvariable=ExpiryDate_var,bd=2,relief=RIDGE,width=29,font=("times new roman",13,"bold"))
ExpDate.grid(row=6,column=1)

lblsideEffect = Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Side Effect",padx=2,pady=6)
lblsideEffect.grid(row=7,column=0,sticky=W)

SideEffect= Entry(DataFrameLeft,bd=2,textvariable=Sideeffect_var,relief=RIDGE,width=29,font=("times new roman",13,"bold"))
SideEffect.grid(row=7,column=1)

lblPrecandWarning = Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Prec&Warning",padx=2,pady=4)
lblPrecandWarning.grid(row=0,column=2,sticky=W)

PrecandWarning= Entry(DataFrameLeft,textvariable=warning_var,bd=2,relief=RIDGE,width=29,font=("times new roman",13,"bold"))
PrecandWarning.grid(row=0,column=3)

lblDosage = Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Dosage",padx=2,pady=4)
lblDosage.grid(row=1,column=2,sticky=W)

Dosage= Entry(DataFrameLeft,textvariable=dosage_var,bd=2,relief=RIDGE,width=29,font=("times new roman",13,"bold"))
Dosage.grid(row=1,column=3)

lblTabPrice = Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Tablet Price",padx=2,pady=4)
lblTabPrice.grid(row=2,column=2,sticky=W)

TabPrice= Entry(DataFrameLeft,bd=2,textvariable=Price_var,relief=RIDGE,width=29,font=("times new roman",13,"bold"))
TabPrice.grid(row=2,column=3)

lblPdtQuant = Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Product QT",padx=2,pady=4)
lblPdtQuant.grid(row=3,column=2,sticky=W)

PdtQuant= Entry(DataFrameLeft,textvariable=product_var,bd=2,relief=RIDGE,width=29,font=("times new roman",13,"bold"))
PdtQuant.grid(row=3,column=3)

lblQuote= Label(DataFrameLeft, relief=RIDGE,font=("times new roman",14,"bold"),text="We are Open 24x7",pady=4,bg="white", fg="darkgreen",width=15)
lblQuote.place(x=530,y=123)

img2 = Image.open("D:\PYTHON\Tkinter Tutorials\Pharma software\IMAGES\shop.webp")
# img2 = img2.resize((80,80),Image.ANTIALIAS) ------> ,Image.ANTIALIAS reduces image quality
img2 = img2.resize((160,140))
photoimg2 = ImageTk.PhotoImage(img2)
b2 = Button(DataFrameLeft, image=photoimg2,borderwidth=0)
b2.place(x=420,y=160)

img3 = Image.open("D:\PYTHON\Tkinter Tutorials\Pharma software\IMAGES\sf.jpg")
# img3 = img3.resize((80,80),Image.ANTIALIAS) ------> ,Image.ANTIALIAS reduces image quality
img3 = img3.resize((160,140))
photoimg3 = ImageTk.PhotoImage(img3)
b3 = Button(DataFrameLeft, image=photoimg3,borderwidth=0)
b3.place(x=600,y=160)



DataFrameRight= LabelFrame(DataFrame, bd=10,relief=RIDGE,padx=17,text="Medicine Addition", fg="darkgreen", font=("times new roman",12,"bold"))
DataFrameRight.place(x=840,y=5,width=580,height=350)

img4 = Image.open("D:\PYTHON\Tkinter Tutorials\Pharma software\IMAGES\cal.webp")
# img4 = img4.resize((80,80),Image.ANTIALIAS) ------> ,Image.ANTIALIAS reduces image quality
img4 = img4.resize((300,80))
photoimg4 = ImageTk.PhotoImage(img4)
b4 = Button(DataFrameRight, image=photoimg4,borderwidth=0)
b4.place(x=0,y=2)

lblref = Label(DataFrameRight,font=("times new roman",11,"bold"),text="Reference No: ",padx=2,pady=2)
lblref.place(x=0,y=90)

refno= Entry(DataFrameRight,textvariable=refMed_var,bd=2,relief=RIDGE,width=15,font=("times new roman",13,"bold"))
refno.place(x=115,y=90)

lblmed = Label(DataFrameRight,font=("times new roman",11,"bold"),text="Medicine Name: ",padx=2,pady=2)
lblmed.place(x=0,y=130)

med= Entry(DataFrameRight,textvariable=addmed_var,bd=2,relief=RIDGE,width=15,font=("times new roman",13,"bold"))
med.place(x=115,y=130)

img5 = Image.open("D:\PYTHON\Tkinter Tutorials\Pharma software\IMAGES\pills.jpg")
# img5 = img5.resize((80,80),Image.ANTIALIAS) ------> ,Image.ANTIALIAS reduces image quality
img5 = img5.resize((215,153))
photoimg5 = ImageTk.PhotoImage(img5)
b5 = Button(DataFrameRight, image=photoimg5,borderwidth=0)
b5.place(x=311,y=2)

ButtonRightFrame = Frame(DataFrameRight,bd=4,relief=RIDGE,padx=2,bg="green")
ButtonRightFrame.place(x=311,y=160,width=215,height=150)

btnAdd= Button(ButtonRightFrame,text="ADD", font=("times new roman",13,"bold"), width=19,bg="darkgreen", fg="white",padx=2,pady=2,command= AddMed)
btnAdd.grid(row=0,column=0)

btnupdate= Button(ButtonRightFrame,text="UPDATE", font=("times new roman",13,"bold"), width=19,bg="blue", fg="white",padx=2,pady=2, command= UpdateMed)
btnupdate.grid(row=1,column=0)

btnDelete= Button(ButtonRightFrame,text="DELETE", font=("times new roman",13,"bold"),width=19, bg="red", fg="white",padx=2,pady=2, command= DeleteMed)
btnDelete.grid(row=2,column=0)

btnclear= Button(ButtonRightFrame,text="CLEAR", font=("times new roman",13,"bold"),width=19, bg="purple", fg="white",padx=2,pady=2, command= clear)
btnclear.grid(row=3,column=0)

            #side frame

side_frame = Frame(DataFrameRight, bd=4,relief=RIDGE,bg="white")
side_frame.place(x=0,y=158,width=300,height=157)



            #scrollbars

sc_x= ttk.Scrollbar(side_frame,orient=HORIZONTAL)
sc_x.pack(side=BOTTOM,fill=X)
sc_y= ttk.Scrollbar(side_frame,orient=VERTICAL)
sc_y.pack(side=RIGHT,fill=Y)

medicine_table = ttk.Treeview(side_frame,column=("id","ref","medname"),xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

sc_x.config(command=medicine_table.xview)
sc_y.config(command=medicine_table.yview)

medicine_table.heading("id",text="No.")
medicine_table.heading("ref",text="Reference No")
medicine_table.heading("medname",text="Medicine Name")

medicine_table["show"]="headings"
medicine_table.pack(fill=BOTH,expand=1)

medicine_table.column("id",width=100)
medicine_table.column("ref",width=100)
medicine_table.column("medname",width=100)        
medicine_table.bind("<ButtonRelease-1>", Medget_Cursor)


# Display frame

DisplayFrame = Frame(root, bd=15,relief=RIDGE,padx=10)
DisplayFrame.place(x=7,y=585,width=1492,height=205)

#Display frame scrollbars

scroll_x= ttk.Scrollbar(DisplayFrame,orient=HORIZONTAL)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y= ttk.Scrollbar(DisplayFrame,orient=VERTICAL)
scroll_y.pack(side=RIGHT,fill=Y)

displaytable = ttk.Treeview(DisplayFrame,column=("reference","companyname","type","medicinename","lotno","issuedate","expdate","sideeffect", "warning","dosage","price","pdtqnt"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.config(command=displaytable.xview)
scroll_y.config(command=displaytable.yview)


displaytable.heading("reference", text="Reference")
displaytable.heading("companyname", text="Company Name")
displaytable.heading("type", text="Type of Medicine")
displaytable.heading("medicinename", text="Medicine Name")
displaytable.heading("lotno", text="Lot No")
displaytable.heading("issuedate", text="Issue Date")
displaytable.heading("expdate", text="Expiry Date")
displaytable.heading("sideeffect", text="Side Effects")
displaytable.heading("warning", text="Warning")
displaytable.heading("dosage", text="Dosage")
displaytable.heading("price", text="Price")
displaytable.heading("pdtqnt", text="Product Quantity")

displaytable["show"]= "headings"
displaytable.pack(fill=BOTH,expand=1)

displaytable.column("reference", width=80)
displaytable.column("companyname",width=80)
displaytable.column("type", width=80)
displaytable.column("medicinename", width=80)
displaytable.column("lotno", width=80)
displaytable.column("issuedate", width=80)
displaytable.column("expdate", width=80)
displaytable.column("sideeffect", width=80)
displaytable.column("warning", width=80)
displaytable.column("dosage", width=80)
displaytable.column("price", width=80)
displaytable.column("pdtqnt", width=80)
fetch_dataMed()
fetch_data()
displaytable.bind("<ButtonRelease-1>",get_cursor)


root.mainloop()
