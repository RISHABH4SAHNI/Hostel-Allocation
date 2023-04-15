from tkinter import*
from  tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox 
import os

class Student:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Hostel Allocation System')


        lbl_title=Label(self.root,text='HOSTEL ALLOCATION SYSTEM',font=('times new roman',40,'bold','underline'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)
        #logo
        img_logo=Image.open('PHOTOS/bits.png')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=300,y=0,width=50,height=50)
        #image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=200)
        #img1
        img1=Image.open('PHOTOS/VYAS_BHAWAN.jpeg')
        img1=img1.resize((300,150),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self1=Label(img_frame,image=self.photo1)
        self1.place(x=0,y=0,width=300,height=150)
        #img2
        img2=Image.open('PHOTOS/KSN_BHAWAN.jpeg')
        img2=img2.resize((300,150),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self2=Label(img_frame,image=self.photo2)
        self2.place(x=300,y=0,width=300,height=150)
        #img3
        img3=Image.open('PHOTOS/GND_BHAWAN.jpeg')
        img3=img3.resize((300,150),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self3=Label(img_frame,image=self.photo3)
        self3.place(x=600,y=0,width=300,height=150)

        #img4
        img4=Image.open('PHOTOS/BD_BHAWAN.jpeg')
        img4=img4.resize((300,150),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img4)

        self4=Label(img_frame,image=self.photo4)
        self4.place(x=900,y=0,width=300,height=150)

        #img5
        img5=Image.open('PHOTOS/RM_BHAWAN.jpeg')
        img5=img5.resize((300,150),Image.ANTIALIAS)
        self.photo5=ImageTk.PhotoImage(img5)

        self5=Label(img_frame,image=self.photo5)
        self5.place(x=1200,y=0,width=300,height=150)


        #Main Frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=200,width=1500,height=570)
        
        #upper frame
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Student Information',font=('times new roman',15,'bold','underline'),fg='red',bg='white')
        upper_frame.place(x=10,y=10,width=1480,height=200)

        #variables
        self.var_pref=StringVar();
        self.var_leadersid=StringVar();
        self.var_sid1=StringVar();
        self.var_sid2=StringVar();

        self.var_sid3=StringVar();
        self.var_sid4=StringVar();
        self.var_sid5=StringVar();
        
 
        

        #Labels and Entry fields
        lbl_dep=Label(upper_frame,text='Hostel Preference',font=('times new roman',15,'bold'),fg='black',bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_pref,font=('times new roman',15,'bold'),width=17,state='readonly')    
        combo_dep['value']=('Select Hostel','Ram','Budh','Krishna','Gandhi','Vyas')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #S-ID Leader
        lbl_sid=Label(upper_frame,font=('times new roman',15,'bold'),text='Wing Leader ID',bg='white',fg='black')
        lbl_sid.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_sid=ttk.Entry(upper_frame,textvariable=self.var_leadersid,width=19,font=('times new roman',15,'bold'))
        txt_sid.grid(row=1,column=1,padx=2,pady=7)


        #S-ID 1
        lbl_sid=Label(upper_frame,font=('times new roman',15,'bold'),text='S-ID1',bg='white',fg='black')
        lbl_sid.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_sid=ttk.Entry(upper_frame,textvariable=self.var_sid1,width=19,font=('times new roman',15,'bold'))
        txt_sid.grid(row=1,column=3,padx=2,pady=7)

        #S-ID 2
        lbl_sid=Label(upper_frame,font=('times new roman',15,'bold'),text='S-ID2',bg='white',fg='black')
        lbl_sid.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_sid=ttk.Entry(upper_frame,textvariable=self.var_sid2,width=19,font=('times new roman',15,'bold'))
        txt_sid.grid(row=2,column=1,padx=2,pady=7)

        #S-ID 3
        lbl_sid=Label(upper_frame,font=('times new roman',15,'bold'),text='S-ID3',bg='white',fg='black')
        lbl_sid.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_sid=ttk.Entry(upper_frame,textvariable=self.var_sid3,width=19,font=('times new roman',15,'bold'))
        txt_sid.grid(row=2,column=3,padx=2,pady=7)

        #S-ID 4
        lbl_sid=Label(upper_frame,font=('times new roman',15,'bold'),text='S-ID4',bg='white',fg='black')
        lbl_sid.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_sid=ttk.Entry(upper_frame,textvariable=self.var_sid4,width=19,font=('times new roman',15,'bold'))
        txt_sid.grid(row=3,column=1,padx=2,pady=7)

        #S-ID 5
        lbl_sid=Label(upper_frame,font=('times new roman',15,'bold'),text='S-ID5',bg='white',fg='black')
        lbl_sid.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_sid=ttk.Entry(upper_frame,textvariable=self.var_sid5,width=19,font=('times new roman',15,'bold'))
        txt_sid.grid(row=3,column=3,padx=2,pady=7)

        #mask image
        img_bits=Image.open('PHOTOS/bits2.jpg')
        img_bits=img_bits.resize((250,150),Image.ANTIALIAS)
        self.photo_bits=ImageTk.PhotoImage(img_bits)

        self.img_bits=Label(upper_frame,image=self.photo_bits)
        self.img_bits.place(x=690,y=10,width=250,height=150)



        #button frame
        button_frame=LabelFrame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1000,y=10,width=450,height=150)

        btn_add=Button(button_frame,text='Add Wing',command=self.add_wing,font=('times new roman',15,'bold'),width=15,bg='darkblue',fg='white')
        btn_add.grid(row=0,column=0,padx=20,pady=5)

        btn2_add=Button(button_frame,text='Delete Database',command = self.clear_database, font=('times new roman',15,'bold'),width=15,bg='darkblue',fg='white')
        btn2_add.grid(row=0,column=1,padx=2,pady=5)

        btn3_add=Button(button_frame,text='Initialise Database',command = self.intialise_database, font=('times new roman',15,'bold'),width=15,bg='darkblue',fg='white')
        btn3_add.grid(row=1,column=0,padx=2,pady=5)

        btn4_add=Button(button_frame,text='Delete',command=self.delete_data,font=('times new roman',15,'bold'),width=15,bg='darkblue',fg='white')
        btn4_add.grid(row=1,column=1,padx=2,pady=5)

        btn5_add=Button(button_frame,text='Update',command=self.update_data,font=('times new roman',15,'bold'),width=15,bg='darkblue',fg='white')
        btn5_add.grid(row=2,column=0,padx=2,pady=5)

        btn6_add=Button(button_frame,text='Clear',command=self.clear_data,font=('times new roman',15,'bold'),width=15,bg='darkblue',fg='white')
        btn6_add.grid(row=2,column=1,padx=2,pady=5)

        #down frame
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Student Information Table',font=('times new roman',15,'bold','underline'),fg='red',bg='white')
        down_frame.place(x=10,y=220,width=1100,height=75)

        down1_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Allotment Table',font=('times new roman',15,'bold','underline'),fg='red',bg='white')
        down1_frame.place(x=1110,y=220,width=370,height=75)


        down2_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,font=('times new roman',15,'bold','underline'),fg='red',bg='white')
        down2_frame.place(x=10,y=290,width=1480,height=270)

        button2_frame=LabelFrame(down1_frame,bd=2,relief=RIDGE,bg='white')
        button2_frame.place(x=1125,y=225,width=200,height=65)
        button2_frame.pack()
        btn9_add=Button(button2_frame,text='Start Allotment',command=self.start_allotment,font=('times new roman',15,'bold'),width=15,bg='darkblue',fg='white')
        btn9_add.pack()       
        style = ttk.Style()
        style.configure('My.TFrame', background='white')
        #Allocation Table

        #Table Frame
        table_frame=ttk.Frame(down2_frame,borderwidth=3,relief=RIDGE,style='My.TFrame')
        table_frame.place(x=0,y=75,width=1476,height=120)
        table_frame.pack(fill='both', expand=True)

        #tABLE 1

        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Wing Leader ID",'S-ID1',"S-ID2","S-ID3","S-ID4","S-ID5","Hostel Preference"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,height=120)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('Wing Leader ID',text='Wing Leader ID')
        self.student_table.heading('S-ID1',text='S-ID1')
        self.student_table.heading('S-ID2',text='S-ID2')
        self.student_table.heading('S-ID3',text='S-ID3')
        self.student_table.heading('S-ID4',text='S-ID4')
        self.student_table.heading('S-ID5',text='S-ID5')
        self.student_table.heading('Hostel Preference',text='Hostel Preference')

        self.student_table['show']='headings'
        self.student_table.column("Wing Leader ID", width=100, anchor=CENTER)
        self.student_table.column("S-ID1", width=100, anchor=CENTER)
        self.student_table.column("S-ID2", width=100, anchor=CENTER)
        self.student_table.column("S-ID3", width=100, anchor=CENTER)
        self.student_table.column("S-ID4", width=100, anchor=CENTER)
        self.student_table.column("S-ID5", width=100, anchor=CENTER)
        self.student_table.column("Hostel Preference", width=100, anchor=CENTER)
        self.student_table.pack(side='left',fill=BOTH,expand=1, padx=10, pady=10)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
        
        self.fetch_data()
        #table-2 allotment

        scroll_x1=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y1=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table2=ttk.Treeview(table_frame,column=("S_ID","H_NAME","ROOM_NUMBER"),xscrollcommand=scroll_x1.set,yscrollcommand=scroll_y1.set,height=120)
        scroll_x1.pack(side=BOTTOM,fill=X)
        scroll_y1.pack(side=RIGHT,fill=Y)


        scroll_x1.config(command=self.student_table2.xview)
        scroll_y1.config(command=self.student_table2.yview)

        self.student_table2.heading('S_ID',text='S_ID')
        self.student_table2.heading('H_NAME',text='H_NAME')
        self.student_table2.heading('ROOM_NUMBER',text='ROOM_NUMBER')

        self.student_table2['show']='headings'

        self.student_table2.column('S_ID',width=100,anchor=CENTER)
        self.student_table2.column('H_NAME',width=100,anchor=CENTER)
        self.student_table2.column('ROOM_NUMBER',width=100,anchor=CENTER)

        self.student_table2.pack(side='left',fill=BOTH,expand=1, padx=10, pady=10)
        self.student_table2.bind("<ButtonRelease>",self.get_cursor)
        self.fetch2_data()

        #search frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Allocation Information',fg='black')
        search_frame.place(x=5,y=0,width=1470,height=70)

        search_by=Label(search_frame,font=('times new roman',15,'bold'),text='Search By:',fg='white',bg='darkblue')
        search_by.grid(row=0,column=0,sticky=W,padx=10)

        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=('times new roman',15,'bold'),width=17)
        com_txt_search['value']=("Select Option","Preference","S_ID","S_ID1","S_ID2","S_ID3","S_ID4","S_ID5")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)


        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=25,font=('times new roman',12,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,command=self.search_data,text="Search",font=('times new roman',12,'bold'),width=17,fg='white',bg='darkblue')
        btn_search.grid(row=0,column=3,padx=5)

        btn_showall=Button(search_frame,command=self.fetch_data,text="ShowAll",font=('times new roman',12,'bold'),width=17,fg='white',bg='darkblue')
        btn_showall.grid(row=0,column=4,padx=5)


     # Function declaration
    def add_wing(self):
        # if self.var_sid.get()=="":
        #     messagebox.showerror('Error','Leader ID is required field')
        # if self.var_pref.get()=="":
        #     messagebox.showerror('Error','Hostel preference is required field')
        # else:
        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='Admin@123',database='BITS')
            my_cursor=conn.cursor()
            my_cursor.execute('INSERT INTO Wing VALUES(%s,%s,%s,%s,%s,%s,%s)',(
                                                                                self.var_leadersid.get(),
                                                                                self.var_sid1.get(),
                                                                                self.var_sid2.get(),
                                                                                self.var_sid3.get(),
                                                                                self.var_sid4.get(),
                                                                                self.var_sid5.get(),
                                                                                self.var_pref.get()
                                                                                    ))
                    
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Success','Wing has been added!',parent=self.root)
        except Exception as es:
            messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
    
    pass

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Admin@123',database='BITS')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from Wing')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def fetch2_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Admin@123',database='BITS')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from Allotment')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table2.delete(*self.student_table2.get_children())
            for i in data:
                self.student_table2.insert("",END,values=i)
            conn.commit()
        conn.close()
    #get cursor 
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content['values']

        self.var_leadersid.set(data[0])
        self.var_sid1.set(data[1])
        self.var_sid2.set(data[2])
        self.var_sid3.set(data[3])
        self.var_sid4.set(data[4])
        self.var_sid5.set(data[5])
        self.var_pref.set(data[6])


    def update_data(self):
        try:
            update=messagebox.askyesno('Update','Are you sure to update student data ')
            if update>0:
                conn=mysql.connector.connect(host='localhost',user='root',password='Admin@123',database='BITS')
                my_cursor=conn.cursor()
                my_cursor.execute('update Wing set S_ID1=%s,S_ID2=%s,S_ID3=%s,S_ID4=%s,S_ID5=%s,Preference=%s where S_ID=%s' ,(
                                                                                                                                            
                                                                                                                                            self.var_sid1.get(),
                                                                                                                                            self.var_sid2.get(),
                                                                                                                                            self.var_sid3.get(),
                                                                                                                                            self.var_sid4.get(),
                                                                                                                                            self.var_sid5.get(),
                                                                                                                                            self.var_pref.get(),
                                                                                                                                            self.var_leadersid.get()
                                                                                                                                        
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                ))
            else:
                if not update:
                    return
            conn.commit()  
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Success','Wing Sucessfully Updated',parent=self.root)
        except Exception as es:
            messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    pass



    def delete_data(self):
        try:
            Delete=messagebox.askyesno('Delete','Are you sure you want to delete this wing')
            if Delete>0:
                conn=mysql.connector.connect(host='localhost',user='root',password='Admin@123',database='BITS')
                my_cursor=conn.cursor()
                sql='delete from Wing where S_ID=%s'
                value=(self.var_leadersid.get(),)
                my_cursor.execute(sql,value)
            else:
                if not Delete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Success','Wing Sucessfully Deleted',parent=self.root)
        except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    pass


    def clear_data(self):
        self.var_leadersid.set("")
        self.var_sid1.set("")
        self.var_sid2.set("")
        self.var_sid3.set("")
        self.var_sid4.set("")
        self.var_sid5.set("")
        self.var_pref.set("Select Hostel")


    def search_data(self):
        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='Admin@123',database='BITS')
            my_cursor=conn.cursor()
            my_cursor.execute('select * from Wing where '+str(self.var_com_search.get())+' = "'+str(self.var_search.get() + '"') )
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in rows:
                    self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)    

    def intialise_database(self):

        os.system('cmd /k "node initialise.js"')
        # os.system('node initialise.js')

    def clear_database(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Admin@123',database='BITS')
        c = conn.cursor()
        c.execute('''Drop table Student''')
        c.execute('''Drop table Hostel''')
        c.execute('''Drop table Wing''')
        c.execute('''Drop table Rooms''')
        c.execute('''Drop table Allotment''')
        conn.commit()
        conn.close()

    def start_allotment(self):
        os.system('cmd /k "node backend.js"')
        # os.system('node backend.js')
        self.fetch2_data()

def initialise_database():

        os.system('cmd /k "node initialise.js"')
        # os.system('node initialise.js')

if __name__=="__main__":
    try:
        initialise_database()
    finally:
        root=Tk()
        obj=Student(root)
        root.mainloop()