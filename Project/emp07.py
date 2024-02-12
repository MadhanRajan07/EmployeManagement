import tkinter
from tkinter import*
from tkinter import ttk,font,messagebox
from PIL import ImageTk,Image

def ad_page(e):
    e.destroy() 
    e=Tk()
    e.geometry("1500x900")
    e.title("EMP")
    frame1=Frame(e,width=1500,height=900,bg="#BEE4ED")
    f=font.Font(weight="normal",family="times new roman",size=20)
    frame1.pack()
    f1=font.Font(family="Times New Roman",size=20)
    x=Label(e,text="LIVE WIRE",fg="red",bg="#BEE4ED",font=f1).place(relx=.45,rely=.01)

    frame=Frame(e,width=500,height=400,bg="#C38EB4").place(relx=.55,rely=.10)
    f=font.Font(e,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="STAFF REGISTER",font=f,bg="#C38EB4")
    l.place(relx=.65,rely=.12)
    l=Label(frame,text="Staff No:",font=f,bg="#C38EB4")
    l.place(relx=.60,rely=.24)
    l=Label(frame,text="Name:",font=f,bg="#C38EB4")
    l.place(relx=.60,rely=.34)
    l=Label(frame,text="Phone No:",font=f,bg="#C38EB4")
    l.place(relx=.60,rely=.44)
    l1=Entry(frame)
    l1.place(relx=.72,rely=.26)
    l2=Entry(frame)
    l2.place(relx=.72,rely=.36)
    l3=Entry(frame)
    l3.place(relx=.72,rely=.46)

    def sttfreg(StaffNo,Name,PhoneNo):
        import pymysql as mysql
        connection = mysql.connect(host="localhost", user="root", password="livewire", database="proemp")
        cursor=connection.cursor()
        s="insert into sttfreg(staffNo,Name, PhoneNo) values(%s,%s,%s)"
        t=(StaffNo,Name, PhoneNo)
        cursor.execute(s,t)
        connection.commit()
        messagebox.showinfo( "Success", "User Insert Successfully")
        l1.delete(0,END)
        l2.delete(0,END)
        l3.delete(0,END)

    b1= Button(frame, text="Register",font=f,bg="#FF6347",command=lambda: sttfreg(l1.get(),l2.get(),l3.get()))
    b1.place(relx=.69,rely=.55)
    f1=font.Font(family="Times New Roman",size=20)
    x=Label(e,text=" @CopyRight Madhan Rajan",fg="red",bg="#BEE4ED",font=f1)
    x.place(relx=.39,rely=.87)

    def treestf():
        import pymysql as mysql
        connection = mysql.connect(host="localhost", user="root", password="livewire", database="proemp")
        cursor = connection.cursor()
        cursor.execute( "SELECT * FROM sttfreg")
        result=cursor.fetchall()
        
        for x in result:
            tree.insert("", "end", values=x)
    

    tree = ttk.Treeview(e, columns=("Staff No", "Name","Phone No"), show="headings")
    tree.heading("#1", text="Staff No")
    tree.heading("#2", text="Name")
    tree.heading("#3", text="Phone No")
    tree.column("#1", width=55)
    tree.place(relx=.10,rely=.10,height=400)

    

    read_button = Button(e, text="Read File",command=lambda:treestf())
    read_button.place(relx=.25,rely=.7)

    
    e.mainloop()


