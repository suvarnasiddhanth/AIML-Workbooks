from tkinter import *
from pathlib import Path
from tkinter import ttk
folder_path = Path("Implementations")
root = Tk()
style = ttk.Style()
style.configure("Custom.TFrame", background="light blue")
frm = ttk.Frame(root, padding=10, border=10, style="Custom.TFrame")
frm.grid()
ttk.Label(frm, text="Project Selection", font="Calibri", background="light blue").grid(column=1,row=0, pady=15)
for index, file_path in enumerate(folder_path.iterdir(), start=1):
    ttk.Button(frm, text=file_path.stem, command=root.destroy, padding=10, width=20).grid(column=1, row=index)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=index + 2, pady=10)
root.mainloop()