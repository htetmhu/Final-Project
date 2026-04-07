import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

#Initializing a nested dictionary to store student info
#(www.w3schools.com, n.d.)
students_dict = {}

def loading_data():
    #Reading the text file.
    try:
        with open("E:\Final\Final-Project\student_data.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line: 
                    continue
                parts = line.split(", ")
                try:
                    #(GeeksforGeeks, 2020)
                    #placing the variables into index places.
                    students_id = parts[0].split(":")[1]
                    student_name = parts[1].split(":")[1]
                    math = float(parts[2].split(":")[1])
                    sci = float(parts[3].split(":")[1])
                    it = float(parts[4].split(":")[1])

                    students_dict[students_id] = {
                        "Name": student_name,
                        "Grades": {"Math": math, "Science": sci, "IT": it}
                    }
                #(GeeksforGeeks, 2019)
                #Handling the error message to prevent from crashing.
                except (IndexError, ValueError):
                    continue 
        print(f"System: {len(students_dict)} records loaded.")
    except FileNotFoundError:
        print("There is no data file found.")

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
        avg_update.set(f"Found: {student['Name']} | M:{gra['Math']} S:{gra['Science']} IT:{gra['IT']}")   #f-string 
        messagebox.showinfo("Search Result", f"Student {student['Name']} found!")
    else:
        avg_update.set("Error: ID not found")
        messagebox.showerror("Search Result", "That Student ID does not exist.")

#(GeeksforGeeks, 2014)
def bubble_sorting_students(sorting_list):
    l = len(sorting_list)
    for m in range(l):
        swapped = False
        for n in range(0, l - m - 1):
            if sorting_list[n][0] < sorting_list[n + 1][0]:
                sorting_list[n], sorting_list[n + 1] = sorting_list[n + 1], sorting_list[n]
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
        m_grade = float(ent_math.get())
        s_grade = float(ent_sci.get())
        i_grade = float(ent_it.get())
        
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
        avg_update.set(f"Average for {upd_name}: {average:.2f}")
        
        print(f"Success: ID {upd_id} ({upd_name}) added with average {average:.2f}")  #using f string to print

        #(W3Schools, 2019) for file read/write
        #Creating and adding the input to text file 
        with open("E:\Final\Final-Project\student_data.txt", "a") as file:
            file.write(f"ID:{upd_id}, Name:{upd_name}, Math:{m_grade}, Science:{s_grade}, IT:{i_grade}, Average:{average:.2f}\n")

    except ValueError:
        print("Error: Please make sure ID is entered and grades are numeric!")

#Function to reset everything from the start so that user can input automatically without moving cursor
def reset_input():
    ent_id.delete(0, tk.END)   #deleting all inputs in entry box
    ent_name.delete(0,tk.END)
    ent_math.delete(0,tk.END)
    ent_sci.delete(0,tk.END)
    ent_it.delete(0,tk.END)

    ent_id.focus_set()
    avg_update.set("All fields cleared!")

#Function for charts showing how students perform during academic years
def showing_chart():
    student_id = ent_id.get().strip()
    if student_id in students_dict:
        students = students_dict[student_id]
        subjects = list(students["Grades"].keys())
        scores = list(students["Grades"].values())
        plt.figure(figsize=(6, 4))
        plt.bar(subjects, scores, color=['#4851ee', '#4dd698', '#8034cf'])
        plt.title(f"Grades for {students['Name']}")
        plt.ylabel("Score")
        plt.xlabel(f"Subjects that {students['Name']} takes")
        plt.ylim(0, 100)
        plt.show()
    else:
        messagebox.showerror("Error", "Firstly, please enter a valid ID to view the chart.")

#(GeeksforGeeks, 2017)
#Creating the window
root = tk.Tk()
root.title("Student Progress Tracker")

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
ent_math = tk.Entry(root, font=font_size_entry, justify='center', width=25, borderwidth=1, relief="solid")
ent_math.grid(row=5, column=0, columnspan=2, pady=(5, 15))

tk.Label(root, text="Science Grade:", font=font_size_label).grid(row=6, column=0, columnspan=2, pady=(5, 0))
ent_sci = tk.Entry(root, font=font_size_entry, justify='center', width=25, borderwidth=1, relief="solid")
ent_sci.grid(row=7, column=0, columnspan=2, pady=(5, 15))

tk.Label(root, text="IT Grade:",font=font_size_label).grid(row=8, column=0, columnspan=2, pady=(5, 0))
ent_it = tk.Entry(root, font=font_size_entry, justify='center', width=25, borderwidth=1, relief="solid")
ent_it.grid(row=9, column=0, columnspan=2, pady=(5, 15))

#(GeeksforGeeks, 2019) for buttons 
#Linking the function of add_student_data with button using command 
submit_button = tk.Button(root, text="Add Data", width=15, command=adding_info_grades)
submit_button.grid(row=10, column=0, columnspan=2, pady=20)

searching_button = tk.Button(root, text="SEARCHING BY ID", width=15, command=search_student)
searching_button.grid(row=11, column=0, padx=10, pady=5)

sorting_button = tk.Button(root, text="SORTING ALL", width=15, command=sorting_students)
sorting_button.grid(row=11, column=1, padx=10, pady=5)

chart_button = tk.Button(root, text="STUDENT PERFORMANCE CHART", width=35, bg="#b4b4cc", font=font_size_label, command=showing_chart)
chart_button.grid(row=12, column=0, columnspan=2, pady=20)

reset_button = tk.Button(root, text="RESET", width=35, bg="#0D0D5D", font=font_size_label, command=reset_input)
reset_button.grid(row=14, column=0, columnspan=2, pady=20)


#(GeeksforGeeks, 2019)
#I got this idea from Chat GPT to access the labels with StringVar() 
avg_update = tk.StringVar()
avg_update.set("System Ready") #setting as a default text

#(GeeksforGeeks, 2020)
result_label = tk.Label(root, textvariable=avg_update, font=("Arial", 12, "bold"), fg="purple") #This is the code for changes
result_label.grid(row=13, column=0, columnspan=2, pady=10)

loading_data()
root.mainloop()   #Output GUI