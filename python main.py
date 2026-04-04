import tkinter as tk
from tkinter import messagebox

#Initializing a nested dictionary to store student info
#(www.w3schools.com, n.d.)
students_dict = {}

#(GeeksforGeeks, 2024)
def idlinear_search(id_list, target_id):
    for i in range(len(id_list)):
        if id_list[i] == target_id:
            return i
    return -1

def search_student():
    id_target = ent_id.get().strip()
    #(www.w3schools.com, n.d.)
    students_ids = list(students_dict.keys())    #searching the students by ids using keys()
    index = idlinear_search(students_ids, id_target)
    
    if index != -1:      #Checking the validation using if/else
        found_id = students_ids[index]
        student = students_dict[found_id]
        gra = student["Grades"]
        #(GeeksforGeeks, 2019)
        average_update.set(f"Found: {student['Name']} | M:{gra['Math']} S:{gra['Science']} IT:{gra['IT']}")   #f-string 
        messagebox.showinfo("Search Result", f"Student {student['Name']} found!")
    else:
        average_update.set("Error: ID not found")
        messagebox.showerror("Search Result", "That Student ID does not exist.")

#(GeeksforGeeks, 2014)
def bubble_sorting_students(sorting_list):
    n = len(sorting_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorting_list[j][0] < sorting_list[j + 1][0]:
                sorting_list[j], sorting_list[j + 1] = sorting_list[j + 1], sorting_list[j]
                swapped = True
        if not swapped:
            break
    return sorting_list

def sorting_students():
    output_list = []
    #(www.w3schools.com, n.d.)  
    for students_id, info in students_dict.items():
        grades = info["Grades"].values()
        avg = sum(grades) / len(grades)
        output_list.append([avg, info["Name"]])

    #(GeeksforGeeks, 2020)
    if not output_list:
        messagebox.showwarning("Warning", "No data to sort!")
        return

    sorted_data = bubble_sorting_students(output_list)
    print("\n Student Rankings (Sorted by Average) ")
    
    rank = 1    #Using a manual counter to count 
    for student in sorted_data:
        print(f"{rank}. {student[1]}: {student[0]:.2f}")  #f-string 
        rank += 1
    messagebox.showinfo("Sorting Complete", "Ranks printed to console.")

def adding_info_grades():
    #(W3Schools, n.d.) for using strip() 
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

        #(W3Schools, 2019) for file read/write
        #Creating and adding the input to text file 
        with open("E:\Final\Final-Project\student_data.txt", "a") as file:
            file.write(f"ID:{upd_id}, Name:{upd_name}, Math:{m_grade}, Science:{s_grade}, IT:{i_grade}, Average:{average:.2f}\n")

    except ValueError:
        print("Error: Please make sure ID is entered and grades are numeric!")

#(GeeksforGeeks, 2017)
#Creating the window
root = tk.Tk()
root.title("Student Progress Tracker")
root.geometry("400x600")   #Setting the size of window

font_size_label = ("Arial", 9, "bold")
font_size_entry = ("Arial", 12)

#(GeeksforGeeks, 2020) for entry box widgets
#Creating the entry using labels
tk.Label(root, text="Student ID:", font=font_size_label).grid(row=0, column=0, columnspan=2, pady=(20,0))
ent_id = tk.Entry(root, font=font_size_entry, justify='center', width=25, borderwidth=1, relief="solid")
ent_id.grid(row=1, column=0, columnspan=2,pady=(5,15))    #(GeeksforGeeks, 2019) for using grid()

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

#(GeeksforGeeks, 2019) for buttons 
#Linking the function of add_student_data with button using command 
submit_button = tk.Button(root, text="Add Data", width=15, command=adding_info_grades)
submit_button.grid(row=10, column=0, columnspan=2, pady=20)

searching_button = tk.Button(root, text="SEARCHING BY ID", width=15, command=search_student)
searching_button.grid(row=11, column=0, padx=10, pady=5)

sorting_button = tk.Button(root, text="SORTING ALL", width=15, command=sorting_students)
sorting_button.grid(row=11, column=1, padx=10, pady=5)

#(GeeksforGeeks, 2019)
#I got this idea from Chat GPT to access the labels with StringVar() 
average_update = tk.StringVar()
average_update.set("System Ready") #setting as a default text

#(GeeksforGeeks, 2020)
result_label = tk.Label(root, textvariable=average_update, font=("Arial", 12, "bold"), fg="purple") #This is the code for changes
result_label.grid(row=13, column=0, columnspan=2, pady=10)

root.mainloop()   #Output GUI