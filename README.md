APP NAME - Student Process Tracker 

GitHub Repository URL:
The source code for this project is available on GitHub: https://github.com/htetmhu/Final-Project.git

Identification:
- Name: Htet Mhu Yadi
- P-number: P513613 
- Course code: IY499

Declaration of Own Work:
I confirm that this assignment is my own work.   
Where I have referred to online sources, I have provided comments detailing the reference and included a link to the source.

Introduction:
Student Progress Tracker is a desktop software that will facilitate the process of managing academic records. Written in Python with Tkinter as the graphical user interface and Matplotlib as data-visualization, the application enables educators to store, search, sort and analyze student performance effectively. 

The main functionality of the app includes:
- Nested Data Management: It uses Python dictionaries to store student IDs, names, and a sub-dictionary of grades (Math, Science, IT).
- Visual Reporting: This is a script that creates moving bar charts in Matplotlib to display the performance of each student.
- Automated Calculations: Automatically computes academic averages of each entry.
- Data Persistence: It is an atomic file writing to make sure that the data is written permanently onto a text file without any replicas.

Installation:
To run the app locally:
1. Make sure Python 3.x is installed.
2. Clone this repository: git clone https://github.com/htetmhu/Final-Project.git
3. Install required dependencies:
   pip install matplotlib

How to Run the App:
1. Open terminal/command prompt in the project folder.
2. Run the main script:
   python main.py

Controls:
- Add/Update Students: Enter the ID, Name and the 3 subject grades and then click Add/Update Data. The average will be automatically calculated and would be saved permanently to the text file by the app.
- Computation of Averages: It is an automated background calculation. Each time a student is added or sorted, the system computes the average of Math, Science and IT scores to the nearest two decimal points.
- Data Visualization: Fill in a valid Student ID in the ID field and press on STUDENT PERFORMANCE CHART. A bar chart window using Matplotlib will appear with the distribution of scores of that particular student.
- Search Records: Type in an ID and press SEARCHING BY ID. Linear Search algorithm is applied to locate the student and show his/her complete information in a message box.
- Sorting Algorithms: Click "SORTING ALL" to start a Bubble Sort algorithm. This will rank the students in ascending order of average performance and show the final leaderboard in a special results window.
- Clearing the Form: To clean the entire form in a single button click, use RESET to wipe out all the input fields and put the system focus back on the ID input with the next student. 

App Elements:
- Fields: High-contrast student ID, Name and Subject Grades input boxes.
- Action Buttons: Different colors of buttons used to add data, clear fields and see charts respectively.
- Message Pop-ups: Real-time message feedback to sort results, success confirmation and error messages.
- System Status: Status information at the bottom that gives the user instant feedback.

Libraries Used:
- Tkinter: This is the standard GUI, which is used to construct the window, grid layout and dialog boxes.
- Matplotlib: This is used to create quality bar charts to visualize performance.

Project Structure:
Final-Project/
├── python main.py   # Main entry point containing GUI and Logic
├── README.md        #Project Documentation 
├── requirements.txt #External Libraries 
└── student_data.txt #Local text student database

Testing:
Include test scenarios covering:
- Valid Cases: Testing the standard data entry (IDs, names and scores 0-100) to make sure the dictionary and text file update properly.
- Invalid Cases: Empty field testing, non-numeric characters in grade boxes, searching for non-existent IDs.
- Edge/Boundary Cases: Scores of 0 and 100, and trying to overwrite existing IDs.

Example:
- Successful Logic: When using a valid ID (e.g. P1000) and valid grades, this will display a Success message and refresh the leaderboard.
- Crash Prevention: Typing letters (e.g. "Five") into a grade box will result in an "Input Error" message instead of crashing the program.
- Boundary Accuracy: The program is able to compute the average properly and it shows a performance chart in cases where a student has a score of 100 as the maximum score or at least 0 as the minimum score.
- Data Integrity: In case of an attempt to add an ID that is already present, a program stops and requests permission through a confirmation dialog before modifying any data.
- Search/Sort Reliability: When clicking on the SORTING ALL button, correct clicking creates a ranked list in a new window even when the data has recently been loaded into a preexisting file.

References:

www.w3schools.com. (n.d.). Python - Access Dictionary Items. [online] Available at: https://www.w3schools.com/python/python_dictionaries_access.asp.

W3Schools (2019). Python File Write. [online] W3schools.com. Available at: https://www.w3schools.com/python/python_file_write.asp.

W3Schools (n.d.). Python String strip() Method. [online] www.w3schools.com. Available at: https://www.w3schools.com/python/ref_string_strip.asp.

GeeksforGeeks (2020). How to Index and Slice Strings in Python? [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/how-to-index-and-slice-strings-in-python/.

GeeksforGeeks (2019). Multiple Exception Handling in Python. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/multiple-exception-handling-in-python/.

GeeksforGeeks (2024). Searching Algorithms in Python. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/dsa/searching-algorithms-in-python/.

GeeksforGeeks (2014). Bubble Sort Python. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/python-program-for-bubble-sort/.

www.w3schools.com. (n.d.). Python - Loop Dictionaries. [online] Available at: https://www.w3schools.com/python/python_dictionaries_loop.asp.

GeeksforGeeks (2020). Python Tkinter MessageBox Widget. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/python-tkinter-messagebox-widget/.

Python Tutorial - Master Python Programming For Beginners from Scratch. (n.d.). How to Show a Confirmation Dialog Using the Tkinter askyesno Function. [online] Available at: https://www.pythontutorial.net/tkinter/tkinter-askyesno/.

GeeksforGeeks (2020). Python any() function. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/python-any-function/.

GeeksforGeeks (2024). How to Clear the Entry Widget After Button Press in Tkinter. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/how-to-clear-the-entry-widget-after-button-press-in-tkinter/.

GeeksforGeeks (2017). Python Tkinter. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/python-gui-tkinter/.

GeeksforGeeks (2020). Python Tkinter Entry Widget. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/python-tkinter-entry-widget/.

GeeksforGeeks (2019). Python | grid() method in Tkinter. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/python-grid-method-in-tkinter/.

GeeksforGeeks (2019). Python Tkinter Create Button Widget. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/python-creating-a-button-in-tkinter/.

GeeksforGeeks (2019). Setting and Retrieving values of Tkinter variable Python. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/python-setting-and-retrieving-values-of-tkinter-variable/.

GeeksforGeeks (2020). Python Tkinter Label. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/python-tkinter-label/.