def std_register(e): 
    e.destroy() 
    e=Tk()
    e.geometry("1500x900")
    e.title("EMP")
    frame1=Frame(e,width=1500,height=900,bg="#BEE4ED")
    f=font.Font(weight="normal",family="times new roman",size=20)
    frame1.pack()
    frame=Frame(e,width=500,height=590,bg="#1ABC9C").place(relx=.33,rely=.07)
    f=font.Font(e,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="STUDENT REGISTER",font=f,bg="#1ABC9C").place(relx=.40,rely=.12)

    f=font.Font(e,weight="bold",family="times new roman",size=17)
    l=Label(frame,text="Name:",font=f,bg="#1ABC9C").place(relx=.38,rely=.23)
    l=Label(frame,text="Age:",font=f,bg="#1ABC9C").place(relx=.38,rely=.32)
    l=Label(frame,text="Education:",font=f,bg="#1ABC9C").place(relx=.38,rely=.43)
    l=Label(frame,text="Course:",font=f,bg="#1ABC9C").place(relx=.38,rely=.54)
    l=Label(frame,text="PhoneNo:",font=f,bg="#1ABC9C").place(relx=.38,rely=.65)
    

    l1=Entry(frame)
    l1.place(relx=.50,rely=.24)
    l2=Entry(frame)
    l2.place(relx=.50,rely=.33)
    l3=Entry(frame)
    l3.place(relx=.50,rely=.44)
    l4=Entry(frame)
    l4.place(relx=.50,rely=.55)
    l5=Entry(frame)
    l5.place(relx=.50,rely=.66)
        
    def sreg(Name,Age,Education,Course,PhoneNo):
        import pymysql as mysql
        connection = mysql.connect(host="localhost", user="root", password="livewire", database="proemp")
        cursor=connection.cursor()
        s="insert into stdreg(Name, Age, Education, Course, PhoneNo) values(%s,%s,%s,%s,%s)"
        t=(Name,Age,Education,Course,PhoneNo)
        cursor.execute(s,t)
        connection.commit()
        messagebox.showinfo( "Success", "Staff Insert Successfully")
        l1.delete(0,END)
        l2.delete(0,END)
        l3.delete(0,END)
        l4.delete(0,END)
        l5.delete(0,END)
    
        
    f1=font.Font(weight="bold",family="Bodoni MT",size=17)
    b1=Button(frame,text="Register",font=f1,bg="#FF6347",activebackground="#FC92C4",width=10,command=lambda: sreg(l1.get(),l2.get(),l3.get(),l4.get(),l5.get()))
    b1.place(relx=.45,rely=.77)
    f1=font.Font(family="Times New Roman",size=20)
    x=Label(e,text="LIVE WIRE",fg="red",bg="#BEE4ED",font=f1).place(relx=.45,rely=.01)

    f1=font.Font(family="Times New Roman",size=20)
    x=Label(e,text=" @CopyRight Madhan Rajan",fg="red",bg="#BEE4ED",font=f1).place(relx=.39,rely=.87)
    e.mainloop()

def stf_page(e):
    e.destroy() 
    e=Tk()
    e.geometry("1500x900")
    e.title("EMP")
    frame1=Frame(e,width=1500,height=900,bg="#BEE4ED")
    f=font.Font(weight="normal",family="times new roman",size=20)
    frame1.pack()

    img5 = Image.open("live.jpg")
    img5 = img5.resize((500,150))
    img5= ImageTk.PhotoImage(img5)
    l=Label(e,image=img5).place(relx=.33,rely=.01)

    img6 = Image.open("it2.jpg")
    img6 = img6.resize((550,286))
    img6= ImageTk.PhotoImage(img6)
    l=Label(e,image=img6).place(relx=.05,rely=.48)

    img7 = Image.open("it1.jpg")
    img7 = img7.resize((550,286))
    img7= ImageTk.PhotoImage(img7)
    l=Label(e,image=img7).place(relx=.55,rely=.48)

   
    t1="""Livewire's on-demand courses in emerging technologies
      give you the knowledge you need to stay ahead of the curve and 
      succeed in today's fast-paced world."""
    x=Label(frame1,text=t1,font=f,bg="#BEE4ED")
    x.place(relx=.23,rely=.23)
    f1=font.Font(weight="bold",family="Century",size=20)
    b1=Button(frame1,text="Student Register",font=f1,bg="#FF6347",activebackground="#FC92C4",width=15,command=lambda: std_register(e))
    b1.place(relx=.42,rely=.38)
    f2=font.Font(family="Times New Roman",size=20)
    x=Label(e,text=" @CopyRight Madhan Rajan",fg="red",bg="#BEE4ED",font=f2).place(relx=.39,rely=.87)
    e.mainloop()

def ad_log(a,b,e):
    if(a=="admin" and b=="admin"):
        ad_page(e)
    else:
        ad_log(e)


def stf_log(a,b,e):
    if(a=="admin" and b=="admin"):
        stf_page(e)
    else:
      stf_log(e)

