import tkinter as tk
from tkinter import messagebox
import pymysql
from datetime import date
import datetime

con = pymysql.connect(
    host='localhost',
    user='root',
    password='1145joellenG.', #CHANGE THIS
    database='library'
    )

class loan_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Loans")
        tk.Label(self.root, text="Select one of the options below: ").grid(row=0,columnspan=2)
        tk.Label(self.root, text="Book borrowing").grid(row=1,column=0)
        tk.Label(self.root, text="Book returning").grid(row=2,column=0)
        btn_borrow = tk.Button(
            self.root,
            text="Borrow",
            command=self.borrow_page
            )
        btn_borrow.grid(row=1,column=1)
        btn_return = tk.Button(
            self.root,
            text="Return",
            command=self.return_page
            )
        btn_return.grid(row=2,column=1)

        btn_return_to_menu = tk.Button(
            self.root,
            text = "Back to main menu",
            width = 10, height = 2,
            command=lambda:self.root.destroy())
        btn_return_to_menu.grid(row = 3, columnspan = 2)
    def return_page(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = return_intro(self.new_window)
    def borrow_page(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = borrow_intro(self.new_window)

class borrow_intro:
    def __init__(self, root):
        self.root = root
        self.root.title("Borrow")
        start = tk.Label(self.root, text="To Borrow a Book, Please Enter Information Below:")
        start.grid(row = 0, columnspan=2)
        tk.Label(
            self.root, 
            text='Accession Number', 
            ).grid(row=1, column=0, pady=5)

        tk.Label(
            self.root, 
            text='Membership ID', 
            ).grid(row=2, column=0, pady=5)

        self.acc_num = tk.Entry(self.root, width=30)
        self.acc_num.insert(0,"Used to identify an instance of book")
        self.acc_num.grid(row=1,column=1)
        self.mem_id = tk.Entry(self.root, width=30)
        self.mem_id.insert(0,"A unique alphanumeric id that distinguishes every member")
        self.mem_id.grid(row = 2, column = 1)
        borrow_btn = tk.Button(self.root, text="Borrow book", padx=20, pady=10, command=lambda:self.borrow()
            )
        borrow_btn.grid(row=3,column=0)
        btn_return_to_menu = tk.Button(
            self.root,
            text = "Back to main menu",
            padx=20, pady = 10,
            command=lambda:self.root.destroy())
        btn_return_to_menu.grid(row = 3, column = 1)

    def borrow(self):
        acc_num = self.acc_num.get()
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                try:
                    t = 'SELECT * FROM library.book WHERE accession_number = %s; '
                    cursor.execute(t, acc_num)
                    result = cursor.fetchone()
                    print(result)
                    self.new_window = tk.Toplevel(self.root)
                    self.app = temp_borrow(self.new_window, result,self.mem_id.get())
                    con.commit()
                except:
                    messagebox.showwarning("showwarning", "Book does not exist!")
                    return
class temp_borrow:
    def __init__(self, root,result,mem):
        self.root = root
        self.root.title("Confirmation")
        tk.Label(self.root, text = "Please confirm loan details to be correct: ").grid(row = 0, columnspan=2)
        self.result = result
        self.mem_id = mem
        for i in range(4):
            tk.Label(self.root, text = f"{self.result[i]}").grid(row=i+1)
        confirm_btn = tk.Button(self.root, text = "Confirm Borrow", padx=20,pady=10,command=lambda:self.confirm())
        confirm_btn.grid(row = 6,column = 0)
        back_btn = tk.Button(self.root, text = "Back to borrow function", padx=20,pady=10,command=lambda:self.root.destroy())
        back_btn.grid(row = 6, column = 1)

    def confirm(self):
        con = pymysql.connect(
            host='localhost',
            user='root', 
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                if self.check_reserved(self.result[0],self.mem_id):
                    messagebox.showwarning("showwarning", "ERROR! \n Book currently reserved by someone else.")
                    self.root.destroy()
                    return
                if self.check_loaned(self.result[0]):
                    messagebox.showwarning("showwarning", f"ERROR! \n Book currently on Loan until: {self.check_loaned(self.result[0])}")
                    self.root.destroy()
                    return
                if self.check_quota(self.mem_id):
                    messagebox.showwarning("showwarning", "ERROR! \n Member loan quota exceeded.")
                    self.root.destroy()
                    return
                if self.check_fines(self.mem_id):
                    messagebox.showwarning("showwarning", "ERROR! \n Member has outstanding fines.")
                    self.root.destroy()
                    return
                else:
                    self.delete_self_reserved(self.result[0], self.mem_id)
                    curr_date = date.today()
                    t = f'UPDATE library.book SET borrow_date = "{date.today()}",due_date = "{date.today() + datetime.timedelta(days=14)}",membership_id_borrowed = "{self.mem_id}",return_date=NULL WHERE accession_number = "{self.result[0]}"; '
                    cursor.execute(t)
                    con.commit()
                    try:
                        t = 'DELETE FROM library.reservation WHERE membership_id = %s AND accession_number = %s '
                        cursor.execute(t, (self.mem_id, self.result[0]))
                        con.commit()
                    except:
                        pass
        messagebox.showinfo("showinfo", "Book borrowed")
        self.root.destroy()

    def check_loaned(self,acc_num):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                
                curr_date = date.today()
                t = 'SELECT return_date,due_date,membership_id_borrowed,borrow_date FROM library.book WHERE accession_number = %s; '
                cursor.execute(t, acc_num)
                result = cursor.fetchone()
                #current date > return date and due_date
                
                if result[3]: #if someone borrow before
                    if result[0]:
                        if result[0] < result[3]: #if borrow date >= return date #if not returned
                            return result[1]
                        else:
                            return False
                    else: #first time borrowed but not returned
                        return result[1]
                else:
                    return False

        
    def check_quota(self,mem_id):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                try:
                    t = 'SELECT accession_number FROM library.book WHERE membership_id_borrowed = %s; '
                    cursor.execute(t, mem_id)
                    result = cursor.fetchall()
                    print(len(result))
                    if len(result) >= 2:
                        return True
                    else:
                        return False
                except:
                    return False


    def check_fines(self,mem_id):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                try:
                    t = 'SELECT * FROM library.fine WHERE membership_id_fined = %s; '
                    cursor.execute(t, mem_id)
                    result = cursor.fetchone()
                    print(result)
                    print("here")
                    if result[2]:
                        return True
                    else:
                        pass
                    
                    t2 = f'SELECT * FROM library.book WHERE membership_id_borrowed = "{mem_id}" AND due_date < {date.today()} ; '
                    cursor.execute(t2)
                    result2 = cursor.fetchall()
                    print(result2)
                    print("here2")
                    if result2:
                        return True
                    else:
                        return False
                except:
                    return False

    def delete_self_reserved(self, acc_num, mem_id):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                try:
                    t = 'DELETE FROM library.reservation WHERE membership_id = %s AND accession_number = %s '
                    cursor.execute(t, (mem_id,acc_num))
                    con.commit()
                except:
                    return
                
    def check_reserved(self,acc_num,mem_id):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                try:
                    t = 'SELECT * FROM library.reservation WHERE accession_number = %s '
                    cursor.execute(t, acc_num)
                    result = cursor.fetchone()
                    if result[1] != mem_id:
                        return True
                    else:
                        return False
                except:
                    return False

class return_intro:
    def __init__(self, root):
        self.root = root
        self.root.title("Return")
        start = tk.Label(self.root, text="To Return a Book, Please Enter Information Below:")
        start.grid(row = 0, columnspan=2)
        tk.Label(
            self.root, 
            text='Accession Number', 
            ).grid(row=1, column=0, pady=5)

        tk.Label(
            self.root, 
            text='Return Date', 
            ).grid(row=2, column=0, pady=5)

        self.acc_num = tk.Entry(self.root, width=30)
        self.acc_num.insert(0,"Used to identify an instance of book")
        self.acc_num.grid(row=1,column=1)
        self.ret_date = tk.Entry(self.root, width=30)
        self.ret_date.insert(0,"Date of book return DD/MM/YYYY")
        self.ret_date.grid(row = 2, column = 1)
        return_btn = tk.Button(self.root, text="Return book", padx=20, pady=10, command=lambda:self.return_bk())
        return_btn.grid(row=3,column=0)
        btn_return_to_menu = tk.Button(
            self.root,
            text = "Back to Loans menu",
            padx=20, pady = 10,
            command=lambda:self.root.destroy())
        btn_return_to_menu.grid(row = 3, column = 1)

    def return_bk(self):
        acc_num = self.acc_num.get()
        ret_date = self.ret_date.get()
        ret_date = datetime.datetime.strptime(ret_date,'%d/%m/%Y').date()
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                try:
                    j = 'SELECT accession_number,return_date,membership_id_borrowed FROM library.book WHERE accession_number = %s'
                    cursor.execute(j, acc_num)
                    test = cursor.fetchone()
                    
                    if test[1]:
                        if test[1] >= ret_date:
                            messagebox.showwarning('showwarning', 'Book already returned!')
                            return
                    t = 'SELECT accession_number,title,membership_id_borrowed,due_date FROM library.book WHERE accession_number = %s; '
                    cursor.execute(t, acc_num)
                    result = cursor.fetchone()
                    x = 'SELECT name FROM library.membership WHERE membership_id = %s; '
                    cursor.execute(x, result[2])
                    result2 = cursor.fetchone()
                    result = result + result2
                    self.new_window = tk.Toplevel(self.root)
                    self.app = temp_return(self.new_window, result,ret_date)
                    
                except:
                    
                    messagebox.showwarning('showwarning', 'No such book or book not borrowed before!')

class temp_return: #confirm delete
    def __init__(self,root,result,new_return):
        self.root = root
        self.root.title("Confirmation")
        tk.Label(self.root, text = "Please confirm return details to be correct: ").grid(row = 0, columnspan=2)
        self.result = result
        print(result)
        self.ret_date = new_return
        for i in range(len(result)):
            if i != 3:
                tk.Label(self.root, text = f"{self.result[i]}").grid(row=i+1,columnspan=2)
        tk.Label(self.root, text = f"{self.ret_date}").grid(row = 6,columnspan=2)
        if self.ret_date > result[3]: 
            self.fine = (self.ret_date - result[3]).days
            
        else:
            self.fine = 0
        
        tk.Label(self.root, text = f"${self.fine}").grid(row = 7,columnspan=2)

        confirm_btn = tk.Button(self.root, text = "Confirm return", padx=20,pady=10,command=lambda:self.confirm())
        confirm_btn.grid(row = 8,column = 0)
        back_btn = tk.Button(self.root, text = "Back to return function", padx=20,pady=10,command=lambda:self.root.destroy())
        back_btn.grid(row = 8, column = 1)
        
    def confirm(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        
        
        with con:
            with con.cursor() as cursor:
                curr_date = date.today()
                t = f'UPDATE library.book SET return_date = "{self.ret_date}", membership_id_borrowed = NULL WHERE accession_number = "{self.result[0]}"; '
                cursor.execute(t)
                con.commit()
                if self.fine:
                    try:
                        test = 'SELECT * FROM library.fine WHERE membership_id_fined = %s'
                        cursor.execute(test,self.result[2])
                        check = cursor.fetchone()
                        if check:
                            t = 'UPDATE library.fine SET last_updated_date = %s, amount_fined = %s + amount_fined WHERE membership_id_fined = %s; '
                            cursor.execute(t, (self.ret_date,self.fine,self.result[2]))
                            con.commit()
                        else:
                            t = f'INSERT INTO library.fine (`membership_id_fined`, `last_updated_date`, `amount_fined`) VALUES ("{self.result[2]}", "{self.ret_date}", "{self.fine}"); '
                            cursor.execute(t)
                            con.commit()
                        messagebox.showinfo("showinfo", "Book returned but has fines")
                        self.root.destroy()
                    except:
                        x = 'INSERT INTO `library`.`fine` (`membership_id_fined`, `last_updated_date`, `amount_fined`) VALUES (%s, %s, %s); '
                        cursor.execute(x, (self.result[2],self.ret_date,self.fine))
                        con.commit()
                        messagebox.showinfo("showinfo", "Book returned but has fines")
                        self.root.destroy()
                else:
                    messagebox.showinfo("showinfo", "Book returned")
                    self.root.destroy()

        
        
        

                
        
        
        
        

                    
        
                    
        

                
                
        

        


        
        
        
            
        
