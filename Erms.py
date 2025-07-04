import mysql.connector
from tabulate import tabulate
from dotenv import load_dotenv
import os

# Connect to MySQL
load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("host"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database")
)
cursor = conn.cursor()

def add_employee():
    global cursor, conn
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    email = input("Enter Email: ")

    query = "INSERT INTO employees (name, department, salary, email) VALUES (%s, %s, %s, %s)"
    values = (name, dept, salary, email)
    cursor.execute(query, values)
    conn.commit()
    print("Employee added successfully!")

def view_employees():
    global cursor, conn
    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()
    print(tabulate(records, headers=["ID", "Name", "Department", "Salary", "Email"], tablefmt="psql"))

def update_employee():
    global cursor, conn
    emp_id = int(input("Enter Employee ID to update: "))
    name = input("New Name: ")
    dept = input("New Department: ")
    salary = float(input("New Salary: "))
    email = input("New Email: ")

    query = "UPDATE employees SET name=%s, department=%s, salary=%s, email=%s WHERE emp_id=%s"
    cursor.execute(query, (name, dept, salary, email, emp_id))
    conn.commit()
    print("Employee updated successfully!")

def delete_employee():
    global cursor, conn
    emp_id = int(input("Enter Employee ID to delete: "))
    query = "DELETE FROM employees WHERE emp_id = %s"
    cursor.execute(query, (emp_id,))
    conn.commit()
    print("Employee deleted successfully!")

def search_employee():
    global cursor, conn
    emp_id = int(input("Enter Employee ID to search: "))
    query = "SELECT * FROM employees WHERE emp_id = %s"
    cursor.execute(query, (emp_id,))
    record = cursor.fetchone()
    if record:
        print(tabulate([record], headers=["ID", "Name", "Department", "Salary", "Email"], tablefmt="grid"))
    else:
        print("Employee not found.")

def menu():
    while True:
        print("\n Employee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employee")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            search_employee()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

menu()
cursor.close()
conn.close()