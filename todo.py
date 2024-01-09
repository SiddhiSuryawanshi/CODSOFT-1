import tkinter as tk
from tkinter import ttk, messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def mark_completed():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task = listbox.get(selected_task_index)
        listbox.itemconfig(selected_task_index, {'bg': 'light green'})
        messagebox.showinfo("Task Completed", f"Task '{task}' marked as completed.")
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def clear_all_tasks():
    confirmed = messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?")
    if confirmed:
        listbox.delete(0, tk.END)

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Tasks Saved", "Tasks saved to 'tasks.txt'.")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        listbox.delete(0, tk.END)
        for task in tasks:
            listbox.insert(tk.END, task)
        messagebox.showinfo("Tasks Loaded", "Tasks loaded from 'tasks.txt'.")
    except FileNotFoundError:
        messagebox.showwarning("File Not Found", "No saved tasks found.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set background color
root.configure(bg='lightblue')

# Create and pack widgets with styling
style = ttk.Style()
style.configure("TButton", padding=(10, 5, 10, 5), font=('Helvetica', 10))
style.configure("TEntry", padding=(10, 5, 10, 5), font=('Helvetica', 12))
style.configure("TListbox", font=('Helvetica', 12))

entry = ttk.Entry(root, width=40, style="TEntry")
entry.pack(pady=10)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

add_button = ttk.Button(button_frame, text="Add Task", command=add_task, style="TButton")
add_button.grid(row=0, column=0, padx=5)

remove_button = ttk.Button(button_frame, text="Remove Task", command=remove_task, style="TButton")
remove_button.grid(row=0, column=1, padx=5)

mark_completed_button = ttk.Button(button_frame, text="Mark Completed", command=mark_completed, style="TButton")
mark_completed_button.grid(row=0, column=2, padx=5)

clear_all_button = ttk.Button(button_frame, text="Clear All Tasks", command=clear_all_tasks, style="TButton")
clear_all_button.grid(row=0, column=3, padx=5)

save_button = ttk.Button(button_frame, text="Save Tasks", command=save_tasks, style="TButton")
save_button.grid(row=0, column=4, padx=5)

load_button = ttk.Button(button_frame, text="Load Tasks", command=load_tasks, style="TButton")
load_button.grid(row=0, column=5, padx=5)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, font=('Helvetica', 12))
listbox.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
