import csv
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent / "tasks.csv"

print("Python file location:", __file__)
print("CSV file location:", FILE_PATH)
print("Does CSV exist?", FILE_PATH.exists())

class Task:
    def __init__(self, name, course_code, weightage, hours, due_date):
        self.name = name.strip()
        self.course_code = course_code.strip().upper()
        self.weightage = float(weightage)
        self.hours = float(hours)
        self.due_date = due_date.strip()

    def __str__(self):
        return (f"[{self.course_code}] {self.name} | Due: {self.due_date} "
                f"| Weight: {self.weightage:g}/10 | Hours: {self.hours:g}h")


def read_tasks():
    """Read tasks from the CSV file. Each row must have 5 columns."""
    tasks = []

    if not FILE_PATH.exists():
        print(f"\nCSV file not found: {FILE_PATH}")
        print("Create tasks.csv in the same folder as main.py.")
        return tasks

    try:
        with open(FILE_PATH, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.reader(file)

            for row_number, row in enumerate(reader, start=1):
                if not row or all(not value.strip() for value in row):
                    continue

                if len(row) != 5:
                    print(f"Skipping row {row_number}: expected 5 columns, found {len(row)}.")
                    continue

                try:
                    name, course, weight, hours, due = row
                    tasks.append(Task(name, course, weight, hours, due))
                except ValueError:
                    print(f"Skipping row {row_number}: weightage and hours must be numbers.")

    except OSError as error:
        print(f"Could not read the CSV file: {error}")

    return tasks


def save_tasks(tasks):
    """Save all tasks to the CSV file."""
    try:
        with open(FILE_PATH, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for task in tasks:
                writer.writerow([
                    task.name, task.course_code, task.weightage,
                    task.hours, task.due_date
                ])
        return True
    except OSError as error:
        print(f"Could not save the CSV file: {error}")
        return False


def add_task():
    print("\n--- ADD A TASK ---")
    name = input("Task name: ").strip()
    course = input("Course code: ").strip()

    if not name or not course:
        print("Task name and course code cannot be empty.")
        return

    try:
        weight = float(input("Academic weightage (1-10): "))
        hours = float(input("Estimated study hours: "))

        if not 1 <= weight <= 10:
            print("Weightage must be between 1 and 10.")
            return
        if hours <= 0:
            print("Study hours must be greater than zero.")
            return

    except ValueError:
        print("Please enter valid numbers for weightage and hours.")
        return

    due = input("Due date (e.g. Friday or 2026-11-20): ").strip()
    if not due:
        print("Due date cannot be empty.")
        return

    tasks = read_tasks()
    tasks.append(Task(name, course, weight, hours, due))

    if save_tasks(tasks):
        print("Task added successfully!")


def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n--- YOUR STUDY TASKS ---")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def view_tasks():
    tasks = read_tasks()
    tasks.sort(key=lambda task: task.weightage, reverse=True)
    display_tasks(tasks)


def delete_task():
    tasks = read_tasks()
    if not tasks:
        print("\nNo tasks available to delete.")
        return

    # Keep the displayed order and delete only the selected row.
    tasks.sort(key=lambda task: task.weightage, reverse=True)
    display_tasks(tasks)

    try:
        choice = int(input("\nEnter task number to delete: "))
        if not 1 <= choice <= len(tasks):
            print("Invalid task number.")
            return
    except ValueError:
        print("Please enter a whole number.")
        return

    removed = tasks.pop(choice - 1)

    if save_tasks(tasks):
        print(f"Deleted: {removed.name}")


def search_by_course():
    tasks = read_tasks()

    if not tasks:
        print("No tasks available.")
        return

    course = input("Enter course code: ").strip().upper()

    results = [task for task in tasks
               if task.course_code == course]

    if not results:
        print("No tasks found for this course.")
        return

    print(f"\n--- TASKS FOR {course} ---")

    for number, task in enumerate(results, start=1):
        print(f"{number}. {task}")


def show_summary():
    tasks = read_tasks()
    if not tasks:
        print("\nNo tasks available for a summary.")
        return

    total_hours = sum(task.hours for task in tasks)
    print("\n--- STUDY SUMMARY ---")
    print(f"Total tasks: {len(tasks)}")
    print(f"Total estimated study hours: {total_hours:g}")

    course_codes = sorted(set(task.course_code for task in tasks))
    print("\nTasks by course:")
    for course in course_codes:
        count = sum(1 for task in tasks if task.course_code == course)
        print(f"{course}: {count} task(s)")


def main():
    while True:
        print("\n========== SMART STUDY PLANNER ==========")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Search tasks by course")
        print("5. View study summary")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            search_by_course()
        elif choice == "5":
            show_summary()
        elif choice == "6":
            print("Goodbye! Keep studying.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
