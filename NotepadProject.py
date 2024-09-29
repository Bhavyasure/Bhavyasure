import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file = filedialog.askopenfile(mode='r')
    if file:
        content = file.read()
        text_area.insert(tk.INSERT, content)

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        content = text_area.get(1.0, tk.END)
        file.write(content)
        file.close()

def exit_app():
    root.quit()

def about():
    messagebox.showinfo("About", "Simple Notepad App")

root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

# Add text area
text_area = tk.Text(root)
text_area.pack(expand=True, fill='both')

# Add menu
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
root.mainloop()
