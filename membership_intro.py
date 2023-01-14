import tkinter as tk
from tkinter import messagebox
import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    password='1145joellenG.', #CHANGE THIS
    database='library'
    )


class membership_window: #member intro
    def __init__(self,root):
        self.root = root
        self.root.title("Membership")
        start_label = tk.Label(master = self.root,
                               relief = tk.GROOVE,
                               padx = 100,
                               text = "Select one of the options below: ")
        start_label.grid(row = 0)

        #M_Back_to_Menu_Button
        back_btn = tk.Button(master = self.root,
                             text = "Back to Main Menu",
                             width = 16,
                             height = 4,
                             highlightbackground = "gray",
                             relief = tk.FLAT,
                             command = lambda:self.root.destroy())
        back_btn.grid(row = 4, column = 0)
        
        #M_Create_Frame
        create_frame = tk.Frame(master = self.root)

        create_frame.grid(row = 1, column = 0)

        #M_Creation_Label
        m_creation_lbl = tk.Label(master = create_frame,
                                  text ="Create:",
                                  width = 8,
                                  height = 4,
                                  relief = tk.FLAT).pack(side = tk.LEFT)
                                  
        
        #Membership Creation Button
        membership_creation_btn = tk.Button(master = create_frame,
                                            text = "Membership Creation",
                                            width = 12,
                                            height = 4,
                                            highlightbackground = "green",
                                            bg = "green",
                                            fg = "black",
                                            relief = tk.RAISED,
                                            command = self.create_member).pack(side = tk.LEFT)
                                            

        #M_Delete_Frame
        delete_frame = tk.Frame(master = self.root)

        delete_frame.grid(row = 2, column = 0)

        #M_Delete_Label
        m_deletion_lbl = tk.Label(master = delete_frame,
                                  text ="Delete:",
                                  width = 8,
                                  height = 4,
                                  relief = tk.FLAT).pack(side = tk.LEFT)
                                  


        #Membership Deletion Button
        membership_deletion_btn = tk.Button(master = delete_frame,
                                            text = "Membership Deletion",
                                            width = 12,
                                            height = 4,
                                            highlightbackground = "red",
                                            bg = "red",
                                            fg = "black", relief = tk.RAISED,
                                            command = self.delete_member).pack(side = tk.LEFT)

        #M_Update_Frame
        update_frame = tk.Frame(master = self.root)

        update_frame.grid(row = 3, column = 0)

        #M_Update_Label
        m_update_lbl = tk.Label(master = update_frame,
                                  text ="Update:",
                                  width = 8,
                                  height = 4,
                                  relief = tk.FLAT).pack(side = tk.LEFT)
                                  

        

        #Membership Update Button
        membership_update_btn = tk.Button(master = update_frame,
                                          text = "Membership Update",
                                          width = 12,
                                          height = 4,
                                          highlightbackground = "blue",
                                          bg = "blue",
                                          fg = "black", relief = tk.RAISED,
                                          command = self.update_member).pack(side = tk.LEFT)


    def create_member(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = class_create(self.new_window)

    def delete_member(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = class_delete(self.new_window)

    def update_member(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = class_update(self.new_window)



class class_create: #create intro
    def __init__(self,root):
        self.root = root
        self.root.title("Membership Creation")
        start = tk.Label(self.root,
                         text="To Create Member, Please Enter Requested Information Below:",
                         padx = 10)
        start.grid(row = 0, columnspan=2)

        #MembershipEntryFrame
        MEFrame = tk.Frame(self.root)
        MEFrame.grid(row = 1, columnspan = 2)

        #MembershipEntryLabel
        MELbl = tk.Label(MEFrame,
                         text = "Membership ID",
                         width = 15,
                         relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #MembershipEntry
        self.mem_id = tk.Entry(MEFrame, width = 40)
        self.mem_id.insert(0,
                           "A unique alphanumeric id that distinguishes every member")
        self.mem_id.pack(side = tk.LEFT)

        #NameEntryFrame
        NameFrame = tk.Frame(self.root)
        NameFrame.grid(row = 2, columnspan = 2)

        #NameEntryLabel
        NameLbl = tk.Label(NameFrame,
                         text = "Name",
                         width = 15,
                         relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #NameEntry
        self.name = tk.Entry(NameFrame, width = 40)
        self.name.insert(0,
                         "Enter member's, name")
        self.name.pack(side = tk.LEFT)

        #FacultyFrame
        FacultyFrame = tk.Frame(self.root)
        FacultyFrame.grid(row = 3, columnspan = 2)

        #FacultyLabel
        FacultyLbl = tk.Label(FacultyFrame,
                         text = "Faculty",
                         width = 15,
                         relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #FacultyEntry
        self.faculty = tk.Entry(FacultyFrame, width = 40)
        self.faculty.insert(0,
                         "e.g., Computing, Engineering, Science, etc.")
        self.faculty.pack(side = tk.LEFT)

        #HPFrame
        PhoneNumFrame = tk.Frame(self.root)
        PhoneNumFrame.grid(row = 4, columnspan = 2)

        #HPLabel
        PhoneNumLbl = tk.Label(PhoneNumFrame,
                         text = "Phone Number",
                         width = 15,
                         relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #HPEntry
        self.phone_num = tk.Entry(PhoneNumFrame, width = 40)
        self.phone_num.insert(0,
                              "e.g., 91234567, 81093487, 92054981, etc")
        self.phone_num.pack(side = tk.LEFT)

        #EmailFrame
        EmailFrame = tk.Frame(self.root)
        EmailFrame.grid(row = 5, columnspan = 2)

        #EmailLabel
        EmailLbl = tk.Label(EmailFrame,
                         text = "Email Address",
                         width = 15,
                         relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #EmailEntry
        self.email_add = tk.Entry(EmailFrame, width = 40)
        self.email_add.insert(0,
                              "e.g., ALSuser@als.edu")
        self.email_add.pack(side = tk.LEFT)

        # buttons
        creation_btn = tk.Button(self.root,
                                 text="Create Member",
                                 padx=20, pady=10,
                                 command=lambda:self.tbl_member())
                                 
        exit_btn = tk.Button(self.root,
                             text="Back to main menu",
                             padx=20, pady=10,
                             command=lambda:self.root.destroy())

        creation_btn.grid(row = 6,column = 0)
        exit_btn.grid(row = 6, column = 1)

    def containsLetterAndNumber(self,test):
        has_letter = False
        has_number = False
        for x in test:
            if x.isalpha():
                has_letter = True
            elif x.isnumeric():
                has_number = True
            if has_letter and has_number:
                return True
        return False

    def tbl_member(self):
        real_mem_id = self.mem_id.get()
        real_name = self.name.get()
        real_faculty = self.faculty.get()
        real_phone_num = 0
        real_email_add = self.email_add.get()

        if self.containsLetterAndNumber(real_mem_id):
            pass
        else:
            messagebox.showwarning("showwarning", "Membership ID is not alphanumeric!")
            return
            
        if len(self.phone_num.get()) != 8: #Valid phone number
            messagebox.showwarning("showwarning", "Not a phone number!")
            return

        for char in self.email_add.get(): #valid email-still need check for other special characters?
            if "@" not in self.email_add.get() or "." not in self.email_add.get():
                messagebox.showwarning("showwarning", "Not an Email Address!")
                return

        try: #Check Int
            real_phone_num = int(self.phone_num.get())
        except:
            messagebox.showwarning("showwarning", "Not a phone number!")
            return

        result = (real_mem_id,real_name,real_faculty,real_phone_num,real_email_add)

        for ele in result: #Blank Fields
            if ele == "":
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
                t = "INSERT INTO `library`.`membership` (`membership_id`, `name`, `faculty`, `phone_number`, `email`) VALUES (%s, %s, %s, %s,%s)"
                try:
                    cursor.execute(t, result)
                    con.commit()
                except:
                    messagebox.showwarning("showwarning", "Membership ID is taken!")
                    return
        messagebox.showinfo("showinfo", "Success! \n ALS Membership created.")
        self.root.destroy()
class class_delete: #delete intro
    def __init__(self,root):
        self.root = root
        self.root.title("Membership Deletion")
        start = tk.Label(self.root,
                         text="To Delete Member, Please Enter Membership ID:",
                         padx = 10)
        start.grid(row = 0, columnspan=2)


        #MembershipEntryFrame
        MEFrame = tk.Frame(self.root)
        MEFrame.grid(row = 1, columnspan = 2)

        #MembershipEntryLabel
        MELbl = tk.Label(MEFrame,
                         text = "Membership ID",
                         width = 15,
                         relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #MembershipEntry
        self.mem_id = tk.Entry(MEFrame, width = 40)
        self.mem_id.insert(0,
                           "A unique alphanumeric id that distinguishes every member")
        self.mem_id.pack(side = tk.LEFT)

        deletion_btn = tk.Button(self.root,
                                 text="Delete Member",
                                 padx=20, pady=10,
                                 command=lambda:self.tbl_del_mem())
        
        deletion_btn.grid(row = 2,column = 0)
                                 
        exit_btn = tk.Button(self.root,
                             text="Back to main menu",
                             padx=20, pady=10,
                             command=lambda:self.root.destroy())
    
        exit_btn.grid(row = 2, column = 1)

    def tbl_del_mem(self):
        mem_del = self.mem_id.get()
        if mem_del == "":
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
                    t = 'SELECT * FROM library.membership WHERE membership_id = %s; '
                    cursor.execute(t, mem_del)
                    result = cursor.fetchone()
                    con.commit()
                except:
                    messagebox.showwarning("showwarning", "Membership ID does not exist!")
                    return
        del_func_class(tk.Toplevel(self.root), result)
    
class del_func_class:
    def __init__(self, root, result):
        self.root = root
        self.result = result
        if result is None:
            messagebox.showwarning("showwarning", "Membership ID does not exist!")
            self.root.title("Try Again")
            button = tk.Button(self.root,
                               text = "Return",
                               bg = "indian red",
                               highlightbackground = "red",
                               fg = "black",
                               command=lambda:self.root.destroy()).pack(padx = 50)
        else:
            self.root.title("Confirmation")
            tk.Label(self.root, text = "Please confirm details to be correct: ").grid(row = 0, columnspan=2)
        
            info_frame = tk.Frame(self.root)
            info_frame.grid(row = 1, columnspan = 2)
            fields = ("Membership ID", "Name", "Faculty", "Phone Number", "Email Address")
            i = 1
            for i in range(len(fields)):
                tk.Label(info_frame,
                         text = f"{fields[i]}").grid(row = i + 1, column = 0)                   

            for i in range(len(result)):
                tk.Label(info_frame,
                         text = f"{self.result[i]}",
                         relief = tk.GROOVE, width = 30).grid(row=i+1, column = 1)

            confirm_btn = tk.Button(self.root,
                                    text = "Confirm deletion",
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
                if self.check_fines() or self.check_loans():
                    messagebox.showwarning("showwarning", "ERROR! \n Member has loans, reservations or outstanding fines!")
                    return
                elif self.check_reservations():
                    t = 'DELETE FROM library.reservation WHERE membership_id = %s; '
                    cursor.execute(t, self.result[0])
                    messagebox.showinfo("showinfo", "Reservations Cancelled")
                    con.commit()
                    s = 'DELETE FROM library.membership WHERE membership_id = %s; '
                    cursor.execute(s, self.result[0])
                    con.commit()
                else:
                    t = 'DELETE FROM library.membership WHERE membership_id = %s; '
                    cursor.execute(t, self.result[0])
                    con.commit()
        messagebox.showinfo("showinfo", "Member Deleted")
        self.root.destroy()
        
    def check_fines(self): # use selfmemid to check for its instance in the library.fine entity
        #print(self.result[0])
        mem_id = str(self.result[0])
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                t = 'SELECT * FROM library.fine WHERE membership_id_fined = %s AND amount_fined != 0; '
                cursor.execute(t, mem_id)
                res = cursor.fetchone()
                con.commit()
                print(res)
                if res is None:
                    return False
                else:
                    return True

    def check_reservations(self): # use selfmemid to check for its instance in the library.reservation entity
        mem_id = str(self.result[0])
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                t = 'SELECT * FROM library.reservation WHERE membership_id = %s; '
                cursor.execute(t, mem_id)
                res = cursor.fetchone()
                con.commit()
                print(res)
                if res is None:
                    return False
                else:
                    return True

    def check_loans(self):# use selfmemid to check for its instance in the library.book entity
        mem_id = str(self.result[0])
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                t = 'SELECT * FROM library.book WHERE membership_id_borrowed = %s; '
                cursor.execute(t, mem_id)
                res = cursor.fetchone()
                con.commit()
                if res is None:
                    return False
                else:
                    return True

class class_update: #update intro
    def __init__(self,root):
        self.root = root
        self.root.title("Membership Update")
        start = tk.Label(self.root,
                         text="To Update a Member, Please Enter Membership ID:",
                         padx = 10)
        start.grid(row = 0, columnspan=2)


        #MembershipEntryFrame
        MEFrame = tk.Frame(self.root)
        MEFrame.grid(row = 1, columnspan = 2)

        #MembershipEntryLabel
        MELbl = tk.Label(MEFrame,
                         text = "Membership ID",
                         width = 15,
                         relief = tk.GROOVE).pack(padx = 5, side = tk.LEFT)

        #MembershipEntry
        self.mem_id = tk.Entry(MEFrame, width = 40)
        self.mem_id.insert(0,
                           "A unique alphanumeric id that distinguishes every member")
        self.mem_id.pack(side = tk.LEFT)

        update_btn = tk.Button(self.root,
                                 text="Update Member",
                                 padx=20, pady=10,
                                 command=lambda:self.tbl_update_mem())
        
        update_btn.grid(row = 2,column = 0)
                                 
        exit_btn = tk.Button(self.root,
                             text="Back to main menu",
                             padx=20, pady=10,
                             command=lambda:self.root.destroy())
    
        exit_btn.grid(row = 2, column = 1)

    def tbl_update_mem(self):
        mem_update = self.mem_id.get()
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        
        with con:
            with con.cursor() as cursor:
                try:
                    t = 'SELECT * FROM library.membership WHERE membership_id = %s; '
                    cursor.execute(t, mem_update)
                    result = cursor.fetchone()
                    self.new_window = tk.Toplevel(self.root)
                    self.app = update_func_class(self.new_window, result)
                    con.commit()
                except:
                    messagebox.showwarning("showwarning", "Membership ID does not exist!")
                    return
        #update_func_class(tk.Toplevel(self.root), result)

class update_func_class:
    def __init__(self, root, result):
        self.root = root
        self.result = result
        if result is None:
            messagebox.showwarning("showwarning", "Membership ID does not exist!")
            self.root.title("Try Again")
            button = tk.Button(self.root,
                               text = "Return",
                               bg = "indian red",
                               highlightbackground = "red",
                               fg = "black",
                               command=lambda:self.root.destroy()).pack(padx = 50)
        else:
            self.root.title("Update")
            tk.Label(self.root,
                     text = "Please Enter Requested Infornmation Below: ").grid(row = 0, columnspan=2)
            info_frame = tk.Frame(self.root)
            info_frame.grid(row = 1, columnspan = 2)
            fields = ("Membership ID", "Name", "Faculty", "Phone Number", "Email Address")
            i = 1
            self.mem_id = tk.Label(info_frame, text = f"{result[0]}")
            self.mem_id.grid(row = 1, column = 1)
            for i in range(len(fields)):
                tk.Label(info_frame,
                         text = f"{fields[i]}").grid(row = i + 1, column = 0)

            self.name = tk.Entry(info_frame, width=30)
            self.name.insert(0,f"{result[1]}")
            self.name.grid(row = 2, column = 1)
            self.faculty = tk.Entry(info_frame, width=30)
            self.faculty.insert(0,f"{result[2]}")
            self.faculty.grid(row = 3, column = 1)
            self.phone_num = tk.Entry(info_frame, width=30)
            self.phone_num.insert(0,f"{result[3]}")
            self.phone_num.grid(row = 4, column = 1)
            self.email_add = tk.Entry(info_frame, width=30)
            self.email_add.insert(0,f"{result[4]}")
            self.email_add.grid(row = 5, column = 1)

            updating_btn = tk.Button(self.root,
                                     text="Update Member",
                                     padx=20, pady=10, width = 14,
                                     command=lambda:self.update_mem())                         
            exit_btn = tk.Button(self.root,
                                 text="Return",
                                 padx=20, pady=10, width = 14,
                                 command=lambda:self.root.destroy())

            updating_btn.grid(row = 6,column = 0)
            exit_btn.grid(row = 6, column = 1)

    def update_mem(self):
        upd_name = self.name.get()
        upd_faculty = self.faculty.get()
        upd_phone_num = 0
        upd_email_add = self.email_add.get()
        
        if len(self.phone_num.get()) != 8: #Valid phone number
            messagebox.showwarning("showwarning", "Not a phone number!")
            return

        for char in self.email_add.get(): #valid email-still need check for other special characters?
            if "@" not in self.email_add.get() or "." not in self.email_add.get():
                messagebox.showwarning("showwarning", "Not an Email Address!")
                return

        try: #Check Int
            upd_phone_num = int(self.phone_num.get())
        except:
            messagebox.showwarning("showwarning", "Not a phone number!")
            return

        result = (self.mem_id.cget("text"),upd_name,upd_faculty,upd_phone_num,upd_email_add)

        for ele in result: #Blank Fields
            if ele == "":
                messagebox.showwarning("showwarning", "Missing or Incomplete fields")
                return
        confirm_update(tk.Toplevel(self.root), result)

class confirm_update:
    def __init__(self,root,result):
        self.root = root
        self.result = result
        self.root.title("Confirmation")
        confirm_label = tk.Label(master = self.root, text = "Please confirm update details to be correct: ")
        confirm_label.grid(row = 0, columnspan = 2)
##        print(result)
##        for i in range(len(result)):
##            tk.Label(self.root, text = f"{self.result[i]}").grid(row=i+1)

        info_frame = tk.Frame(self.root)
        info_frame.grid(row = 1, columnspan = 2)
        fields = ("Membership ID", "Name", "Faculty", "Phone Number", "Email Address")
        i = 1
        for i in range(len(fields)):
            tk.Label(info_frame,
                     text = f"{fields[i]}").grid(row = i + 1, column = 0)
            
        for i in range(len(result)):
            tk.Label(info_frame,
                     text = f"{self.result[i]}",
                     relief = tk.GROOVE, width = 30).grid(row=i+1, column = 1)

        confirm_btn = tk.Button(self.root,
                                text = "Confirm update",
                                padx=20, pady=10,
                                command=lambda:self.confirmUpd())
        confirm_btn.grid(row = 6,column = 0)

        back_btn = tk.Button(self.root,
                             text = "Back to update function",
                             padx=20, pady=10,
                             command=lambda:self.root.destroy())
        back_btn.grid(row = 6, column = 1)



    def confirmUpd(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='1145joellenG.', #CHANGE THIS
            database='library'
            )
        with con:
            with con.cursor() as cursor:
                try:
                    t = f'UPDATE library.membership SET name = "{self.result[1]}" ,faculty= "{self.result[2]}" ,phone_number = "{self.result[3]}", email = "{self.result[4]}" WHERE membership_id = "{self.result[0]}"; '
##                    print(t)
                    cursor.execute(t)
                    con.commit()
                except:
                    messagebox.showwarning("showwarning", "Error! \n Missing or Incomplete fields!")
                    return
        messagebox.showinfo("showinfo", "Success! \n ALS Membership updated.")
        self.root.destroy()
        

            

            
            
    

        

        
        








        
