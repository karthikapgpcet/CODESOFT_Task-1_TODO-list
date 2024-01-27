import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.create_widgets()

    def create_widgets(self):
        # Frame
        self.frame = Frame(self.master,bg="#DED0B6")
        self.frame.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        # Date Picker
        self.date_entry = DateEntry(self.frame, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        # Task Entry
        self.task_entry = Entry(self.frame, width=25,font=("Helvetica",11), bg="#FEFAE0",fg="#6B240C",selectbackground="#B99470")
        self.task_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        # Add Button
        self.add_button = Button(self.frame, text="Add Task", command=self.add_task,bg="#9A4444",fg="#FAEED1", font=("Helvetica",11,"bold"), cursor='hand2',  takefocus=False)
        self.add_button.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

        # Task Listbox
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10,font=("Helvetica",11,"bold"), bg="#FEFAE0", fg="#6B240C",activestyle="none", selectbackground="#B99470")
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)

        # Delete Button
        self.delete_button = Button(self.frame, text="Delete Task", command=self.delete_task,bg="#9A4444",fg="#FAEED1",font=("Helvetica",11,"bold"), cursor='hand2',  takefocus=False)
        self.delete_button.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        # Mark as Complete Checkbox
        self.complete_button = Button(self.frame, text="Mark as completed", command=self.mark_complete,bg="#9A4444",fg="#FAEED1",font=("Helvetica",11,"bold"),  cursor='hand2',  takefocus=False)
        self.complete_button.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        # Completed Tasks
        self.completed_tasks = Button(self.frame, text="Refresh completed Tasks", command=self.tasks_completed,bg="#9A4444",fg="#FAEED1",font=("Helvetica",11,"bold"),  cursor='hand2',  takefocus=False)
        self.completed_tasks.grid(row=2, column=2, padx=5, pady=5,sticky=tk.W)

        # New Frame for Completed Tasks
        self.completed_frame = Frame(self.master,bg="#DED0B6")
        self.completed_frame.grid(row=1, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

        # Completed Tasks Listbox
        self.completed_listbox = tk.Listbox(self.completed_frame, width=50, height=5,font=("Helvetica",11,"bold"), bg="#FEFAE0",fg="#6B240C",activestyle="none", selectbackground="#B99470")
        self.completed_listbox.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

    def add_task(self):
        date = self.date_entry.get_date().strftime('%Y-%m-%d')
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, f"{date} - {task}")
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        task = self.task_listbox.get(tk.ACTIVE)
        result = messagebox.askokcancel("Confirmation", "Do you want to delete the selected task?")
        if result:
            self.task_listbox.delete(tk.ACTIVE)
        

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.completed_listbox.insert(tk.END, f"{task} - Completed")

    def tasks_completed(self):
        result = messagebox.askokcancel("Confirmation", "Do you want to refresh completed tasks?")
        if result:
            # Reset completed tasks listbox
            self.completed_listbox.delete(0, tk.END)

            # Populate completed tasks listbox
            for task in self.task_listbox.get(0, tk.END):
                if "Completed" in task:
                    self.completed_listbox.insert(tk.END, task)


root = tk.Tk()
root.configure(bg="blue")
app = ToDoApp(root)
root.mainloop()