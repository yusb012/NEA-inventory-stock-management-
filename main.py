import tkinter
from tkinter import messagebox
#creating main window
window= tkinter.Tk()
window.title('login form')
window.geometry('340x440')

def login():
    username='Yusuf'
    password='Password'
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title='login', message='login successful')
        window.destroy()
        import SystemGUI
    else:
        messagebox.showerror(title='login', message='login failed')
      

#creating widgets
login_label= tkinter.Label(window, text='login')
login_label.grid(row=0, column=0, columnspan=2)

username_label=tkinter.Label(window, text='username')
username_label.grid(row=1, column=0)
username_entry=tkinter.Entry(window)
username_entry.grid(row=1, column=1)

password_label=tkinter.Label(window, text='password')
password_label.grid(row=2, column=0)
password_entry=tkinter.Entry(window, show='*')
password_entry.grid(row=2, column=1)

login_button=tkinter.Button(window, text='submit login',command=login)
login_button.grid(row=3, column=0, columnspan=2,)











window.mainloop()