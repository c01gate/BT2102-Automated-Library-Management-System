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

#doesnt account for the case where YOU can keep reserving the same book?
#check if my reserve date is updating
#make sure that book reservation is checking both fines AS WELL AS if theres books overdue but not returned


class reserve_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservations")
        tk.Label(self.root, text="Select one of the options below: ").grid(row=0,columnspan=2)
        tk.Label(self.root, text="Book reservation").grid(row=1,column=0)
        tk.Label(self.root, text="Book reservation cancellation").grid(row=2,column=0)

        btn_reserve = tk.Button(self.root, text="Reservations", command=self.reserve_page)
        btn_reserve.grid(row=1, column=1)

        btn_reservation_cancellation = tk.Button(self.root, text="Reservation Cancellations", command=self.reservation_cancellation_page)
        btn_reservation_cancellation.grid(row=2, column=1)

        btn_return_to_menu = tk.Button(self.root, text="Back to main menu", width=15, height=2, command=lambda: self.root.destroy())
        btn_return_to_menu.grid(row=3, columnspan=2)


    def reservation_cancellation_page(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = reservation_cancellation_intro(self.new_window)

    def reserve_page(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = reserve_intro(self.new_window)

class reserve_intro:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservation")
        start = tk.Label(self.root, text="To Reserve a Book, Please Enter Information Below:")
        start.grid(row=0, columnspan=2)
        tk.Label(self.root, text='Accession Number').grid(row=1, column=0, pady=5)

        tk.Label(self.root, text='Membership ID').grid(row=2, column=0, pady=5)

        self.acc_num = tk.Entry(self.root, width=30)
        self.acc_num.insert(0, "Used to identify an instance of book")
        self.acc_num.grid(row=1, column=1)

        self.mem_id = tk.Entry(self.root, width=30)
        self.mem_id.insert(0, "A unique alphanumeric id that distinguishes every member")
        self.mem_id.grid(row=2, column=1)

        reserve_btn = tk.Button(self.root, text="Reserve book", padx=20, pady=10, command=lambda: self.reserve())
        reserve_btn.grid(row=3, column=0)

        btn_return_to_menu = tk.Button(self.root, text="Back to main menu", padx=20, pady=10,
                                       command=lambda: self.root.destroy())
        btn_return_to_menu.grid(row=3, column=1)

    def reserve(self):
        acc_num = self.acc_num.get()
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.',  # CHANGE THIS
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
                    self.app = temp_reserve(self.new_window, result, self.mem_id.get())
                    con.commit()
                except:
                    messagebox.showwarning("showwarning", "Book does not exist!")
                    return

class temp_reserve:
    def __init__(self, root, result, mem):
        self.root = root
        self.root.title("Confirmation")
        tk.Label(self.root, text="Please confirm reservation details to be correct: ").grid(row=0, columnspan=2)
        self.result = result
        self.mem_id = mem
        for i in range(4):
            tk.Label(self.root, text=f"{self.result[i]}").grid(row=i + 1,columnspan = 2)
        confirm_btn = tk.Button(self.root, text="Confirm Reserve", padx=20, pady=10, command=lambda: self.confirm())
        confirm_btn.grid(row=6, column=0)
        back_btn = tk.Button(self.root, text="Back to reservation function", padx=20, pady=10,
                             command=lambda: self.root.destroy())
        back_btn.grid(row=6, column=1)

    def confirm(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.',  # CHANGE THIS
            database='library'
        )
        with con:
            with con.cursor() as cursor:

                # check if book is on loan
                # if book is on loan, give member the option to reserve
                # can only reserve a maximum of 2 books
                if self.check_quota(self.mem_id):
                    messagebox.showwarning("showwarning", "ERROR! \n Member reservation quota exceeded.")
                    self.root.destroy()
                    return

                # can only reserve books if there is no outstanding fines
                if self.check_fines(self.mem_id):
                    messagebox.showwarning("showwarning", "ERROR! \n Member has outstanding fines.")
                    self.root.destroy()
                    return

                # can only be reserved if the book is not reserved by someone else
                if self.check_reserved(self.result[0], self.mem_id):
                    messagebox.showwarning("showwarning", "ERROR! \n Book currently reserved by someone else.")
                    self.root.destroy()
                    return
                curr_date = date.today()
                t = f'INSERT INTO library.reservation (`accession_number`, `membership_id`, `reserved_date`) VALUES ("{self.result[0]}", "{self.mem_id}", "{curr_date}"); '
                cursor.execute(t)
                con.commit()
                messagebox.showinfo("showinfo", "Book reserved")
        self.root.destroy()

    # correct
    def check_quota(self, mem_id):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.',  # CHANGE THIS
            database='library'
        )
        with con:
            with con.cursor() as cursor:
                try:
                    t = 'SELECT accession_number FROM library.reservation WHERE membership_id = %s; '
                    cursor.execute(t, mem_id)
                    result = cursor.fetchall()
                    print(len(result))
                    if len(result) >= 2:
                        return True
                    else:
                        return False
                except:
                    return False

    # correct
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

    # correct
    def check_reserved(self, acc_num, mem_id):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.',  # CHANGE THIS
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


class reservation_cancellation_intro:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservation Cancellation")
        start = tk.Label(self.root, text="To Cancel Your Reservation for a Book, Please Enter Information Below:")
        start.grid(row=0, columnspan=2)
        tk.Label(self.root, text='Accession Number').grid(row=1, column=0, pady=5)

        tk.Label(self.root, text='Membership ID').grid(row=2, column=0, pady=5)

        self.acc_num = tk.Entry(self.root, width=30)
        self.acc_num.insert(0, "Used to identify an instance of book")
        self.acc_num.grid(row=1, column=1)

        self.mem_id = tk.Entry(self.root, width=30)
        self.mem_id.insert(0, "A unique alphanumeric id that distinguishes every member")
        self.mem_id.grid(row=2, column=1)

        reserve_btn = tk.Button(self.root, text="Cancel Book Reservation", padx=20, pady=10,
                                command=lambda: self.reserve_cancellation())
        reserve_btn.grid(row=3, column=0)

        btn_return_to_menu = tk.Button(self.root, text="Back to main menu", padx=20, pady=10,
                                       command=lambda: self.root.destroy())
        btn_return_to_menu.grid(row=3, column=1)

    def reserve_cancellation(self):
        acc_num = self.acc_num.get()
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.',  # CHANGE THIS
            database='library'
        )

        with con:
            with con.cursor() as cursor:
                try:
                    t = 'SELECT * FROM library.reservation WHERE accession_number = %s; '
                    cursor.execute(t, acc_num)
                    result = cursor.fetchone()
                    self.new_window = tk.Toplevel(self.root)
                    
                    self.app = temp_reserve_cancellation(self.new_window, result, self.mem_id.get())
                    print(result)
                except:
                    messagebox.showwarning("showwarning", "Book reservation does not exist!")
                    return

