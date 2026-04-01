import tkinter as tk

#(GeeksforGeeks, 2017)
#Initializing the window 
root = tk.Tk()
root.title("Student Progress Tracker")
root.geometry("400x300")   #Setting the size of window

#(GeeksforGeeks, 2019)
#Using labels
tk.Label(root, text="Name of Student:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Student's Subject:").grid(row=1, column=0, padx=10, pady=5)
entry_subj = tk.Entry(root)
entry_subj.grid(row=1, column=1)

tk.Label(root, text="Grade:").grid(row=2, column=0, padx=10, pady=5)
entry_grade = tk.Entry(root)
entry_grade.grid(row=2, column=1)

#(GeeksforGeeks, 2019)
#Creating buttons to access
button_submit = tk.Button(root, text="Add Data", width=15)
button_submit.grid(row=3, column=1, pady=10)

root.mainloop()   #Output GUI