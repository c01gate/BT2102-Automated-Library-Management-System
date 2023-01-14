import tkinter as tk
import membership_intro as mem
import fines_intro as fin
import reports_intro as rep
import reserve_intro as res
import loans_intro as loan
import books_intro as book

class first:
    def __init__(self, root):
        self.root = root
        self.root.title("Intro")

        start_message = tk.Label(text="Welcome to ALS")
        #add message that cannot be interacted
        start_message.grid(row=0,columnspan=3)
        #interface size wraps arnd message

        btn_membership = tk.Button(
            text="Membership!",
            width=25,
            height=5,
            bg="blue",
            fg="yellow",
        )
        btn_membership.grid(row=1, column=0)
        btn_membership.bind("<Button-1>", self.to_member)

        btn_books = tk.Button(
            text="Books!",
            width=25,
            height=5,
            bg="blue",
            fg="purple",
        )
        btn_books.grid(row=1, column=1)
        btn_books.bind("<Button-1>", self.to_books)

        btn_loans = tk.Button(
            text="Loans!",
            width=25,
            height=5,
            bg="blue",
            fg="white",
        ) 
        btn_loans.grid(row=1, column=2)
        btn_loans.bind("<Button-1>", self.to_loans)

        btn_reservations = tk.Button(
            text="Reservations!",
            width=25,
            height=5,
            bg="blue",
            fg="black",
        )
        btn_reservations.grid(row=2, column=0)
        btn_reservations.bind("<Button-1>", self.to_reservations)

        btn_fines = tk.Button(
            text="Fines!",
            width=25,
            height=5,
            bg="blue",
            fg="blue",
        )  
        btn_fines.grid(row=2, column=1)
        btn_fines.bind("<Button-1>", self.to_fines)

        btn_reports = tk.Button(
            text="Reports!",
            width=25,
            height=5,
            bg="blue",
            fg="green",
        )  
        btn_reports.grid(row=2, column=2)
        btn_reports.bind("<Button-1>", self.to_reports)
        
    def to_member(self,event):
        self.new_window = tk.Toplevel(self.root)
        self.app = mem.membership_window(self.new_window)
        
    def to_reports(self,event):
        self.new_window = tk.Toplevel(self.root)
        self.app = rep.report_window(self.new_window)
        
    def to_fines(self,event):
        self.new_window = tk.Toplevel(self.root)
        self.app = fin.fine_window(self.new_window)
        
    def to_reservations(self,event):
        self.new_window = tk.Toplevel(self.root)
        self.app = res.reserve_window(self.new_window)
        
    def to_loans(self,event):
        self.new_window = tk.Toplevel(self.root)
        self.app = loan.loan_window(self.new_window)
        
    def to_books(self,event):
        self.new_window = tk.Toplevel(self.root)
        self.app = book.book_window(self.new_window)
    #to edit the member window just redefine this function in another python file
    #then import the function after
        
def main():
    window_start = tk.Tk()
    app = first(window_start)
    window_start.mainloop()

if __name__ == '__main__':
    main()
    #allows interface to listen for button clicks etc
    #blocks any code that comes after it from running
    #until the window it’s called on is closed

