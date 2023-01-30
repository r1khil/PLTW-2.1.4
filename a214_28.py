import tkinter as tk
root = tk.Tk()
root.wm_geometry("300x300")


blue_frame = tk.Frame(root, width=200, height=150, background="blue")
blue_frame.grid(row=0, column=0, sticky="news")

green_frame = tk.Frame(root, width=100, height=150, background="green")
green_frame.grid(row=0, column=1, sticky="news")

red_frame = tk.Frame(root, width=200, height=150, background="red")
red_frame.grid(row=1, column=0, sticky="news")

yellow_frame = tk.Frame(root, width=100, height=150, background="yellow")
yellow_frame.grid(row=1, column=1, sticky="news")

root.mainloop()