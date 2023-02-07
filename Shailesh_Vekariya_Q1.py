import datetime
from datetime import date
import csv
import dateutil
from dateutil import relativedelta

class Employee:
    date_format='%d/%m/%Y'
    hobbies=[]
    salary=10000
    designation='L1'
    total_employees = 0
    all_employee_details=[]
    
    
    #defining constructor
    def __init__(self,name,gender,date_of_birth,date_of_joining,hobbies,salary,designation):
        
        self.name=name
        self.gender=gender
        self.date_of_birth=date_of_birth
        self.date_of_joining=date_of_joining
        self.hobbies=hobbies
        self.salary=salary
        self.designation=designation
     
    
        #try-except for checking the input(format DD/MM/YYYY) of user for date_of_birth and date_of_joining.
        try:
            dateObjectdob = datetime.datetime.strptime(date_of_birth,Employee.date_format)
        except ValueError:
            print("Incorrect data format, should be DD/MM/YYYY")
        try:
            dateObjectdoj= datetime.datetime.strptime(date_of_joining,Employee.date_format)
        except ValueError:
            print("Incorrect data format, should be DD/MM/YYYY")
        Employee.total_employees +=1
        
        
        #calculating the number_of_months_worked
        self.doj=datetime.datetime.strptime(self.date_of_joining, '%d/%m/%Y')
        self.today=datetime.datetime.now().date()
        self.delta=relativedelta.relativedelta(self.today,self.doj)
        self.number_of_months_worked=self.delta.months + self.delta.years*12
        
        Employee.all_employee_details.append([self.name,self.gender,self.date_of_birth,self.date_of_joining,self.hobbies,self.salary,self.designation,self.number_of_months_worked])

        
    #to get the age of employee using date_of_birth    
    def age(self,date_of_birth):
        #date_of_birth
        self.date_of_birth=date_of_birth
        #today's date
        today = date.today()
        
        d,m,y=date_of_birth.split('/')
        d=int(d)
        m=int(m)
        y=int(y)
        birthdate=date(y,m,d)
        
        # A bool that represents if today's day/month precedes the birth day/month
        one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
        # Calculate the difference in years from the date object's components
        year_difference = today.year - birthdate.year
        # The difference in years is not enough. 
        # To get it right, subtract 1 or 0 based on if today precedes the birthdate's month/day.
        # To do this, subtract the 'one_or_zero' boolean 
        # from 'year_difference'. (This converts True to 1 and False to 0 under the hood.)
        self.age = year_difference - one_or_zero
        if self.age>65 or self.age<25:
            raise Exception("not valid age")
        return self.age
    

    #creating function to get the employee_details
    def employee_details(self):
        print("employee name:",self.name)
        print("employee gender:",self.name)
        print("employee date_of_birth:",self.date_of_birth)
        print("employee date_of_joining:",self.date_of_joining)
        print("hobbies:",self.hobbies)
        print("salary:",self.salary)
        print("designation:",self.designation)
        
    #creating function for updating the employee details like name,gender,age
    #to update the age I will take date_of_birth from user and call age function to update the age
    def update_employee_details(self,**kwargs):
        if 'name' in kwargs:
            self.name=kwargs['name']
        if 'gender' in kwargs:
            self.gender=kwargs['gender']
        if 'date_of_birth' in kwargs:
            self.date_of_birth=kwargs['date_of_birth']
            #after updating the date_of_birth age must be updated
            self.age=self.age(kwargs['date_of_birth'])
            
            
    #creating function for promotion.updating the salary and designation as per the given increment and level.
    def promote_employee(self,increment=10,level=1):
        self.increment=increment
        self.level=level
        #salary after increment
        self.salary=self.salary + increment*self.salary/100
        self.designation=int(self.designation[1])+level
        #designation after promotion
        self.designation='L'+str(self.designation)
        
        
    #creating function for demotion.updating the salary and designation as per the given decrement and level.
    def demote_employee(self,decrement=10,level=1):
        self.decrement=decrement
        self.level=level
        #salary after decrement
        self.salary=self.salary - decrement*self.salary/100
        self.designation=int(self.designation[1])-level
        #designation after demotion
        self.designation="L"+str(self.designation)
        
    #creating the function to save the employee_details in csv file    
    def save_employee_details(self):
    
        header=['Name','gender','date_of_birth','date_of_joining','hobbies','salary','designation','number_of_months_worked']
        with open('employee_details.csv', 'w', newline ='') as file:
            writer = csv.writer(file)
            #writing into header
            writer.writerow(header)
            #adding employee details
            writer.writerows(Employee.all_employee_details)
            
        
    #creating function to add hobbies in the existing hobbies list
    def add_hobbies(self,hobbies_to_be_added):
        self.hobbies_to_be_added=hobbies_to_be_added
        #if the hobbies_to_be_added is of type string append it
        if type(self.hobbies_to_be_added)==type(" "):
            self.hobbies.append(self.hobbies_to_be_added)
        #if the hobbies_to_be_added is of type list use extend
        elif type(self.hobbies_to_be_added)==type([]):
            self.hobbies.extend(hobbies_to_be_added)
            
    #creating the function to remove hobbies from the existing hobbies list
    def remove_hobbies(self,hobbies_to_be_removed):
        self.hobbies_to_be_removed=hobbies_to_be_removed
        if type(self.hobbies_to_be_removed)==type(" "):
            self.hobbies.remove(self.hobbies_to_be_removed)
        if type(self.hobbies_to_be_removed)==type([ ]):
            for i in range(len(self.hobbies_to_be_removed)):
                if self.hobbies_to_be_removed[i] in self.hobbies:
                    self.hobbies.remove(self.hobbies_to_be_removed[i])
                else:
                    pass
                
    #creating a function to get the number of employee            
    def total_employee(self):
        return Employee.total_employees
    
    #creating function to get the experience of employee in year and months
    def get_experience(self,name):
        date_format = "%d/%m/%Y"
        start_date = datetime.datetime.strptime(self.date_of_joining,date_format)
        end_date = datetime.datetime.strptime(datetime.datetime.today().strftime(date_format),date_format)
        delta = end_date - start_date
        years = delta.days // 365
        months = (delta.days % 365) // 30
        return "Employee {} has worked for {} years and {} months".format(name, years,months)
        
    