import tkinter as tk
from tkinter import messagebox

#Initializing a nested dictionary to store student info
#(www.w3schools.com, n.d.)
students_dict = {}

def adding_info_grades():
    #(W3Schools, n.d.)
    #adding id and name using strip so that it removes the whitespaces 
    upd_id = ent_id.get().strip()
    upd_name = ent_name.get().strip()
    
    try:
        m_grade = float(entry_math.get())
        s_grade = float(entry_sci.get())
        i_grade = float(entry_it.get())
        
        #(GeeksforGeeks, 2018)
        #Using id as primary key to access
        students_dict[upd_id] = {
            "Name": upd_name,
            "Grades": {"Math": m_grade, "Science": s_grade, "IT": i_grade}
        }
        
        # Average Calculation
        average = (m_grade + s_grade + i_grade) / 3

        #(GeeksforGeeks, 2020)
        #Updating the average value using StringVar() to UI 
        average_update.set(f"Average for {upd_name}: {average:.2f}")
        
        print(f"Success: ID {upd_id} ({upd_name}) added with average {average:.2f}")  #using f string to print

        #(W3Schools, 2019)
        #Creating and adding the input to text file 
        with open("E:\Final\Final-Project\\student_data.txt", "a") as file:
            file.write(f"ID:{upd_id}, Name:{upd_name}, Math:{m_grade}, Science:{s_grade}, IT:{i_grade}, Average:{average:.2f}\n")

    except ValueError:
        print("Error: Please make sure ID is entered and grades are numeric!")

#(GeeksforGeeks, 2020)
#Creating the window 
root = tk.Tk()
root.title("Student Progress Tracker")
root.geometry("400x600")   #Setting the size of window

font_size_label = ("Arial", 9, "bold")
font_size_entry = ("Arial", 12)

#(GeeksforGeeks, 2021)
#(GeeksforGeeks, 2020)
#Creating the entry using labels
tk.Label(root, text="Student ID:", font=font_size_label).grid(row=0, column=0, columnspan=2, pady=(20,0))
ent_id = tk.Entry(root, font=font_size_entry, justify='center', width=25, borderwidth=1, relief="solid")
ent_id.grid(row=1, column=0, columnspan=2,pady=(5,15))

tk.Label(root, text="Name of Student:", font=font_size_label).grid(row=2, column=0, columnspan=2, pady=(5,0))
ent_name = tk.Entry(root, font=font_size_entry, justify='center', width=25, borderwidth=1, relief="solid")
ent_name.grid(row=3, column=0, columnspan=2, pady=(5,15))

tk.Label(root, text="Mathematics Grade:", font=font_size_label).grid(row=4, column=0, columnspan=2, pady=(5, 0))
entry_math = tk.Entry(root, font=font_size_entry, justify='center', width=25, borderwidth=1, relief="solid")
entry_math.grid(row=5, column=0, columnspan=2, pady=(5, 15))

tk.Label(root, text="Science Grade:", font=font_size_label).grid(row=6, column=0, columnspan=2, pady=(5, 0))
entry_sci = tk.Entry(root, font=font_size_entry, justify='center', width=25, borderwidth=1, relief="solid")
entry_sci.grid(row=7, column=0, columnspan=2, pady=(5, 15))

tk.Label(root, text="IT Grade:",font=font_size_label).grid(row=8, column=0, columnspan=2, pady=(5, 0))
entry_it = tk.Entry(root, font=font_size_entry, justify='center', width=25, borderwidth=1, relief="solid")
entry_it.grid(row=9, column=0, columnspan=2, pady=(5, 15))

#(GeeksforGeeks, 2019)
#Linking the function of add_student_data with button using command 
submit_button = tk.Button(root, text="Add Data", width=15, command=adding_info_grades)
submit_button.grid(row=10, column=0, columnspan=2, pady=20)

#(GeeksforGeeks, 2019)
#I got this idea from Chat GPT to access the labels with StringVar() 
average_update = tk.StringVar()
average_update.set("System Ready") #setting as a default text
result_label = tk.Label(root, textvariable=average_update, font=("Arial", 12, "bold"), fg="purple") #This is the code for changes
result_label.grid(row=13, column=0, columnspan=2, pady=10)

root.mainloop()   #Output GUI