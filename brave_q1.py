from datetime import datetime
from datetime import date
import sys
import csv


todays_date = date.today()

class Employee:
    all_employ = []
    count_of_employ = 0
    employee_dict = {}
    
    def __init__(self,name,gender,date_of_birth,date_of_joining,hobbies=[]):
        self.name = name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.salary = 10000
        self.designation = "L1"
        
        
        #checking for valid age
        
        def calculate_age(date_of_birth):
            date_of_birth = date_of_birth.split("/")
            res = [eval(i) for i in date_of_birth]
            self.age = todays_date.year - res[2] - ((todays_date.month, todays_date.day) < (res[1], res[0]))
            return self.age
        
        
        #calling the check-age function
        
        calculate_age(date_of_birth)
        if self.age < 25 or self.age > 65:
            sys.exit("Object creation not possible due to unvalid age")
        else:
            pass
        self.date_of_joining = date_of_joining
        self.hobbies = hobbies
        
        #calculating number of months
        
        def number_of_month_worked():
        
            date_of_joining = self.date_of_joining.split("/")
            res = [eval(i) for i in date_of_joining]
            years_worked = abs(todays_date.year - res[2])
            months_worked = abs(todays_date.month - res[1])
            total_months = years_worked + months_worked
            return total_months
        
        Employee.all_employ.append([self.name,self.gender,self.date_of_birth,number_of_month_worked(),self.salary,self.designation,self.hobbies]) 
        
        
        #checking date-format
        
        try:
            dateObjectdob = datetime.strptime(date_of_birth,'%d/%m/%Y')
        except ValueError:
            raise Exception("Date format should be: DD/MM/YYYY")
        try:
            dateObjectdoj = datetime.strptime(date_of_joining,'%d/%m/%Y')
        except ValueError:
            raise Exception("Date format should be: DD/MM/YYYY")
        Employee.count_of_employ = Employee.count_of_employ + 1
        Employee.employee_dict[self.name] = self.date_of_joining
        
        
    def display_employee_details(self):
        
        print("Employee Detials:")
        print(f"The Name of the Employee is: {self.name}")
        print(f"The Gender of the Employee is: {self.gender}")
        print(f"The age of the Employee is: {self.age}")
        print(f"Employee's date of joining was:{self.date_of_joining}")
        print(f"Employee's hobbies are:{self.hobbies}")
        print(f"Salary of the Employee is:{self.salary}")
        print(f"Employee's Designation: {self.designation}")
        
    
    def update_employee_details(self,name=None,age=None,gender=None):
        #checks if the name is updated or not
        if name == None:
            pass
        else: self.name = name
            
        #checks if the age is updated or not    
        if age == None:
            pass
        else: self.age = age
        
        #checks if the gender is updated or not
        if gender == None:
            pass
        else: self.gender = gender
    
    def promote_employee(self,increment_by_perc=10,increment_by_level=1):
        
        #updating salary and level as required
        
        self.salary += self.salary*increment_by_perc/100
        self.designation = 'L' + str(int(self.designation[1]) + increment_by_level)
    
    def demote_employee(self,decrement_by_perc=10,decrement_by_level=1):
        
        #updating salary and level as required
        
        self.salary -= self.salary*decrement_by_perc/100
        self.designation = 'L' + str(int(self.designation[1]) - decrement_by_level)
        
    def number_of_months_worked(self):
        
        date_of_joining = self.date_of_joining.split("/")
        res = [eval(i) for i in date_of_joining]
        years_worked = abs(todays_date.year - res[2]) 
        months_worked = abs(todays_date.month - res[1])
        print(f"{months_worked + (years_worked*12) - 1} months")
        
    def save_employee_details(self):
        
        with open("mycsvfile.csv","w") as f:
            thewriter = csv.writer(f)
            field_name = ['Name','gender','date_of_birth','number_of_months_worked','salary','designation','hobbies' ]
            
            #passing the list of fieldname
            
            thewriter.writerow(field_name)
            thewriter.writerows(Employee.all_employ)
            
            
    def add_hobbies(self,hobbies):
        
        #checks for the data-type of hobbies as input and then executes accordingly
        
        if type(hobbies) == str:
            self.hobbies.append(hobbies)
        elif type(hobbies) == list:
            self.hobbies.extend(hobbies)
            
            
    def remove_hobbies(self,hobbies):
        
        #checks for the data-type of hobbies as input and then executes accordingly
        
        if type(hobbies) == str:
            self.hobbies.remove(hobbies)
        elif type(hobbies) == list:
            for hobby in hobbies:
                self.hobbies.remove(hobby)
                
                
    def total_num_of_employees():
        print(f"The total number of Employees are: {Employee.count_of_employ}")
        
    
    def number_of_months_worked(self):
        
        date_of_joining = self.date_of_joining.split("/")
        res = [eval(i) for i in date_of_joining]
        years_worked = abs(todays_date.year - res[2])
        months_worked = abs(todays_date.month - res[1])
        total_months = years_worked + months_worked
        
        print(f"{months_worked + (years_worked*12) - 1} months")
        
    
    def get_experience(name):
        
        #accessing the value from the dictionary
        ans = Employee.employee_dict[name]
        ans = ans.split("/")
        res = [eval(i) for i in ans]
        
        years_worked = abs(todays_date.year - res[2])
        months_worked = abs(todays_date.month - res[1])
        print(f"{years_worked} years and {months_worked} months experience")
        
        