class temp_reserve_cancellation:
    def __init__(self, root, result, mem):
        self.root = root
        self.root.title("Confirmation")
        tk.Label(self.root, text="Please confirm reservation cancellation details to be correct: ").grid(row=0,columnspan=2)
        self.result = result
        self.mem_id = mem
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.',
            database='library'
            )

        with con:
            with con.cursor() as cursor:
                t1 = f'SELECT title FROM library.book WHERE accession_number = "{self.result[0]}"; '
                cursor.execute(t1)
                title = cursor.fetchone()[0]
                t2 = f'SELECT name FROM library.membership WHERE membership_id = "{self.result[1]}"; '
                cursor.execute(t2)
                name = cursor.fetchone()[0]
        final = (self.result[0], title, self.result[1], name, date.today())
        for i in range(len(final)):
            tk.Label(self.root, text= f"{final[i]}").grid(row=i+1,columnspan=2)
            
        confirm_btn = tk.Button(self.root, text="Confirm Reservation cancellation", padx=20, pady=10,
                                command=lambda: self.confirm(self.result[0],self.result[1]))
        confirm_btn.grid(row=6, column=0)
        back_btn = tk.Button(self.root, text="Back to reservation cancellation function", padx=20, pady=10,
                             command=lambda: self.root.destroy())
        back_btn.grid(row=6, column=1)

    def confirm(self, acc_num, mem_id):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.',  # CHANGE THIS
            database='library'
        )
        with con:
            with con.cursor() as cursor:
                try:
                    t = 'DELETE FROM library.reservation WHERE membership_id = %s AND accession_number = %s '
                    cursor.execute(t, (mem_id, acc_num))
                    con.commit()
                    messagebox.showinfo("showinfo", "Book reservation deleted")
                    self.root.destroy()
                except:
                    messagebox.showwarning("showwarning", "Book reservation does not exist!")
                    return