def staff_login(e):
    e.destroy() 
    e=Tk()
    e.geometry("1500x900")
    e.title("EMP")
    frame1=Frame(e,width=1500,height=900,bg="#BEE4ED")
    f=font.Font(weight="normal",family="times new roman",size=20)
    frame1.pack() 

    img5 = Image.open("live.jpg")
    img5 = img5.resize((500,150))
    img5= ImageTk.PhotoImage(img5)
    l=Label(e,image=img5).place(relx=.35,rely=.01)

    frame=Frame(e,width=500,height=250,bg="#FFDEAD").place(relx=.51,rely=.3)
    f=font.Font(e,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="STAFF LOGIN",font=f,bg="#FFDEAD").place(relx=.60,rely=.3)
    
    f=font.Font(e,weight="bold",family="times new roman",size=15)
    l=Label(frame,text="User Name:",font=f,bg="#FFDEAD").place(relx=.55,rely=.4)
    l=Label(frame,text="Password   :",font=f,bg="#FFDEAD").place(relx=.55,rely=.5)
    
    l11=Entry(frame)
    l11.place(relx=.64,rely=.41)
    l22=Entry(frame)
    l22.place(relx=.64,rely=.51)

    frame2=Frame(e,width=500,height=250,bg="#FFDEAD").place(relx=.10,rely=.3)
    f=font.Font(e,weight="bold",family="times new roman",size=20)
    l=Label(frame2,text="ADMIN LOGIN",font=f,bg="#FFDEAD").place(relx=.22,rely=.3)
    
    f=font.Font(e,weight="bold",family="times new roman",size=15)
    l=Label(frame2,text="User Name:",font=f,bg="#FFDEAD").place(relx=.18,rely=.4)
    l=Label(frame2,text="Password   :",font=f,bg="#FFDEAD").place(relx=.18,rely=.5)
    
    l1=Entry(frame2)
    l1.place(relx=.28,rely=.41)
    l2=Entry(frame2)
    l2.place(relx=.28,rely=.51)

    f1=font.Font(weight="bold",family="Bodoni MT",size=14)
    b1=Button(frame,text="Login",font=f1,bg="#FF6347",activebackground="#FC92C4",width=10,command=lambda:stf_log(l11.get(),l22.get(),e))
    b1.place(relx=.64,rely=.57)
    b2=Button(frame,text="Admin Login",font=f1,bg="#FF6347",activebackground="#FC92C4",width=10,command=lambda:ad_log(l1.get(),l2.get(),e))
    b2.place(relx=.24,rely=.57)
    f1=font.Font(family="Times New Roman",size=20)
    x=Label(e,text=" @CopyRight Madhan Rajan",fg="red",bg="#BEE4ED",font=f1).place(relx=.39,rely=.87)
    e.mainloop()
def std_page(e,data):
    e.destroy() 
    e=Tk()
    e.geometry("1500x900")
    e.title("EMP")
    frame1=Frame(e,width=1500,height=900,bg="#BEE4ED")
    f=font.Font(weight="normal",family="times new roman",size=20)
    img5 = Image.open("st.webp")
    img5 = img5.resize((300,300))
    img5= ImageTk.PhotoImage(img5)
    l=Label(e,image=img5).place(relx=.03,rely=.01)
    f1=font.Font(weight="bold",family="Bodoni MT",size=20)
    data1=data[0]
    a="Name : "+data1[0]
    label=Label(frame1,text=a,font=f1,bg="#BEE4ED")
    label.place(relx=.39,rely=.2)
    a="Age : "+str(data1[1])
    label=Label(frame1,text=a,font=f1,bg="#BEE4ED")
    label.place(relx=.39,rely=.3)
    a="Education : "+data1[2]
    label=Label(frame1,text=a,font=f1,bg="#BEE4ED")
    label.place(relx=.39,rely=.4)
    a="Course: "+data1[3]
    label=Label(frame1,text=a,font=f1,bg="#BEE4ED")
    label.place(relx=.39,rely=.5)
    a="Phone No : "+str(data1[4])
    label=Label(frame1,text=a,font=f1,bg="#BEE4ED")
    label.place(relx=.39,rely=.6)  
   
    frame1.pack()
  

    f1=font.Font(family="Times New Roman",size=20)
    x=Label(e,text="LIVE WIRE",fg="red",bg="#BEE4ED",font=f1).place(relx=.45,rely=.01)

    f1=font.Font(family="Times New Roman",size=20)
    x=Label(e,text=" @CopyRight Madhan Rajan",fg="red",bg="#BEE4ED",font=f1).place(relx=.39,rely=.87)
    e.mainloop() 


def std_login(e):
    e.destroy() 
    e=Tk()
    e.geometry("1500x900")
    e.title("EMP")
    frame1=Frame(e,width=1500,height=900,bg="#BEE4ED")
    f=font.Font(weight="normal",family="times new roman",size=20)
    frame1.pack()

    img5 = Image.open("live.jpg")
    img5 = img5.resize((500,150))
    img5= ImageTk.PhotoImage(img5)
    l=Label(e,image=img5).place(relx=.35,rely=.01)

    frame=Frame(e,width=500,height=250,bg="#FFE4E1").place(relx=.35,rely=.3)
    f=font.Font(e,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="STUDENT LOGIN",font=f,bg="#FFE4E1").place(relx=.45,rely=.3)
    
    f=font.Font(e,weight="bold",family="times new roman",size=15)
    l=Label(frame,text="User Name:",font=f,bg="#FFE4E1").place(relx=.38,rely=.4)
    l=Label(frame,text="Password   :",font=f,bg="#FFE4E1").place(relx=.38,rely=.5)
    
    l1=Entry(frame)
    l1.place(relx=.48,rely=.41)
    l2=Entry(frame)
    l2.place(relx=.48,rely=.51)
    def spage(e):
        import pymysql as mysql
        UserName =l1.get()
        Password=l2.get()
        connection = mysql.connect(host="localhost", user="root", password="livewire", database="proemp")
        cursor = connection.cursor()
        query = "SELECT * FROM stdreg WHERE Name=%s and PhoneNo=%s"
        cursor.execute(query, (UserName,Password))
    
        result = cursor.fetchall()
        print(result)
        if result:
            std_page(e,result)
        else:
            messagebox.showerror( "Incorrect", "Invalid UserId and Password")

    f1=font.Font(weight="bold",family="Bodoni MT",size=14)
    b1=Button(frame,text="Login",font=f1,bg="#FF6347",activebackground="#FC92C4",width=10,command=lambda:spage(e))
    b1.place(relx=.48,rely=.57)
    f1=font.Font(family="Times New Roman",size=20)
    x=Label(e,text=" @CopyRight Madhan Rajan",fg="red",bg="#BEE4ED",font=f1).place(relx=.39,rely=.87)
    e.mainloop()



