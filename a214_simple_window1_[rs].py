#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

def test_my_button():
    frame_auth.tkraise()
    password = ent_password.get()
    lbl_auth_password.config(text=password)

# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.title('Authorization')
frame_login = tk.Frame(root)

frame_login.grid(row=0, column=0, sticky="news")

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login,text="Password:")
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3, show="*")
ent_password.pack()

btn_login = tk.Button(frame_login, text="Login", command=test_my_button)
btn_login.pack()


frame_auth = tk.Frame(root) 
frame_auth.grid(row=0,column=0,sticky="news")
lbl_auth_password = tk.Label(frame_auth, text="password")
lbl_auth_password.pack()

frame_login.tkraise()



root.mainloop()