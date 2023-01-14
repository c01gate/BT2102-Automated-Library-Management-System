import tkinter as tk
from tkinter import messagebox
import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    password='1145joellenG.', #CHANGE THIS
    database='library'
    )

class book_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Book")
        start_label = tk.Label(master = self.root,
                               relief = tk.GROOVE,
                               padx = 100,
                               text = "Select one of the options below: ")
        start_label.grid(row = 0)

        #B_Back_to_Menu_Button
        back_btn = tk.Button(master = self.root,
                             text = "Back to Main Menu",
                             width = 16,
                             height = 4,
                             highlightbackground = "gray",
                             relief = tk.FLAT,
                             command = lambda:self.root.destroy())
        back_btn.grid(row = 4, column = 0)

        #B_Acquisition_Frame
        acq_frame = tk.Frame(master = self.root)

        acq_frame.grid(row = 1, column = 0)

        #B_Acquisition_Label
        b_acq_lbl = tk.Label(master = acq_frame,
                             text ="Acquisition:",
                             width = 8,
                             height = 4,
                             relief = tk.FLAT).pack(side = tk.LEFT)
                                  
        
        #B_Acquisition Button
        b_acq_btn = tk.Button(master = acq_frame,
                              text = "Book Acquisition",
                              width = 12,
                              height = 4,
                              highlightbackground = "green",
                              bg = "green",
                              fg = "black",
                              relief = tk.RAISED,
                              command = self.bookacq).pack(side = tk.LEFT) 

        #B_Withdraw_Frame
        withdraw_frame = tk.Frame(master = self.root)

        withdraw_frame.grid(row = 2, column = 0)

        #B_Withdraw_Label
        b_withdraw_lbl = tk.Label(master = withdraw_frame,
                                  text ="Withdrawal:",
                                  width = 8,
                                  height = 4,
                                  relief = tk.FLAT).pack(side = tk.LEFT)
                                  


        #B_Withdraw_Button
        b_withdraw_btn = tk.Button(master = withdraw_frame,
                                   text = "Book Withdrawal",
                                   width = 12,
                                   height = 4,
                                   highlightbackground = "red",
                                   bg = "red",
                                   fg = "black",
                                   relief = tk.RAISED,
                                   command = self.bookwithdraw).pack(side = tk.LEFT)
    def bookacq(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = class_acquisition(self.new_window)

    def bookwithdraw(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = class_withdrawal(self.new_window)


class class_acquisition:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Acquistion")
        start = tk.Label(self.root,
                         text="For New Book Acquisition, Please Enter Requested Information Below:",
                         padx = 10)
        start.grid(row = 0, columnspan=2)

        #AccessionNumFrame
        ANFrame = tk.Frame(self.root)
        ANFrame.grid(row = 1, columnspan = 2)

        #AccessionNumLabel
        ANLbl = tk.Label(ANFrame,
                         text = "Accession Number",
                         width = 15,
                         relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #AccessionNumEntry
        self.accession_num = tk.Entry(ANFrame, width = 40)
        self.accession_num.insert(0,
                           "Used to identify an instance of a book")
        self.accession_num.pack(side = tk.LEFT)

        #TitleFrame
        TitleFrame = tk.Frame(self.root)
        TitleFrame.grid(row = 2, columnspan = 2)

        #TitleLabel
        TitleLbl = tk.Label(TitleFrame,
                         text = "Title",
                         width = 15,
                         relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #TitleEntry
        self.title = tk.Entry(TitleFrame, width = 40)
        self.title.insert(0,
                         "Title of Book")
        self.title.pack(side = tk.LEFT)

        #AuthorFrame
        AuthorFrame = tk.Frame(self.root)
        AuthorFrame.grid(row = 3, columnspan = 2)

        #AuthorLbl
        AuthorLbl = tk.Label(AuthorFrame,
                              text = "Authors",
                              width = 15,
                              relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #AuthorLblEntry
        self.author = tk.Entry(AuthorFrame, width = 40)
        self.author.insert(0,
                           "There can be multiple author for a book")
        self.author.pack(side = tk.LEFT)

        #ISBNFrame
        ISBNFrame = tk.Frame(self.root)
        ISBNFrame.grid(row = 4, columnspan = 2)

        #ISBNLabel
        ISBNLbl = tk.Label(ISBNFrame,
                         text = "ISBN",
                         width = 15,
                         relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #ISBNEntry
        self.isbn = tk.Entry(ISBNFrame, width = 40)
        self.isbn.insert(0,
                         "ISBN Number")
        self.isbn.pack(side = tk.LEFT)

        #PublisherFrame
        PublisherFrame = tk.Frame(self.root)
        PublisherFrame.grid(row = 5, columnspan = 2)

        #PublisherLabel
        PublisherLbl = tk.Label(PublisherFrame,
                         text = "Publisher",
                         width = 15,
                         relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #PublisherEntry
        self.publisher = tk.Entry(PublisherFrame, width = 40)
        self.publisher.insert(0,
                              "Random House, Penguin, Cengage, Springer, etc.")
        self.publisher.pack(side = tk.LEFT)

        #PublicationYearFrame
        PublicationYearFrame = tk.Frame(self.root)
        PublicationYearFrame.grid(row = 6, columnspan = 2)

        #PublicationYearLabel
        PublicationYearLbl = tk.Label(PublicationYearFrame,
                         text = "Publication Year",
                         width = 15,
                         relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #PublisherYearEntry
        self.pubyear = tk.Entry(PublicationYearFrame, width = 40)
        self.pubyear.insert(0,
                            "Edition year")
        self.pubyear.pack(side = tk.LEFT)

        
        # buttons
        add_btn = tk.Button(self.root,
                                 text="Add New Book",
                                 padx=20, pady=10,
                                 command=lambda:self.tbl_book())
                                 
        exit_btn = tk.Button(self.root,
                             text="Back to Books Menu",
                             padx=20, pady=10,
                             command=lambda:self.root.destroy())

        add_btn.grid(row = 7,column = 0)
        exit_btn.grid(row = 7, column = 1)


    def tbl_book(self):
        real_accession_num = self.accession_num.get()
        real_title = self.title.get()
        real_isbn = self.isbn.get()
        real_publisher = self.publisher.get()
        real_pubyear = self.pubyear.get()
        real_author = self.author.get()

        checkempty = (real_accession_num, real_title, real_isbn, real_publisher, real_pubyear, real_author)

        for ele in checkempty: #Blank Fields
            if ele == "":
                messagebox.showwarning("showwarning", "Missing or Incomplete fields")
                return
        try: #Check Int
            real_isbn = int(real_isbn)
        except:
            messagebox.showwarning("showwarning", "ISBN not an integer!")
            return
        try: #Check Int
            real_pubyear = int(real_pubyear)
        except:
            messagebox.showwarning("showwarning", "Publication year not an integer!")
            return
        result = (real_accession_num, real_title, int(real_isbn), real_publisher, int(real_pubyear))
        print(result)

        real_author_list = real_author.split(", ")
        print(real_author_list)

        substring = ","
        if ", " in real_author:
            pass
        elif substring in real_author:
            messagebox.showwarning("showwarning", "Enter multiple authors in the following format: \n Author 1, Author 2, etc.")
            return


        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )

        with con:
            with con.cursor() as cursor:
                t = "INSERT INTO `library`.`book` (`accession_number`, `title`, `isbn`, `publisher`, `pub_year`) VALUES (%s, %s, %s, %s,%s)"
                try:
                    cursor.execute(t, result)
                    con.commit()
                except:
                    messagebox.showwarning("showwarning", "Book already added")
                    return

        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )

        with con:
            with con.cursor() as cursor:
                s = "INSERT INTO `library`.`author` (`accession_number`, `author_name`) VALUES (%s, %s)"
                for author in real_author_list:
                    author_tup = (real_accession_num, author)
                    cursor.execute(s, author_tup)
                    con.commit()

        
        messagebox.showinfo("showinfo", "Success! \n ALS Book Acquisition Successful.")
##        self.auto_withdraw(real_isbn)
        self.root.destroy()
        
##    def auto_withdraw(self,isbn):
##
##        con = pymysql.connect(
##            host='localhost',
##            user='root',
##            password='1145joellenG.', #CHANGE THIS
##            database='library'
##            )
##
##        with con:
##            with con.cursor() as cursor:
##                    t = f'SELECT * FROM library.book WHERE isbn = "{isbn}" '
##                    cursor.execute(t)
##                    result = cursor.fetchall()
##                    updated = int(result[0][4])
##                    for i in result:
##                        if int(i[4]) > updated:
##                            updated = int(i[4])
##                    for x in result:
##                        if x[2] != updated:
##                            t2 = 'DELETE FROM library.book WHERE accession_number = %s; '
##                            cursor.execute(t2, x[0])
##                            con.commit()

class class_withdrawal:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Withdrawal")
        start = tk.Label(self.root,
                         text="To Remove Outdated Books From System, Please Enter Required Information Below:",
                         padx = 10)
        start.grid(row = 0, columnspan=2)

        #AccessionNumFrame
        ANFrame = tk.Frame(self.root)
        ANFrame.grid(row = 1, columnspan = 2)

        #AccessionNumLabel
        ANLbl = tk.Label(ANFrame,
                         text = "Accession Number",
                         width = 15,
                         relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #AccessionNumEntry
        self.accession_num = tk.Entry(ANFrame, width = 40)
        self.accession_num.insert(0,
                                  "Used to identify an instance of a book")
        self.accession_num.pack(side = tk.LEFT)

        # buttons
        withdraw_btn = tk.Button(self.root,
                                 text="Withdraw Book",
                                 padx=20, pady=10,
                                 command=lambda:self.tbl_bookwithdraw())
                                 
        exit_btn = tk.Button(self.root,
                             text="Back to Books Menu",
                             padx=20, pady=10,
                             command=lambda:self.root.destroy())

        withdraw_btn.grid(row = 2,column = 0)
        exit_btn.grid(row = 2, column = 1)

    def tbl_bookwithdraw(self):
        del_accession_num = self.accession_num.get()
        if del_accession_num == "":
            messagebox.showwarning("showwarning", "Missing or Incomplete fields")
            return

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
                    cursor.execute(t, del_accession_num)
                    result = cursor.fetchone()
                    con.commit()
                except:
                    messagebox.showwarning("showwarning", "Book does not exist!")
                    return
        #print(result)

        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )

        with con:
            with con.cursor() as cursor:
                try:
                    s = 'SELECT * FROM library.author WHERE accession_number = %s'
                    cursor.execute(s, del_accession_num)
                    res = cursor.fetchall()
                    con.commit()
                except:
                    messagebox.showwarning("showwarning", "Book ID does not exist!")
                    return
        print(res)
        
        if res == ():
            messagebox.showwarning("showwarning", "Missing or Incomplete fields")
            return
        else:
            #print("why iasit running")
            authorsTpl = ()
            if len(res) > 1:
                for ele in res:
                    authorsTpl = authorsTpl + (ele[1],)
                #print(authorsTpl)
            else:
                authorsTpl = (res,)
                #print(authorsTpl)

            result = result[:2] + (authorsTpl,) + result[2:5]
            #print(result)
            withdraw_func_class(tk.Toplevel(self.root), result)

class withdraw_func_class:
    def __init__(self, root, result):
        self.root = root
        self.result = result
        del_accession_num = result[0]

        if result is None:
            messagebox.showwarning("showwarning", "Book ID does not exist!")
            self.root.title("Try Again")
            button = tk.Button(self.root,
                               text = "Return",
                               bg = "indian red",
                               highlightbackground = "red",
                               fg = "black",
                               command=lambda:self.root.destroy()).pack(padx = 50)
        else:
            con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )

            with con:
                with con.cursor() as cursor:
                    try:
                        s = 'SELECT * FROM library.author WHERE accession_number = %s'
                        cursor.execute(s, del_accession_num)
                        res = cursor.fetchall()
                        con.commit()
                    except:
                        messagebox.showwarning("showwarning", "Membership ID does not exist!")
                        return
            print(res)
            authorsTpl = ()
            if len(res) > 1:
                for ele in res:
                    authorsTpl = authorsTpl + (ele[1],)
                #print(authorsTpl)
            else:
                authorsTpl = (res[0][1],)
                print(authorsTpl)

                
            authorDisplayStr = ""
            if len(authorsTpl) > 1:
                for i in range(len(authorsTpl)-1):
                    authorDisplayStr = authorDisplayStr + authorsTpl[i] + ", "
                authorDisplayStr = authorDisplayStr + authorsTpl[-1]
            else:
                authorDisplayStr += authorsTpl[0]
                
            self.root.title("Confirmation")
            tk.Label(self.root, text = "Please confirm details to be correct: ").grid(row = 0, columnspan=2)

            info_frame = tk.Frame(self.root)
            info_frame.grid(row = 1, columnspan = 2)
            fields = ("Accession Number", "Title", "Authors", "ISBN", "Publisher", "Publication Year")
            i = 1
            for i in range(len(fields)):
                tk.Label(info_frame,
                         text = f"{fields[i]}").grid(row = i + 1, column = 0)                   

            for i in range(2):
                tk.Label(info_frame,
                         text = f"{self.result[i]}",
                         relief = tk.GROOVE, width = 30).grid(row=i+1, column = 1)

            authorLbl = tk.Label(info_frame,
                                 text = authorDisplayStr,
                                 relief = tk.GROOVE,
                                 width = 30).grid(row = 3, column  = 1)

            for i in range(3, len(result)):
                tk.Label(info_frame,
                         text = f"{self.result[i]}",
                         relief = tk.GROOVE, width = 30).grid(row=i+1, column = 1)
                

            confirm_btn = tk.Button(self.root,
                                    text = "Confirm Withdrawal",
                                    padx=20, pady=10,
                                    command=lambda:self.confirm())
            confirm_btn.grid(row = 6,column = 0)

            back_btn = tk.Button(self.root,
                                 text = "Back to delete function",
                                 padx=20, pady=10,
                                 command=lambda:self.root.destroy())
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
                if self.check_loaned():
                    messagebox.showwarning("showwarning", "ERROR! \n Book is currently on Loan")
                    return
                elif self.check_reserved():
                    messagebox.showwarning("showwarning", "ERROR! \n Book is currently Reserved")
                    return
                else:
                    t = 'DELETE FROM library.book WHERE accession_number = %s; '
                    cursor.execute(t, self.result[0])
                    con.commit()
        messagebox.showinfo("showinfo", "Book Withdrawn")
        self.root.destroy()

    def check_loaned(self):
        accnum = self.result[0]
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                t = 'SELECT * FROM library.book WHERE accession_number = %s'
                cursor.execute(t, accnum)
                check = cursor.fetchone()
                con.commit()
                print(check)
                if check[5] is None:
                    return False
                else:
                    return True

    def check_reserved(self):
        accnum = self.result[0]
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                t = 'SELECT * FROM library.reservation WHERE accession_number = %s'
                cursor.execute(t, accnum)
                check = cursor.fetchone()
                con.commit()
                print(check)
                if check is None:
                    return False
                else:
                    return True