def student(e): 
    e.destroy()
    e=Tk()
    e.geometry("1500x900")
    e.title("EMP")
    frame1=Frame(e,width=1500,height=900,bg="#BEE4ED")
    f=font.Font(weight="normal",family="times new roman",size=20)
    frame1.pack()
    t1="""Livewire's on-demand courses in emerging technologies
      give you the knowledge you need to stay ahead of the curve and 
      succeed in today's fast-paced world."""
    x=Label(frame1,text=t1,font=f,bg="#BEE4ED")
    x.place(relx=.2,rely=.23)
    img5 = Image.open("live.jpg")
    img5 = img5.resize((500,150))
    img5= ImageTk.PhotoImage(img5)
    l=Label(e,image=img5).place(relx=.3,rely=.01)
    img = Image.open("py.png")
    img = img.resize((200,200))
    img = ImageTk.PhotoImage(img)
    l=Label(e,image=img).place(relx=.01,rely=0.61)
    img1= Image.open("ja.png")
    img1 = img1.resize((200,200))
    img1= ImageTk.PhotoImage(img1)
    l=Label(e,image=img1).place(relx=.2,rely=0.61)
    img2= Image.open("se.png")
    img2 = img2.resize((200,200))
    img2= ImageTk.PhotoImage(img2)
    l=Label(e,image=img2).place(relx=.4,rely=0.61)
    img3= Image.open("as.png")
    img3 = img3.resize((200,200))
    img3= ImageTk.PhotoImage(img3)
    l=Label(e,image=img3).place(relx=.6,rely=0.61)
    img4= Image.open("web.png")
    img4 = img4.resize((200,200))
    img4= ImageTk.PhotoImage(img4)
    l=Label(e,image=img4).place(relx=.8,rely=0.61)

    f1=font.Font(weight="bold",family="Century",size=20)
    b=Button(frame1,text="Login",font=f1,bg="#FF6347",activebackground="#FC92C4",width=15,command=lambda:std_login(e))
    b.place(relx=.4,rely=.4)
    
    f1=font.Font(family="Times New Roman",size=20)
    x=Label(e,text=" @CopyRight Madhan Rajan",fg="red",bg="#BEE4ED",font=f1).place(relx=.39,rely=.87)
    e.mainloop()

def Home():
    e=Tk()
    e.geometry("1500x900")
    e.title("EMP")
    frame1=Frame(e,width=1500,height=900,bg="#BEE4ED")
    f=font.Font(weight="normal",family="times new roman",size=20)
    frame1.pack()
    t1="""Livewire represents an electrifying blend of high-end skills, 
    expert trainers, and individual attention. Our goal as a part of CADD Centre, 
    a global skill development conglomerate, is to bring these three factors together and prepare you, 
    the students, for exciting careers in emerging technologies."""
    x=Label(frame1,text=t1,font=f,bg="#BEE4ED")
    x.place(relx=.1,rely=.6)
   
    img = Image.open("live.jpg")
    img = img.resize((500,150))
    img = ImageTk.PhotoImage(img)
    l=Label(e,image=img).place(relx=.3,rely=.09)

    f1=font.Font(weight="bold",family="Bodoni MT",size=20)
    b=Button(frame1,text="Student",font=f1,bg="#FF6347",activebackground="#FC92C4",width=15,command=lambda:student(e))
    b.place(relx=.3,rely=.4)
    b1=Button(frame1,text="Staff",font=f1,bg="#FF6347",activebackground="#FC92C4",width=15,command=lambda:staff_login(e))
    b1.place(relx=.5,rely=.4)
    f1=font.Font(family="Times New Roman",size=20)
    x=Label(e,text=" @CopyRight Madhan Rajan",fg="red",bg="#BEE4ED",font=f1).place(relx=.39,rely=.87)
    e.mainloop()

Home()