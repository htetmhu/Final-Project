import tkinter as tk

#Initializing a nested dictionary to store student info
#(www.w3schools.com, n.d.)
students_lists = {}

def adding_student_info():
    #Getting the information from entry
    #(GeeksforGeeks, 2020)
    name = entry_name.get().strip()
    subject = entry_name.get().strip()
    
    #(W3 Schools, 2024)
    #Coding for the validation input, not to crash so writing the code with try/except
    try:
        grade = float(entry_grade.get())
        
        #(GeeksforGeeks, 2018)
        #Creating a nested dictionary 
        if name not in students_lists:
            students_lists[name] = {}
        
        #Adding the subject to each student like Math, Science, IT --> Student 
        students_lists[name][subject] = grade
        
        #(www.w3schools.com, n.d.)
        #Calculating the averages of dictionary values 
        all_grades = students_lists[name].values()
        avg = sum(all_grades) / len(all_grades)
        
        print(f"Updated {name}: Average is {avg:.2f}")   #Using f string to print 
        
        #(www.w3schools.com, n.d.)
        #With text file, saving data permanently so that they will not deleted 
        with open("student_info_grades.txt", "w") as f:
            for name, data in students_lists.items():
                for subject, grade in data.items():
                    f.write(f"{name},{subject},{grade}\n")

    except ValueError:
        print("Error: Please enter a valid number for the grade.")


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

#Linking the function of add_student_data with button using command 
submit_btn = tk.Button(root, text="Add Data", width=15, command=adding_student_info)
submit_btn.grid(row=3, column=1, pady=10)

root.mainloop()   #Output GUI