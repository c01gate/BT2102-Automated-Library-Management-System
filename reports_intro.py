import tkinter as tk
from tkinter import messagebox
import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    password='1145joellenG.', #CHANGE THIS
    database='library'
    )

class report_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Reports")
        tk.Label(self.root, text="Select one of the options below: ").grid(row=0,columnspan=2)
        tk.Label(self.root, text="A member can perform a search on the collection of books.").grid(row=1,column=1)
        tk.Label(self.root, text="This function displays all the books currently on loan to members.").grid(row=2,column=1)
        tk.Label(self.root, text="This function displays all the books that members have reserved.").grid(row=3,column=1)
        tk.Label(self.root, text="This function displays all the books that members have reserved.").grid(row=4,column=1)
        tk.Label(self.root, text="This function displays all the books a member identified by the membership id has borrowed.").grid(row=5,column=1)
        
        btn_search = tk.Button(
            self.root,
            text="Book Search",
            command=lambda:self.search_intro()
            )
        btn_search.grid(row=1,column=0)
        
        btn_loan = tk.Button(
            self.root,
            text="Books On Loan",
            command=lambda:self.loan_dis_int()
            )
        btn_loan.grid(row=2,column=0)
        
        btn_reservation = tk.Button(
            self.root,
            text="Books On Reservation",
            command=lambda:self.res_dis_int()
            )
        btn_reservation.grid(row=3,column=0)
        
        btn_outfine = tk.Button(
            self.root,
            text="Outstanding Fines",
            command=lambda:self.outfine_int()
            )
        btn_outfine.grid(row=4,column=0)
        
        btn_memloan = tk.Button(
            self.root,
            text="Books On Loan To Member",
            command=lambda:self.memloan_int()
            )
        btn_memloan.grid(row=5,column=0)

        btn_return_to_menu = tk.Button(
            self.root,
            text = "Back to main menu",
            width = 10, height = 2,
            command=lambda:self.root.destroy())
        btn_return_to_menu.grid(row = 6, columnspan = 2)

    def search_intro(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = search_intro(self.new_window)

    def loan_dis_int(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = loan_dis_int(self.new_window)

    def res_dis_int(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = res_dis_int(self.new_window)

    def outfine_int(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = outfine_int(self.new_window)

    def memloan_int(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = memloan_int(self.new_window)

#search function
class search_intro:
    def __init__(self, root):
        self.root = root
        self.root.title("Search")
        tk.Label(self.root, text="Search based on one of the categories below: ").grid(row=0,columnspan=2)
        tk.Label(self.root, text="Title").grid(row=1,column=0)
        tk.Label(self.root, text="Authors").grid(row=2,column=0)
        tk.Label(self.root, text="ISBN").grid(row=3,column=0)
        tk.Label(self.root, text="Publisher").grid(row=4,column=0)
        tk.Label(self.root, text="Publication Year").grid(row=5,column=0)
        
        # Entry
        self.title = tk.Entry(self.root, width=30)
        self.title.insert(0,"Book Name")
        self.title.grid(row = 1, column = 1)
        self.authors = tk.Entry(self.root, width=30)
        self.authors.insert(0,"There can be multiple authors for a book e.g authorA,authorB,authorC")
        self.authors.grid(row = 2, column = 1)
        self.isbn = tk.Entry(self.root, width=30)
        self.isbn.insert(0,"ISBN Number")
        self.isbn.grid(row = 3, column = 1)
        self.publisher = tk.Entry(self.root, width=30)
        self.publisher.insert(0,"Random House, Penguin, Cengage, Springer, etc. ")
        self.publisher.grid(row = 4, column = 1)
        self.year = tk.Entry(self.root, width=30)
        self.year.insert(0,"Edition year")
        self.year.grid(row = 5, column = 1)

        srch_btn = tk.Button(self.root, text="Search book", padx=20, pady=10, command=lambda:self.srch_book()
            )
                                 
        exit_btn = tk.Button(self.root, text="Back to Reports menu", padx=20, pady=10, command=lambda:self.root.destroy())
        srch_btn.grid(row = 6,column = 0)
        exit_btn.grid(row = 6, column = 1)

    def srch_book(self):
        real_title = self.title.get()
        real_authors = self.authors.get()

        if len(real_title.split(" ")) > 1:
            messagebox.showwarning("showwarning", "Search only accept one word!")
            return
        if len(real_authors.split(" ")) > 1:
            messagebox.showwarning("showwarning", "Search only accept one word!")
            return
        
        try:
            if self.isbn.get() != "":
                real_isbn = int(self.isbn.get())
        except:
            messagebox.showwarning("showwarning", "Not a year!")
            return
        real_publisher = self.publisher.get()
        if len(real_publisher.split(" ")) > 1:
            messagebox.showwarning("showwarning", "Search only accept one word!")
            return
        try:
            if self.year.get() != "":
                real_year = int(self.year.get())
        except:
            messagebox.showwarning("showwarning", "Not an ISBN number!")
            return
        #result1 =  (real_title, real_authors, real_isbn, real_publisher, real_year)       
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                result = ()
                #REGEXP "^{real_title}\s|\s{real_title}$"
                if real_title != "":
                    t1 = f'SELECT * FROM library.book WHERE title LIKE "% {real_title} %" OR title LIKE "% {real_title}" OR title LIKE "{real_title} %" OR title = "{real_title}" '
                    cursor.execute(t1)
                    result = cursor.fetchall()
                elif real_authors:
                    if type(real_authors) == str:
                        t2 = f'SELECT accession_number FROM library.author WHERE author_name LIKE "% {real_authors} %" OR author_name LIKE "% {real_authors}" OR author_name LIKE "{real_authors} %" OR author_name = "{real_authors}" '
                        cursor.execute(t2)
                        result1 = cursor.fetchall()
                    else:
                        for i in real_authors:
                            t2 = f'SELECT accession_number FROM library.author WHERE author_name = "{i}"; '
                            cursor.execute(t2)
                            result1 = cursor.fetchall()
                    for x in result1:
                        t2_1 = f'SELECT * FROM library.book WHERE accession_number = "{x[0]}"; '
                        cursor.execute(t2_1)
                        result = result + (cursor.fetchone(),)

                elif self.isbn.get() != "":
                    t3 = f'SELECT * FROM library.book WHERE isbn = "{real_isbn}"; '
                    cursor.execute(t3)
                    result = cursor.fetchall()
                elif real_publisher != "":
                    t4 = f'SELECT * FROM library.book WHERE publisher LIKE "% {real_publisher} %" OR publisher LIKE "% {real_publisher}" OR publisher LIKE "{real_publisher} %" OR publisher = "{real_publisher}" '
                    cursor.execute(t4)
                    result = cursor.fetchall()
                elif self.year.get() != "":
                    t5 = f'SELECT * FROM library.book WHERE pub_year = {real_year}'
                    cursor.execute(t5)
                    result = cursor.fetchall()
            #result = tuple of tuples
        self.new_window = tk.Toplevel(self.root)
        self.app = search_result(self.new_window,result)

class search_result:
    def __init__(self, root, result):
        self.root = root
        self.result = result
        print(self.result)
        print("here")
        self.root.title("Search Results")
        start = tk.Label(self.root, text="Book Search Results")
        start.grid(row = 0, columnspan=2)
        tk.Label(self.root, text="Accession Number").grid(row=1,column=0)
        tk.Label(self.root, text="Title").grid(row=1,column=1)
        tk.Label(self.root, text="Authors").grid(row=1,column=2)
        tk.Label(self.root, text="ISBN").grid(row=1,column=3)
        tk.Label(self.root, text="Publisher").grid(row=1,column=4)
        tk.Label(self.root, text="Publication Year").grid(row=1,column=5)
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                #find authors for each book result = (book,book)
                for x in range(len(result)):
                    t = f'SELECT author_name FROM library.author WHERE accession_number = "{result[x][0]}"; '
                    cursor.execute(t)
                    authors = cursor.fetchall()
                    new = ""
                    for i in authors:
                        new += i[0] + ", "
                        
                    for j in range(6):
                        if j < 2:
                            tk.Label(self.root, text = f"{result[x][j]}").grid(row=2+x,column=j)
                        if j == 2:
                            tk.Label(self.root, text = f"{new}").grid(row=2+x,column=j)
                        if j > 2:
                            tk.Label(self.root, text = f"{result[x][j-1]}").grid(row=2+x,column=j)
                            
        exit_btn = tk.Button(self.root, text="Back to Search Function", padx=20, pady=10, command=lambda:self.root.destroy())
        exit_btn.grid(row = 5+len(result), columnspan = 2)
                
class loan_dis_int:
    def __init__(self, root):
        self.root = root
        self.root.title("Loans report")
        start = tk.Label(self.root, text="Book On Loan Report")
        start.grid(row = 0, columnspan=2)
        tk.Label(self.root, text="Accession Number").grid(row=1,column=0)
        tk.Label(self.root, text="Title").grid(row=1,column=1)
        tk.Label(self.root, text="Authors").grid(row=1,column=2)
        tk.Label(self.root, text="ISBN").grid(row=1,column=3)
        tk.Label(self.root, text="Publisher").grid(row=1,column=4)
        tk.Label(self.root, text="Publication Year").grid(row=1,column=5)
        
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                t = 'SELECT * FROM library.book WHERE membership_id_borrowed IS NOT NULL'
                cursor.execute(t)
                result = cursor.fetchall()
                print(result)
                for x in range(len(result)):
                    t = f'SELECT author_name FROM library.author WHERE accession_number = "{result[x][0]}"; '
                    cursor.execute(t)
                    authors = cursor.fetchall()
                    new = ""
                    for i in authors:
                        if len(authors) > 1:
                            new += i[0] + ", "
                        else:
                            new += i[0]
                        
                    for j in range(6):
                        if j < 2:
                            tk.Label(self.root, text = f"{result[x][j]}").grid(row=2+x,column=j)
                        if j == 2:
                            tk.Label(self.root, text = f"{new}").grid(row=2+x,column=j)
                        if j > 2:
                            tk.Label(self.root, text = f"{result[x][j-1]}").grid(row=2+x,column=j)
                            
        exit_btn = tk.Button(self.root, text="Back to Report Menu", padx=20, pady=10, command=lambda:self.root.destroy())
        exit_btn.grid(row = 5+len(result), columnspan = 2)

        
class res_dis_int:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservations report")
        start = tk.Label(self.root, text="Book On Reservation Report")
        start.grid(row = 0, columnspan=2)
        tk.Label(self.root, text="Accession Number").grid(row=1,column=0)
        tk.Label(self.root, text="Title").grid(row=1,column=1)
        tk.Label(self.root, text="Membership ID").grid(row=1,column=2)
        tk.Label(self.root, text="Name").grid(row=1,column=3)
        
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                t1 = 'SELECT * FROM library.reservation'
                cursor.execute(t1)
                result = cursor.fetchall()
                print(result) #acc, mem, date reserved
                final = ()
                #result will be tuple if u select more than one column
                for x in range(len(result)):
                    check = result[x]
                    t2 = f'SELECT title FROM library.book WHERE accession_number = "{check[0]}"; '
                    cursor.execute(t2)
                    title = cursor.fetchone()[0]
                    check = (check[0],) + (title,) + (check[1],)
                    t3 = f'SELECT name FROM library.membership WHERE membership_id = "{check[2]}"; '
                    cursor.execute(t3)
                    name = cursor.fetchone()[0]
                    check = check + (name,)
                    final += (check,)
                for i in range(len(final)):
                    for j in range(len(final[i])):
                        tk.Label(self.root, text=f"{final[i][j]}").grid(row = 2+i,column=j)
                    
        exit_btn = tk.Button(self.root, text="Back to Report Menu", padx=20, pady=10, command=lambda:self.root.destroy())
        exit_btn.grid(row = len(final) + 2, columnspan = 2)
        
class outfine_int:
    def __init__(self, root):
        self.root = root
        self.root.title("Outstanding fines report")
        start = tk.Label(self.root, text="Members With Outstanding Fines")
        start.grid(row = 0, columnspan=2)
        tk.Label(
            self.root, 
            text='Membership ID', 
            ).grid(row=1, column=0, pady=5)

        tk.Label(
            self.root, 
            text='Name', 
            ).grid(row=1, column=1, pady=5)

        tk.Label(
            self.root, 
            text='Faculty', 
            ).grid(row=1, column=2, pady=5)

        tk.Label(
            self.root, 
            text='Phone Number', 
            ).grid(row=1, column=3, pady=5)

        tk.Label(
            self.root, 
            text='Email Address', 
            ).grid(row=1, column=4, pady=5)
        
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.',
            database='library'
            )

        with con:
            with con.cursor() as cursor:
                result = ()
                t = 'SELECT membership_id_fined FROM library.fine WHERE amount_fined > 0; ' 
                cursor.execute(t)
                check = cursor.fetchall()
                print(check)
                for i in check:
                    t2 = f'SELECT * FROM library.membership WHERE membership_id = "{i[0]}"; '
                    cursor.execute(t2)
                    result += cursor.fetchall()
                for x in range(len(result)):
                    for y in range(len(result[x])):
                        tk.Label(self.root, text = f"{result[x][y]}").grid(row = 2+x, column = y)
                
        
        exit_btn = tk.Button(self.root, text="Back to Report Menu", padx=20, pady=10, command=lambda:self.root.destroy())
        exit_btn.grid(row = len(result) + 3, columnspan = 2)

        
        
class memloan_int:
    def __init__(self, root):
        self.root = root
        self.root.title("Member's Loan report")
        tk.Label(self.root,text = "Books on Loan to Member").grid(row=0,columnspan=2)
        tk.Label(
            self.root, 
            text='Membership ID', 
            ).grid(row=1, column=0, pady=5)
        self.mem_id = tk.Entry(self.root, width=30)
        self.mem_id.insert(0,"A unique alphanumeric id that distinguishes every member")
        self.mem_id.grid(row = 1, column = 1)

        srch_btn = tk.Button(self.root, text="Search Member", padx=20, pady=10, command=lambda:self.srch_mem()
            )
                                 
        exit_btn = tk.Button(self.root, text="Back to Reports menu", padx=20, pady=10, command=lambda:self.root.destroy())
        srch_btn.grid(row = 2,column = 0)
        exit_btn.grid(row = 2, column = 1)

    def srch_mem(self):
        mem_id = self.mem_id.get()
        self.new_window = tk.Toplevel(self.root)
        self.app = search_mem(self.new_window, mem_id)

class search_mem:
    def __init__(self, root, mem_id):
        self.root = root
        self.mem_id = mem_id
        self.root.title("Membership Loan")
        tk.Label(self.root, text="Accession Number").grid(row=1,column=0)
        tk.Label(self.root, text="Title").grid(row=1,column=1)
        tk.Label(self.root, text="Authors").grid(row=1,column=2)
        tk.Label(self.root, text="ISBN").grid(row=1,column=3)
        tk.Label(self.root, text="Publisher").grid(row=1,column=4)
        tk.Label(self.root, text="Publication Year").grid(row=1,column=5)
        
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        print(self.mem_id)
        with con:
            with con.cursor() as cursor:
                t = f'SELECT * FROM library.book WHERE membership_id_borrowed = "{self.mem_id}"; '
                cursor.execute(t)
                result = cursor.fetchall()
                print(result)
                for x in range(len(result)):
                    t = f'SELECT author_name FROM library.author WHERE accession_number = "{result[x][0]}"; '
                    cursor.execute(t)
                    authors = cursor.fetchall()
                    new = ""
                    for i in authors:
                        if len(authors) > 1:
                            new += i[0] + ", "
                        else:
                            new += i[0]
                        
                    for j in range(6):
                        if j < 2:
                            tk.Label(self.root, text = f"{result[x][j]}").grid(row=2+x,column=j)
                        if j == 2:
                            tk.Label(self.root, text = f"{new}").grid(row=2+x,column=j)
                        if j > 2:
                            tk.Label(self.root, text = f"{result[x][j-1]}").grid(row=2+x,column=j)
                            
        exit_btn = tk.Button(self.root, text="Back to Report Menu", padx=20, pady=10, command=lambda:self.root.destroy())
        exit_btn.grid(row = 5+len(result), columnspan = 2)
        
        

        
        

        
    
        

                    
                    
        
        
        
        
        
        
