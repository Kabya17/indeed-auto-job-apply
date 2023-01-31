from tkinter import *
from tkinter import ttk
from apply_job import apply_job

def main():
    #Create an instance of Tkinter frame
    win= Tk()

    #Set the geometry of Tkinter frame
    win.title("Indeed Auto Job Apply")
    win.geometry("750x500")

    def start_apply():
        global job_title, no_of_job, location, email, password, msg_entry
    
        print(job_title.get(), no_of_job.get(), location.get(), email.get(), password.get())

        msg_entry['text'] = "Applying Job..."
        msg_entry.pack()
        
        apply_job()
        
        msg_entry['text'] = "Apply Job Completed"
        msg_entry.pack()

        
    #Initialize a Label to display the User Input
    # label.pack()

    #User Email
    Label(win, text="Indeed email address:", font=("Courier 14")).pack()
    email= Entry(win, width= 40)
    email.pack()

    #User password
    Label(win, text="Indeed password:", font=("Courier 14")).pack()
    password= Entry(win, width= 40)
    password.pack()

    #Job Title/keyword
    Label(win, text="Job title, keyword:", font=("Courier 14")).pack()
    job_title= Entry(win, width= 40)
    job_title.pack()

    #Job Location
    Label(win, text="Job location:", font=("Courier 14")).pack()
    location= Entry(win, width= 40)
    location.pack()

    #Number of jobs
    Label(win, text="How many jobs to apply:", font=("Courier 14")).pack()
    no_of_job= Entry(win, width= 40)
    no_of_job.pack()


    #Response
    msg_entry = Label(win, text="", font=("Courier 14"))
    msg_entry.pack()

    #Submit Button
    Button(win, text="Submit",width=20, command=start_apply).pack(pady=20)

    win.mainloop()

if __name__ == "__main__":
    main()