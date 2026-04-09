import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

#Initializing a nested dictionary to store student info
#(www.w3schools.com, n.d.) for accessing dictionary 
students_dict = {}

def loading_data():
    #Reading the text file and fill in the dictionary on startup. This ensures that data continues even after the program is closed.
    try:
        #(W3Schools, 2019) for file read/write
        with open("student_data.txt", "r") as file:
            for line in file:
                #(W3Schools, n.d.) for using strip()
                line = line.strip()
                if not line: 
                    continue
                parts = line.split(", ")
                try:
                    #(GeeksforGeeks, 2020) for slicing and index places.
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
                #(GeeksforGeeks, 2019) for multiple error handling 
                #Handling the error message to prevent from crashing.
                except (IndexError, ValueError):
                    continue 
        messagebox.showinfo("Data Loaded", f"System: {len(students_dict)} records loaded successfully.")

    except FileNotFoundError:
    # Changed from print to warning messagebox
        messagebox.showwarning("File Missing", "There is no data file found. A new one will be created when you add a student.")

#(GeeksforGeeks, 2024) (Searching Algorithms)
#This function is for simple and effective for small-to-medium datasets. 
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

#(GeeksforGeeks, 2014) (Bubble Sorting Algorithms)
#This function is easy to implement and illustrate the logic of comparison sorting.
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

def sorting_students():  #This is displaying the output with Messagebox instead of just the console. 
    output_list = []
    #(www.w3schools.com, n.d.)  
    for students_id, info in students_dict.items():
        grades = info["Grades"].values()
        avg = sum(grades) / len(grades)
        output_list.append([avg, info["Name"]])

    #(GeeksforGeeks, 2020) for messagebox
    if not output_list:
        messagebox.showwarning("Warning", "No data to sort!")
        return

    sorted_data = bubble_sorting_students(output_list)

    report = "--- STUDENT RANKINGS BY AVERAGE ---\n\n"
    report = report + "RANK | NAME | AVERAGE\n"
    
    rank = 1   #Looping through sorted data and add lines to 'report' string 
    for student in sorted_data:
        name = student[1]
        score = round(student[0], 2)
        line = str(rank) + ". " + name + ": " + str(score) + "\n"
        report = report + line
        rank += 1
    messagebox.showinfo("Sorting Results", report)  #Showing the final report string in a messagebox


def adding_info_grades():  
    #adding id and name using strip so that it removes the whitespaces 
    upd_id = ent_id.get().strip()
    upd_name = ent_name.get().strip()

    #Checking input validation for grades ranges and empty strings 
    if not upd_id or not upd_name:
        messagebox.showwarning("Input Error!", "Student ID and Name cannot be empty!")
        return
    
    #(Python Tutorial - Master Python Programming For Beginners from Scratch, n.d.) for askyesno() for overwriting the student info
    if upd_id in students_dict:
        if not messagebox.askyesno(title="Overwrite?", message="This ID already exists. Do you want to update it?"):
            return
    
    try:
        m_grade = float(ent_math.get())
        s_grade = float(ent_sci.get())
        i_grade = float(ent_it.get())

        #(GeeksforGeeks, 2020) for any() 
        #I got this idea from online as I searched, I used this to have a boundary between 0 to 100 so that user cannot input the negative. 
        if any(grade < 0 or grade > 100 for grade in [m_grade, s_grade, i_grade]):
            messagebox.showerror("Validation Error", "Grades must be between 0 and 100.")
            return
        
        #Using id as primary key to access
        students_dict[upd_id] = {
            "Name": upd_name,
            "Grades": {"Math": m_grade, "Science": s_grade, "IT": i_grade}
        }
        
        # Average Calculation
        average = (m_grade + s_grade + i_grade) / 3 
        avg_update.set(f"Average for {upd_name}: {average:.2f}")
        
        #File handling in safer way
        try:
            with open("student_data.txt", "w") as file:
                for stu_id, information in students_dict.items():
                    gra = information["Grades"]
                    line_avg = sum(gra.values()) / len(gra)
                    file.write(f"ID:{stu_id}, Name:{information['Name']}, Math:{gra['Math']}, Science:{gra['Science']}, IT:{gra['IT']}, Average:{line_avg:.2f}\n")
            
            messagebox.showinfo("Success", "Student data saved successfully!")
        except:
            messagebox.showerror("File Error", "Could not save to file. Please check if the file is open elsewhere.")
    except ValueError:
        messagebox.showerror("Non-numberic Error", "Please make sure ID is entered and grades are numeric!")

#(GeeksforGeeks, 2024)
#Clears all entry boxes and returns focus to the Student ID box. This function improves User Experience by allowing quick entry of new data.
def reset_input():
    ent_id.delete(0, tk.END)   #deleting all inputs in entry box
    ent_name.delete(0,tk.END)
    ent_math.delete(0,tk.END)
    ent_sci.delete(0,tk.END)
    ent_it.delete(0,tk.END)

    ent_id.focus_set()
    avg_update.set("All fields cleared!")

#Function for charts showing how students perform during academic years. It provides a visual representation of performance for better analysis.
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

#This is UI section. 
#(GeeksforGeeks, 2017) (Creating the window)
root = tk.Tk()
root.title("Student Progress Tracker")
root.resizable(False,False)  #User cannot resize the windows either by both x or y axis. 
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
submit_button = tk.Button(root, text="Add/Update Data", width=15, command=adding_info_grades)
submit_button.grid(row=10, column=0, columnspan=2, pady=20)

searching_button = tk.Button(root, text="SEARCHING BY ID", width=15, command=search_student)
searching_button.grid(row=11, column=0, padx=10, pady=5)

sorting_button = tk.Button(root, text="SORTING ALL", width=15, command=sorting_students)
sorting_button.grid(row=11, column=1, padx=10, pady=5)

chart_button = tk.Button(root, text="STUDENT PERFORMANCE CHART", width=35, bg="#b4b4cc", font=font_size_label, command=showing_chart)
chart_button.grid(row=12, column=0, columnspan=2, pady=20)

reset_button = tk.Button(root, text="RESET", width=35, bg="#5BED2F", font=font_size_label, command=reset_input)
reset_button.grid(row=14, column=0, columnspan=2, pady=20)


#(GeeksforGeeks, 2019) for using StringVar()
#I got this idea from Chat GPT to access the labels with StringVar() 
avg_update = tk.StringVar()
avg_update.set("System Ready") #setting as a default text

#(GeeksforGeeks, 2020)
result_label = tk.Label(root, textvariable=avg_update, font=("Arial", 12, "bold"), fg="purple") #This is the code for changes
result_label.grid(row=13, column=0, columnspan=2, pady=10)

loading_data()
root.mainloop()   #Output GUI