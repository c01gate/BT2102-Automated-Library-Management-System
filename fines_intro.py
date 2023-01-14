import tkinter as tk
from tkinter import messagebox
import pymysql
import datetime
from datetime import date


con = pymysql.connect(
    host='localhost',
    user='root',
    password='1145joellenG.', #CHANGE THIS
    database='library'
    )

class fine_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Fines")
        tk.Label(self.root, text="Select one of the options below: ").grid(row=0,columnspan=2)
        tk.Label(self.root, text="Fine Payment").grid(row=1,column=0)
        btn_pay = tk.Button(
            self.root,
            text="Payment",
            command=lambda:self.payment()
            )
        btn_pay.grid(row=1,column=1)

        btn_return_to_menu = tk.Button(
            self.root,
            text = "Back to main menu",
            width = 10, height = 2,
            command=lambda:self.root.destroy())
        btn_return_to_menu.grid(row = 2, columnspan = 2)

    def payment(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = payment_intro(self.new_window)
        
class payment_intro:
    def __init__(self,root):
        self.root = root
        self.root.title("Fines")
        start = tk.Label(self.root, text="To Pay a Fine, Please Enter Information Below:")
        start.grid(row = 0, columnspan=2)
        tk.Label(
            self.root, 
            text='Membership ID', 
            ).grid(row=1, column=0, pady=5)

        tk.Label(
            self.root, 
            text='Payment Date', 
            ).grid(row=2, column=0, pady=5)
        tk.Label(
            self.root, 
            text='Payment Amount', 
            ).grid(row=3, column=0, pady=5)

        self.mem_id = tk.Entry(self.root, width=30)
        self.mem_id.insert(0,"A unique alphanumeric id that distinguishes every member")
        self.mem_id.grid(row=1,column=1)
        self.date = tk.Entry(self.root, width=30)
        self.date.insert(0,"Date Payment Received DD/MM/YYYY")
        self.date.grid(row = 2, column = 1)
        self.amt = tk.Entry(self.root, width=30)
        self.amt.insert(0,"Total fine amount")
        self.amt.grid(row=3,column=1)
        paid_btn = tk.Button(self.root, text="Pay Fine", padx=20, pady=10, command=lambda:self.paid()
            )
        paid_btn.grid(row=4,column=0)
        btn_return_to_menu = tk.Button(
            self.root,
            text = "Back to Fines menu",
            padx=20, pady = 10,
            command=lambda:self.root.destroy())
        btn_return_to_menu.grid(row = 4, column = 1)

    def paid(self):
        mem_id = self.mem_id.get()
        pay_date = self.date.get()
        amt = self.amt.get()
        print(pay_date)
        try:
            pay_date = datetime.datetime.strptime(pay_date,'%d/%m/%Y').date()
        except:
            messagebox.showwarning("showwarning","Not in correct date format!")
            return
        try:
            amt = int(amt)
        except:
            messagebox.showwarning("showwarning","fines are integers!")
            return
            
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        self.new_window = tk.Toplevel(self.root)
        self.app = temp_paid(self.new_window, mem_id,pay_date,amt)

class temp_paid:
    def __init__(self,root,mem_id,pay_date,amt):
        self.root = root
        self.mem_id = mem_id
        self.pay_date = pay_date
        self.amt = amt
        tk.Label(self.root, text = "Please confirm details to be correct: ").grid(row = 0, columnspan=2)
        tk.Label(self.root, text = f'Payment Due: \n ${amt}').grid(row=1,column=0)
        tk.Label(self.root, text = f'{mem_id}').grid(row=1,column=1)
        tk.Label(self.root, text = 'Exact fee only!').grid(row=2,column=0)
        tk.Label(self.root, text = f'{pay_date}').grid(row=2,column=1)

        cfm_btn = tk.Button(self.root, text="Confirm Payment", padx=20, pady=10, command=lambda:self.final_pay())
        cfm_btn.grid(row=3,column=0)
        btn_return_to_menu = tk.Button(
            self.root,
            text = "Back to Payment Function",
            padx=20, pady = 10,
            command=lambda:self.root.destroy())
        btn_return_to_menu.grid(row = 3, column = 1)

    def final_pay(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                try:
                    t = f'SELECT * FROM library.fine WHERE membership_id_fined = "{self.mem_id}"; '
                    cursor.execute(t)
                    result = cursor.fetchone()
                    print(result)
                except:
                    messagebox.showwarning("showwarning", "Member has no fine!")
                    return
                if result[2] != self.amt:
                    messagebox.showwarning("showwarning", "Incorrect fine payment amount!")
                    return
                else:
                    j = 'UPDATE library.fine SET last_updated_date = %s,amount_fined = 0, payment_date=%s, transaction_id = %s WHERE membership_id_fined = %s; '
                    k = 'INSERT INTO `library`.`fine payment` (`membership_id_paying`, `pay_date`, `amount_paid`) VALUES (%s, %s, %s); '
                    cursor.execute(k, (self.mem_id,self.pay_date,self.amt))
                    con.commit()
                    cursor.execute('SELECT MAX(transaction_id) FROM library.`fine payment`;' )
                    trans_id = cursor.fetchone()
                    cursor.execute(j, (self.pay_date, self.pay_date, trans_id, self.mem_id))
                    con.commit()
                    messagebox.showinfo("showinfo", "Paid")
                    self.root.destroy()
                    
                    
        

        
        
        

        
        
        
        
        
        
        
    
        

        
        
        
        
