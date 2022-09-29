import tkinter 
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To Do List by arfad")
root.iconbitmap('to_do_app code/icon.ico')

def add_task():
    task = entry_task.get()
    if task !="":
        listbox_task.insert(tkinter.END,task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task")
    
def delete_task():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task")
        
def load_task():
    try:
        tasks = pickle.load(open("tasks.dat","rb")) #bisa di ganti .txt / .dat
        listbox_task.delete(0, tkinter.END)
        for task in tasks:
            listbox_task.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks .dat")

def save_task():
    tasks = listbox_task.get(0, listbox_task.size())
    pickle.dump(tasks, open("tasks.dat", "wb")) #bisa di ganti .txt / .dat


#create GUI
frame_task = tkinter.Frame(root)
frame_task.pack()

listbox_task = tkinter.Listbox(frame_task, height=3, width=50)
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task = tkinter.Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)


entry_task = tkinter.Entry(root, width=53)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_add_task = tkinter.Button(root, text="Delete Task", width=48, command=delete_task)
button_add_task.pack()

button_add_task = tkinter.Button(root, text="Load Task", width=48, command=load_task)
button_add_task.pack()

button_add_task = tkinter.Button(root, text="Save Task", width=48, command=save_task)
button_add_task.pack()

root.mainloop()