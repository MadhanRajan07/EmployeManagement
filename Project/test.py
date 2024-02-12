""" 
 import tkinter
from tkinter import*
from tkinter import ttk,font
from PIL import ImageTk,Image
def stf_page():
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

   
    t1=Livewire's on-demand courses in emerging technologies
      give you the knowledge you need to stay ahead of the curve and 
      succeed in today's fast-paced world.
    x=Label(frame1,text=t1,font=f,bg="#BEE4ED")
    x.place(relx=.23,rely=.23)
    f1=font.Font(weight="bold",family="Century",size=20)
    b1=Button(frame1,text="Register",font=f1,bg="#FF6347",activebackground="#FC92C4",width=15)
    b1.place(relx=.42,rely=.38)
    f2=font.Font(family="Times New Roman",size=20)
    x=Label(e,text=" @CopyRight Madhan Rajan",fg="red",bg="#BEE4ED",font=f2).place(relx=.39,rely=.87)
    e.mainloop()
stf_page() """


""" win = tk.Tk()
win.title("GST Calculator")
win.geometry("400x300")
win.minsize(400,300)
win.maxsize(400,300)
menubar = tk.Menu(win)

def onTouch():
    webbrowser.open_new_tab(r'http://vaibhavpathak.diagodevelopers.dx.am/')

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="About Developer", command = onTouch)

menubar.add_cascade(label="Help", menu=filemenu)
win.config(menu=menubar)

label_frame = ttk.LabelFrame(win, width=70)
label_frame.grid(row=0,column=0,padx=55,pady=70)
gst_label = ttk.Label(label_frame, text="Enter Your Amount : ")
gst_label.grid(row=0,column=0,padx=0,pady=3,sticky=tk.W)
gst_persent = ttk.Label(label_frame, text="Select Your GST Percent (%) : ")
gst_persent.grid(row=1, column=0,sticky=tk.W)
gst_amount = tk.StringVar()
gst_entry = ttk.Entry(label_frame, width=20, textvariable=gst_amount)
gst_entry.grid(row=0,column=1,padx=0, pady=5)
gst_entry.focus()
get_percentcomo = ttk.Combobox(label_frame, width=17,state='readonly')
get_percentcomo.grid(row=1,column=1)
get_percentcomo['values'] = (5,12,18,28)
get_percentcomo.current(0)
def onClick():
    user_amount = gst_amount.get()
    user_gst = get_percentcomo.get()
    if user_amount != "":
        try:
            gst = int(user_amount)
        except ValueError:
            wrong = m_box.showerror("Warning !", "Amounts are only in Digits !")
            gst_entry.delete(first=0, last=100)
            return wrong
        else:
            if int(user_amount) != 0:
                got_result = (gst / 100) * int(user_gst)
                right = m_box.showinfo("Successfully Calculated", f"Your GST Charge is {got_result}")
                gst_entry.delete(first=0, last=100)
                return right
            else:
                wrong2 = m_box.showerror("Warning !", "GST Amount is Can't be Zero !")
                gst_entry.delete(first=0, last=100)
                return wrong2
    else:
        wrong3 = m_box.showerror("Warning !", "GST Amount Can't be Blank")
        gst_entry.delete(first=0, last=100)
        return wrong3

cal_percent = ttk.Button(label_frame, text="Calculate GST", command=onClick)
cal_percent.grid(row=3, columnspan=3, padx=0, pady=10)
win.mainloop()

 """
""" import tkinter as tk

def calculate_gst():
    try:
        # Get the input values from the entry fields
        amount = float(amount_entry.get())
        rate = float(rate_entry.get())
        
        # Calculate GST
        gst_amount = (amount * rate) / 100
        total_amount = amount + gst_amount
        
        # Update the result labels
        gst_label.config(text=f"GST Amount: {gst_amount:.2f}")
        total_label.config(text=f"Total Amount: {total_amount:.2f}")
    except ValueError:
        # Handle non-numeric input
        gst_label.config(text="Invalid Input")
        total_label.config(text="Invalid Input")

# Create the main application window
app = tk.Tk()
app.title("GST Calculator")

# Create labels and entry fields
amount_label = tk.Label(app, text="Enter Amount:")
amount_label.place(relx=.37, rely=.20)

amount_entry = tk.Entry(app)
amount_entry.place(relx=.52, rely=.20)

rate_label = tk.Label(app, text="Enter GST Rate (%):")
rate_label.place(relx=.37, rely=.30)

rate_entry = tk.Entry(app)
rate_entry.place(relx=.52, rely=.30)

gst_button = tk.Button(app, text="Calculate GST", command=calculate_gst)
gst_button.place(relx=.45, rely=.40)

gst_label = tk.Label(app, text="")
gst_label.place(relx=.45, rely=.50)

total_label = tk.Label(app, text="")
total_label.place(relx=.45, rely=.60)

# Start the GUI event loop
app.mainloop()
app = tk.Tk()
app.title("GST Calculator")
app.geometry("1500x720") """

"""
    img1 = Image.open("Networking.jpg")
    img1 = img1.resize((400,300))
    img1 = ImageTk.PhotoImage(img1)
    l=Label(a,image=img1).place(relx=0.02,rely=0.17) """
""" import pymysql as mysql

UserName = "Madhan"

# Establishing connection
connection = mysql.connect(host="localhost", user="root", password="livewire", database="proemp")
cursor = connection.cursor()

# Using parameterized query to avoid SQL injection and syntax errors
query = "SELECT Name, PhoneNo FROM stdreg WHERE Name=%s"
cursor.execute(query, (UserName,))

# Fetching results
result = cursor.fetchall()

# Printing results
print("success")
for x in result:
    print("\t", x)

# Closing connection
cursor.close()
connection.close() """
