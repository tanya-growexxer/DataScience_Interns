import csv
from datetime import datetime, timedelta
import sys

class Employee:
    
    count_of_employee = 0 #claas globel variable count of employee 
    all_employee_details = [] #class global variable store employee details
    emp_dict ={}
    #create constuctor for employee
    def __init__(self, name, gender, date_of_birth, date_of_joining, hobbies=[]):
        #object creation and variable assign
        self.name = name 
        self.gender = gender
        
        #store birthdate in  DD/MM/YYYY format 
        self.date_of_birth = datetime.strptime(date_of_birth, '%d/%m/%Y')
        #store joining date in  DD/MM/YYYY format 
        self.date_of_joining = datetime.strptime(date_of_joining, '%d/%m/%Y')
        
        self.hobbies = hobbies
        self.salary = 10000 #inisial salary is 10000
        self.designation = 'L1' #by defalut it is L1
        
        #calculate age by days total day - joining day /365 
        self.number_of_months_worked = ((datetime.now().date() - self.date_of_joining.date()).days*12//365)
        
        
        #calculate age by days total day - birth day /365 
        self.age = (datetime.now().date() - self.date_of_birth.date()).days//365
        
        #check age is between 25 yo 65 or not
        if self.age >=25 and self.age <=65:
            #age condition satisfy then employee count will increase
            Employee.count_of_employee += 1   
            Employee.emp_dict[self.name]=self.number_of_months_worked
            #append new employee details to all employee details
            Employee.all_employee_details.append([self.name, self.gender, self.date_of_birth, self.date_of_joining, self.number_of_months_worked,self.hobbies, self.salary, self.designation, self.age])
        else:
            #object will not create and system will be exit
            sys.exit()
            
            
    #create fuction for display employee details
    def display_employee_details(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Date of Birth:", self.date_of_birth.strftime('%d/%m/%Y'))
        print("Date of Joining:", self.date_of_joining.strftime('%d/%m/%Y'))
        print("number of months worked:",self.number_of_months_worked)
        print("Hobbies:", self.hobbies)
        print("Salary:", self.salary)
        print("Designation:", self.designation)
        print("Age:", self.age)
        print()
        
        
    #create fuction for update employee details
    def update_employee_details(self, name=None, gender=None, age=None):
        if name != None:
            self.name = name
        if gender != None:
            self.gender = gender
        if age != None:
            self.age = age
        
        
    #promote employee by default and also by user 
    def promote_employee(self, increment=10, level=1):
        
        #promote employee and update details of salary and designation
        self.salary += self.salary*increment/100
        self.designation = str(int(self.designation[1])+level)
        
        
    #demote employee by default and also by user 
    def demote_employee(self, decrement=10, level=1):
        
        #demote employee and update details of salary and designation
        self.salary -= self.salary*decrement/100
        self.designation = str(int(self.designation[1])-level)
        
     
    #save all employee details in csv file
    def save_employee_details(self):
        headers = ['Name', 'Gender', 'Date of Birth', 'Date of Joining','number of months worked','Hobbies', 'Salary', 'Designation', 'Age']
        with open('employee_details.csv', 'w', newline ='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(Employee.all_employee_details)
    
    
    #add hobbies by user input        
    def add_hobbies(self, input_hobbies):
        
        #check if string input then append 
        if type(input_hobbies) == str:
            self.hobbies.append(input_hobbies)
        
        #else it will extend the list
        elif type(input_hobbies) == list:
            self.hobbies.extend(input_hobbies)
       
    
    #remove hobbies by user input
    def remove_hobbies(self, input_hobbies):
        
        #user input is string then just remove it 
        if type(input_hobbies) == str:
            self.hobbies.remove(input_hobbies)
        
        #otherwise if list then one by one remove
        elif type(input_hobbies) == list:
            
            #iterting hobbies which given by user
            for hobby in input_hobbies:
                
                #cheching hobby is avilaible then remove otherwise pass
                if hobby in self.hobbies:
                    self.hobbies.remove(hobby)
                else:
                    pass
        
        
    #print fuction to print total nnumber of employee
    def display_count_of_employee():
        
        print(f"Total Number Of Employees is {Employee.count_of_employee}")
    
    #experience of imployee
    def get_experience(name):
        number_of_months_worked =Employee.emp_dict[name]
        years = number_of_months_worked//12
        months = (number_of_months_worked) %12
        print("Employee {} has worked for {} years and {} months".format(name, years, months))
    