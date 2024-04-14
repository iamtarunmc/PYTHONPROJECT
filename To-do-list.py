import tkinter as tk

task_counter = 1

def add_task():
    global task_counter
    task = entry_task.get()
    if task:
        task_with_number = f"{task_counter}. {task}"
        listbox_tasks.insert(tk.END, task_with_number)
        entry_task.delete(0, tk.END)
        task_counter += 1

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        pass

def clear_tasks():
    global task_counter
    listbox_tasks.delete(0, tk.END)
    task_counter = 1

root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50,font=("Bold",10),fg="Black",bg="light grey")
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task",fg="green", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task",fg="blue", width=48, command=delete_task)
button_delete_task.pack()

button_clear_tasks = tk.Button(root, text="Clear All Tasks",fg="red", width=48, command=clear_tasks)
button_clear_tasks.pack()

root.mainloop()