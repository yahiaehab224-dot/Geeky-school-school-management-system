import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("School System")
window.geometry("800x700")
window.configure(bg="#eef2f7")
students = []
def add_student():
    name = name_entry.get()
    grade = grade_entry.get()
    if name and grade:
        students.append(f"{name} - Grade {grade}")
        sort_students()
        name_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
def sort_students():
    students.sort(key=lambda x: int(x.split("Grade ")[1]))
    listbox.delete(0, tk.END)
    for student in students:
        listbox.insert(tk.END, student)
def delete_student():
    selected = listbox.curselection()

    if selected:
        students.pop(selected[0])
        listbox.delete(selected[0])

def delete_all():
    students.clear()
    listbox.delete(0, tk.END)

def edit_student():
    selected = listbox.curselection()

    if selected:
        student = students[selected[0]]
        name, grade = student.split(" - Grade ")

        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)

        grade_entry.delete(0, tk.END)
        grade_entry.insert(0, grade)

        students.pop(selected[0])
        listbox.delete(selected[0])
def search_student():
    name = name_entry.get().lower()
    grade = grade_entry.get()

    listbox.delete(0, tk.END)

    for student in students:
        student_name, student_grade = student.split(" - Grade ")

        if name in student_name.lower() and (not grade or grade == student_grade):
            listbox.insert(tk.END, student)
def save_students():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(student + "\n")

    messagebox.showinfo("Saved", "Students saved!")

def show_saved_students():
    try:
        with open("students.txt", "r") as file:
            saved_students = file.readlines()

        listbox.delete(0, tk.END)
        for student in saved_students:
            listbox.insert(tk.END, student.strip())
    except FileNotFoundError:
        messagebox.showerror("Error", "No saved students found.")
tk.Label(
    window,
    text="🏫 School System",
    font=("Arial", 24, "bold"),
    bg="#263a5b",
    fg="white",
    pady=15
).pack(fill="x")


frame = tk.Frame(window, bg="white", padx=20, pady=15)
frame.pack(pady=20)

tk.Label(frame, text="Student Name", bg="white",
         font=("Arial", 11, "bold")).grid(row=0, column=0)

tk.Label(frame, text="Grade", bg="white",
         font=("Arial", 11, "bold")).grid(row=0, column=1)

name_entry = tk.Entry(frame, width=25, font=("Arial", 11))
name_entry.grid(row=1, column=0, padx=10)

grade_entry = tk.Entry(frame, width=10, font=("Arial", 11))
grade_entry.grid(row=1, column=1, padx=10)


buttons = tk.Frame(window, bg="#eef2f7")
buttons.pack(pady=5)

tk.Button(
    buttons,
    text="＋ Add Student",
    font=("Arial", 10, "bold"),
    bg="#27ae60",
    fg="white",
    width=18,
    height=2,
    command=add_student
).grid(row=0, column=0, padx=5, pady=5)

tk.Button(
    buttons,
    text="✏ Edit Student",
    font=("Arial", 10, "bold"),
    bg="#3498db",
    fg="white",
    width=18,
    height=2,
    command=edit_student
).grid(row=0, column=1, padx=5, pady=5)

tk.Button(
    buttons,
    text="🔍 Search Student",
    font=("Arial", 10, "bold"),
    bg="#8e44ad",
    fg="white",
    width=18,
    height=2,
    command=search_student
).grid(row=0, column=2, padx=5, pady=5)

tk.Button(
    buttons,
    text="🗑 Delete Student",
    font=("Arial", 10, "bold"),
    bg="#e74c3c",
    fg="white",
    width=18,
    height=2,
    command=delete_student
).grid(row=1, column=0, padx=5, pady=5)

tk.Button(
    buttons,
    text="🗑 Delete All",
    font=("Arial", 10, "bold"),
    bg="#c0392b",
    fg="white",
    width=18,
    height=2,
    command=delete_all
).grid(row=1, column=1, padx=5, pady=5)

tk.Button(
    buttons,
    text="💾 Save Students",
    font=("Arial", 10, "bold"),
    bg="#34495e",
    fg="white",
    width=18,
    height=2,
    command=save_students
).grid(row=1, column=2, padx=5, pady=5)

tk.Button(
    buttons,
    text="📂 Show Saved Students",
    font=("Arial", 10, "bold"),
    bg="#9b59b6",
    fg="white",
    width=18,
    height=2,
    command=show_saved_students
).grid(row=2, column=0, padx=5, pady=5)

tk.Label(
    window,
    text="Students",
    font=("Arial", 16, "bold"),
    bg="#eef2f7",
    fg="#263a5b"
).pack(pady=10)

listbox = tk.Listbox(
    window,
    width=45,
    height=9,
    font=("Arial", 12),
    bd=0
)
listbox.pack()

window.mainloop()