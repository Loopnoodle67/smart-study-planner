# Smart Study Planner 📚

## 1. Project Overview

Smart Study Planner is a beginner-friendly Python-based academic task management system designed to help students organize and manage their academic workload efficiently.

The application allows students to add, view, delete, and search academic tasks based on course codes. It also provides a study summary displaying the total number of tasks, estimated study hours, and course-wise task distribution.

The project uses CSV file handling to store task information permanently, allowing users to access their saved tasks whenever they run the application.

## 2. Objectives

- Simplify academic task management.
- Help students organize assignments and study activities.
- Prioritize tasks based on academic weightage.
- Maintain task records using CSV file handling.
- Track estimated study hours.
- Provide course-wise task filtering and workload summaries.

## 3. Features

### 1. Add New Task
Users can enter:
- Task name
- Course code
- Academic weightage (1–10)
- Estimated completion hours
- Due date

### 2. View All Tasks
- Displays all saved academic tasks.
- Automatically sorts tasks according to academic weightage, from highest to lowest.

### 3. Delete Task
- Allows users to select and delete a particular task.
- Updates the CSV file after deletion.

### 4. Search Tasks by Course
- Filters tasks using their course codes.
- Displays only tasks belonging to the selected course.

### 5. Study Summary
Displays:
- Total number of tasks.
- Total estimated study hours.
- Number of tasks assigned to each course.

### 6. CSV Data Storage
- Stores task information in `tasks.csv`.
- Retrieves saved records whenever the application runs.
- Maintains data even after the program is closed.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| CSV Module | Reading and writing task records |
| pathlib | Managing file paths |
| Classes and Objects | Representing academic tasks |
| Exception Handling | Managing invalid inputs and file errors |

## 5. Project Structure

```text
Smart-Study-Planner/
│
├── main.py
│
├── tasks.csv
│
└── README.md
```

**main.py:** Contains the main Python program and all task management functions.

**tasks.csv:** Stores academic task records.

**README.md:** Provides project documentation and instructions.

## 6. CSV File Format

The application stores information in the following format:

```csv
Task Name,Course Code,Weightage,Hours,Due Date
Python Lab Assignment,CSE1005,8.0,3.5,Friday
BEEE Circuit Analysis,CSE1001,7.0,4.0,Monday
Calculus Assignment 2,CSE1001,6.5,2.5,Wednesday
```

Each record contains five fields:
1. Task name
2. Course code
3. Academic weightage
4. Estimated study hours
5. Due date

## 7. Installation and Execution

### Prerequisites
- Python 3.x
- Any Python IDE (VS Code, PyCharm, or IDLE)

No external Python libraries are required.

### Steps to Run

1. Download or clone the project.
2. Keep `main.py` and `tasks.csv` in the same folder.
3. Open the project folder in your preferred IDE.
4. Open the terminal.
5. Execute the following command:

```bash
python main.py
```

6. Select the desired option from the displayed menu.

## 8. Python Concepts Implemented

This project demonstrates the practical implementation of:

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Special methods (`__str__`)
- User-defined functions
- Lists and list comprehension
- Conditional statements
- Loops
- File handling
- CSV operations
- Exception handling
- Sorting and searching
- Modules and libraries

## 9. Future Scope

The project can be enhanced by introducing:

- Task completion status (Completed/Pending).
- Automatic deadline reminders.
- Daily study schedule recommendations.
- Study progress tracking.
- Graphical user interface using Tkinter.
- Data visualization using Matplotlib.
- A personalized study recommendation system.

## 10. Conclusion

Smart Study Planner demonstrates how Python programming and file handling can be used to solve a practical student-life problem.

By combining Object-Oriented Programming, CSV storage, and task management functionalities, the project provides a simple and effective solution for organizing academic responsibilities.

The project also serves as a foundation for developing more advanced student productivity and academic planning applications.

---

**Project Name:** Smart Study Planner  
**Category:** Python Mini Project  
**Programming Language:** Python 3  
**Data Storage:** CSV  
**Project Level:** Beginner