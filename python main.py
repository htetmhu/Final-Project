import tkinter as tk

#Initializing a nested dictionary to store student info
#(www.w3schools.com, n.d.)
students_lists = {}

def adding_info_grades():
    #(W3Schools, n.d.)
    #adding id and name using strip so that it removes the whitespaces 
    id_update = id_entry.get().strip()
    name_update = entry_name.get().strip()
    
    try:
        math_grade = float(entry_math.get())
        sci_grade = float(entry_sci.get())
        it_grade = float(entry_it.get())
        
        #(GeeksforGeeks, 2018)
        #Using id as primary key to access
        students_lists[id_update] = {
            "Name": name_update,
            "Grades": {"Math": math_grade, "Science": sci_grade, "IT": it_grade}
        }
        
        # Average Calculation
        average = (math_grade + sci_grade + it_grade) / 3
        
        print(f"Success: ID {id_update} ({name_update}) added with average {average:.2f}")  #using f string to print

        #(W3Schools, 2019)
        #Creating and adding the input to text file 
        with open("student_data.txt", "a") as file:
            file.write(f"ID:{id_update}, Name:{name_update}, Math:{math_grade}, Science:{sci_grade}, IT:{it_grade}, Average:{average:.2f}\n")

    except ValueError:
        print("Error: Ensure ID is entered and grades are numeric!")


#(GeeksforGeeks, 2017)
#Initializing the window 
root = tk.Tk()
root.title("Student Progress Tracker")
root.geometry("400x300")   #Setting the size of window

#(GeeksforGeeks, 2019)
#Creating the entry using labels
tk.Label(root, text="Student ID:").grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

tk.Label(root, text="Name of Student:").grid(row=1, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

tk.Label(root, text="Mathematics Grade:").grid(row=2, column=0)
entry_math = tk.Entry(root)
entry_math.grid(row=2, column=1)

tk.Label(root, text="Science Grade:").grid(row=3, column=0)
entry_sci = tk.Entry(root)
entry_sci.grid(row=3, column=1)

tk.Label(root, text="IT Grade:").grid(row=4, column=0)
entry_it = tk.Entry(root)
entry_it.grid(row=4, column=1)

#(GeeksforGeeks, 2019)
#Linking the function of add_student_data with button using command 
submit_btn = tk.Button(root, text="Add Data", width=15, command=adding_info_grades)
submit_btn.grid(row= 5, column=1, pady=10)

root.mainloop()   #Output GUI