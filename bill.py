from tkinter import *
import math
import random
from tkinter import messagebox
import os
# import messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        self.root.iconbitmap(r"C:\Users\User\Desktop\kinter\images\icon.ico")

        # bg_color = "#074463"
        title = Label(self.root, text="Billing Software",bd=12, relief=GROOVE, bg="#074463", fg= "white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # ===============================================variable=================================


        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.loshan = IntVar()

        self.rice = IntVar()
        self.dal = IntVar()
        self.wheat = IntVar()
        self.oil = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        # ========================total price============

        self.product_price = StringVar()
        self.g_price = StringVar()
        self.cold_drink_price = StringVar()

        self.product_tax = StringVar()
        self.g_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # ================================customer============================

        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()




        # ===========================Customer detaile frame==============================================

        F1 = LabelFrame(self.root,bd=10, relief=GROOVE, text = "Customer Detailes", font=("times new roman", 30, "bold"),bg="#074463", fg= "gold")
        F1.place(x=0, y=80, relwidth=1)

        cname_lb1 = Label(F1, text="Customer Name",bg="#074463",fg="white" , font=("times new roman",18,"bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1,width=15, textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)

        cphn_lb1 = Label(F1, text=" Phone Number",bg="#074463",fg="white" , font=("times new roman",18,"bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        cbill_lb1 = Label(F1, text=" Bill",bg="#074463",fg="white" , font=("times new roman",18,"bold")).grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1,width=15,textvariable=self.bill_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        bill_btn = Button(F1, text="Search",command=self.find_bill,textvariable=self.search_bill, width=10, font="arial 12 bold").grid(row=0, column=6, pady=10,padx=10)

        # ============================ products=============================================================


        F2 = LabelFrame(self.root,bd=10, relief=GROOVE, text = "Products", font=("times new roman", 20, "bold"),bg="#074463", fg= "gold")
        F2.place(x=5, y=180,width=325, height=400)

        bath_lb = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10,textvariable=self.soap, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10,pady=10)

        face_cream_lb = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10,pady=10)

        face_w_lb = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        face_w_txt = Entry(F2, width=10, textvariable=self.face_wash , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10,pady=10)

        hair_s_lb = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hair_s_txt = Entry(F2, width=10, textvariable=self.spray , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10,pady=10)

        hair_g_lb = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hair_g_txt = Entry(F2, width=10, textvariable=self.gel , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10,pady=10)

        body_lb = Label(F2, text="Body Loshan", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(F2, width=10, textvariable=self.loshan , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10,pady=10)


        # ============================G products=============================================================


        F3 = LabelFrame(self.root,bd=10, relief=GROOVE, text = "G Products", font=("times new roman", 20, "bold"),bg="#074463", fg= "gold")
        F3.place(x=340, y=180,width=325, height=400)

        g1_lb = Label(F3, text="Dal", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.dal , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10,pady=10)

        g2_lb = Label(F3, text="Rice", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.rice , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10,pady=10)

        g3_lb = Label(F3, text="Wheat", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.wheat , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10,pady=10)

        g4_lb = Label(F3, text="sugar", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10,  textvariable=self.sugar, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10,pady=10)

        g5_lb = Label(F3, text="tea", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10,  textvariable=self.tea, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10,pady=10)

        g6_lb = Label(F3, text="oil", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10,  textvariable=self.oil, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10,pady=10)

        # ============================cold drinks=============================================================


        F4 = LabelFrame(self.root,bd=10, relief=GROOVE, text = "Cold Drinks", font=("times new roman", 20, "bold"),bg="#074463", fg= "gold")
        F4.place(x=670, y=180,width=325, height=400)

        c1_lb = Label(F4, text="Maza", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10, textvariable=self.maza, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=0, column=2,padx=10,pady=10)

        c2_lb = Label(F4, text="Cock", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10, textvariable=self.cock, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=1, column=2,padx=10,pady=10)

        c3_lb = Label(F4, text="Frooti", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10, textvariable=self.frooti, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=2, column=2,padx=10,pady=10)

        c4_lb = Label(F4, text="Thumbs up", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10, textvariable=self.thumbsup, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=3, column=2,padx=10,pady=10)

        c5_lb = Label(F4, text="Limca", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10, textvariable=self.limca, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=4, column=2,padx=10,pady=10)

        c6_lb = Label(F4, text="Sprite", font=("times new roman", 16, "bold"),bg="#074463",fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10, textvariable=self.sprite, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=5, column=2,padx=10,pady=10)



        # ====================================Bill Aread==========================
        F5 = Frame(self.root,bd=10, relief=GROOVE)
        F5.place(x=1010, y=200,width=325, height=360)

        bill_title = Label(F5, text="Bill Area", font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1) 


        # ==========================================Button Frame==========================


        F6 = LabelFrame(self.root,bd=10, relief=GROOVE, text = "Bill Menu", font=("times new roman", 15, "bold"),bg="#074463", fg= "gold")
        F6.place(x=0, y=560,relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total price of product" ,font=("times new roman",14,"bold")).grid(row=0, column=0,padx=20,pady=1,sticky="w")
        m1_txt = Entry(F6,width=18, textvariable=self.product_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0, column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text="Total price of g product" ,font=("times new roman",14,"bold")).grid(row=1, column=0,padx=20,pady=1,sticky="w")
        m2_txt = Entry(F6,width=18, textvariable=self.g_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1, column=1,padx=10,pady=1)

        m3_lbl = Label(F6, text="Total price of cold drinks" ,font=("times new roman",14,"bold")).grid(row=2, column=0,padx=20,pady=1,sticky="w")
        m3_txt = Entry(F6,width=18, textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2, column=1,padx=10,pady=1)


        # =================================================


        c1_lbl = Label(F6, text="product tax" ,font=("times new roman",14,"bold")).grid(row=0, column=2,padx=20,pady=1,sticky="w")
        c1_txt = Entry(F6,width=18, textvariable=self.product_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0, column=3,padx=10,pady=1)

        c2_lbl = Label(F6, text=" g product tax" ,font=("times new roman",14,"bold")).grid(row=1, column=2,padx=20,pady=1,sticky="w")
        c2_txt = Entry(F6,width=18, textvariable=self.g_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1, column=3,padx=10,pady=1)

        c3_lbl = Label(F6, text=" cold drinks tax " ,font=("times new roman",14,"bold")).grid(row=2, column=2,padx=20,pady=1,sticky="w")
        c3_txt = Entry(F6,width=18, textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2, column=3,padx=10,pady=1)


        btn_F = Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)

        total_btn = Button(btn_F, command=self.total, text="Total", bg="cadetblue", fg="white",pady=15, width=11, font="arial 12 bold").grid(row=0, column=0,padx=5,pady=5)
        Gbill = Button(btn_F, command=self.bill_area, text="Generate Bill", bg="cadetblue", fg="white",pady=15, width=11, font="arial 12 bold").grid(row=0, column=1,padx=5,pady=5)
        Clear = Button(btn_F, text="Clear", bg="cadetblue", fg="white",pady=15, width=11, font="arial 12 bold").grid(row=0, column=2,padx=5,pady=5)
        Exit = Button(btn_F, text="Exit", bg="cadetblue", fg="white",pady=15, width=11, font="arial 12 bold").grid(row=0, column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        
        self.total_product_price =float(((self.soap.get()*40)+(self.face_cream.get()*120)+(self.face_wash.get()*60)+(self.spray.get()*180)+(self.gel.get()*140)+(self.loshan.get()*180)))
        self.product_price.set("Rs. " + str(self.total_product_price))

        self.total_g_price =float(((self.dal.get()*120)+(self.rice.get()*40)+(self.oil.get()*100)+(self.sugar.get()*180)+(self.tea.get()*40)+(self.wheat.get()*80)))
        self.g_price.set("Rs. " + str(self.total_g_price))

        self.total_cold_drink_price =float(((self.maza.get()*90)+(self.cock.get()*85)+(self.sprite.get()*96)+(self.thumbsup.get()*100)+(self.limca.get()*65)+(self.frooti.get()*75)))
        self.cold_drink_price.set("Rs. " + str(self.total_cold_drink_price))

        # self.total_product_tax = float((self.total_product_price.get()*0.18))
        self.product_tax.set("Rs. " + str(self.total_product_price*0.18))
        self.g_tax.set("Rs. " + str(self.total_g_price*0.18))
        self.cold_drink_tax.set("Rs. " + str(self.total_cold_drink_price*0.18))

        self.billing_price = float((self.total_product_price)+(self.total_g_price)+(self.total_cold_drink_price)+(self.total_product_price*0.18)+(self.total_g_price*0.18)+(self.total_cold_drink_price*0.18))
        

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END, "\tWELCOME SKY RETAIL\n")
        self.textarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.textarea.insert(END, f"\n===================================")
        self.textarea.insert(END, f"\nprodacts\t\tQty\t  prc")
        self.textarea.insert(END, f"\n===================================")


    def bill_area(self):
        self.welcome_bill()
        # products
        if self.soap.get()!=0 :
            self.textarea.insert(END, f"\nBath soap\t\t{self.soap.get()}\t  {(self.soap.get()*40)}")
        if self.face_cream.get()!=0 :
            self.textarea.insert(END, f"\nFace Cream\t\t{self.face_cream.get()}\t  {(self.face_cream.get()*120)}")
        if self.face_wash.get()!=0 :
            self.textarea.insert(END, f"\nFace Wash\t\t{self.face_wash.get()}\t  {(self.face_wash.get()*60)}")
        if self.spray.get()!=0 :
            self.textarea.insert(END, f"\nHair spary\t\t{self.spray.get()}\t  {(self.spray.get()*180)}")
        if self.gel.get()!=0 :
            self.textarea.insert(END, f"\nHair Gel\t\t{self.gel.get()}\t  {(self.gel.get()*140)}")
        if self.loshan.get()!=0 :
            self.textarea.insert(END, f"\nBath soap\t\t{self.loshan.get()}\t  {(self.loshan.get()*180)}")

        

        if self.dal.get()!=0 :
            self.textarea.insert(END, f"\nDal\t\t{self.dal.get()}\t  {(self.soap.get()*40)}")
        if self.rice.get()!=0 :
            self.textarea.insert(END, f"\nRice\t\t{self.rice.get()}\t  {(self.rice.get()*40)}")
        if self.oil.get()!=0 :
            self.textarea.insert(END, f"\nOil\t\t{self.oil.get()}\t  {(self.oil.get()*100)}")
        if self.wheat.get()!=0 :
            self.textarea.insert(END, f"\nWheat\t\t{self.wheat.get()}\t  {(self.wheat.get()*180)}")
        if self.tea.get()!=0 :
            self.textarea.insert(END, f"\nTea\t\t{self.tea.get()}\t  {(self.tea.get()*40)}")
        if self.sugar.get()!=0 :
            self.textarea.insert(END, f"\nSugar\t\t{self.sugar.get()}\t  {(self.sugar.get()*80)}")

        
        if self.maza.get()!=0 :
            self.textarea.insert(END, f"\nMaza\t\t{self.maza.get()}\t  {(self.maza.get()*90)}")
        if self.cock.get()!=0 :
            self.textarea.insert(END, f"\nCock\t\t{self.cock.get()}\t  {(self.cock.get()*85)}")
        if self.frooti.get()!=0 :
            self.textarea.insert(END, f"\nFrooti\t\t{self.frooti.get()}\t  {(self.frooti.get()*96)}")
        if self.thumbsup.get()!=0 :
            self.textarea.insert(END, f"\nThumbs Up\t\t{self.thumbsup.get()}\t  {(self.thumbsup.get()*100)}")
        if self.limca.get()!=0 :
            self.textarea.insert(END, f"\nLimca\t\t{self.limca.get()}\t  {(self.limca.get()*65)}")
        if self.sprite.get()!=0 :
            self.textarea.insert(END, f"\nSprite\t\t{self.sprite.get()}\t  {(self.sprite.get()*75)}")

        self.textarea.insert(END,"\n-----------------------------------")
        self.textarea.insert(END, f"\nTotal price\t\t\t{self.billing_price}")
        self.save_bill()
        

        # ****************************saving of bill*******************************************************
    def save_bill(self):
        op = messagebox.askyesno("save Bill","Do you want to save the bil?")
        if op>0:
            self.bill_data = self.textarea.get('1.0',END)
            f1 = open("Bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close
            messagebox.showinfo("saved", f"Bill no. : {self.bill_no.get()} saved successfully")
        else:
            return


root = Tk()
obj = Bill_App(root)
root.mainloop()

