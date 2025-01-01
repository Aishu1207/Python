# Employee Management System

class Employee:
    def __init__(self, emp_id, name, age, post, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.post = post
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Post: {self.post}, Salary: {self.salary}"
class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, age, post, salary):
        if emp_id in self.employees:
            print(f"Employee with ID {emp_id} Already Exists.")
        else:
            employee = Employee(emp_id, name, age, post, salary)
            self.employees[emp_id] = employee
            print(f"Employee {name} Added Successfully.")

    def view_employee(self, emp_id):
        if emp_id in self.employees:
            print(self.employees[emp_id])
        else:
            print(f"Employee with ID {emp_id} not found.")

    def update_employee(self, emp_id, name=None, age=None, post=None, salary=None):
        if emp_id in self.employees:
            if name:
                self.employees[emp_id].name = name
            if age:
                self.employees[emp_id].age = age
            if post:
                self.employees[emp_id].post = post
            if salary:
                self.employees[emp_id].salary = salary
            print(f"Employee {emp_id} Updated Successfully.")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print(f"Employee {emp_id} Deleted Successfully.")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def list_employees(self):
        if self.employees:
            for emp_id, employee in self.employees.items():
                print(employee)
        else:
            print("No Employees found.")

def main():
    employee = EmployeeManagementSystem()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. List All Employees")
        print("6. Exit")

        choice = input("Enter your Choice: ")

        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            age = int(input("Enter Employee Age: "))
            post = input("Enter Employee Post: ")
            salary = float(input("Enter Employee Salary: "))
            employee.add_employee(emp_id, name, age, post, salary)

        elif choice == '2':
            emp_id = input("Enter Employee ID: ")
            employee.view_employee(emp_id)

        elif choice == '3':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name : ")
            age = input("Enter Employee Age : ")
            post = input("Enter Employee Post : ")
            salary = input("Enter Employee Salary : ")

            age = int(age) if age else None
            salary = float(salary) if salary else None
            employee.update_employee(emp_id, name, age,post, salary)

        elif choice == '4':
            emp_id = input("Enter Employee ID: ")
            employee.delete_employee(emp_id)

        elif choice == '5':
            employee.list_employees()

        elif choice == '6':
            print("Exit...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
