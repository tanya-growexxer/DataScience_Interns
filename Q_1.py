#Importing Libraries
import csv
import pandas as pd
from datetime import date,datetime

#create a class Employee
class Employee:

  #The init function acts as a constructor
  def __init__(self,name,gender,date_of_birth,date_of_joining,hobbies=[]):
    #assigning the values to the local variable
    self.name = name
    self.gender = gender
    self.date_of_birth = date_of_birth
    self.date_of_joining = date_of_joining
    self.hobbies = list(hobbies)
    print(self.hobbies)

    #initialising values
    self.salary = 10000
    self.designation = 1

  #Formate the date calculate age according to that
  def date_format(self):
    today = date.today()
    self.d1 = datetime.strptime(self.date_of_birth,'%d/%m/%Y')
    self.d2 = datetime.strptime(self.date_of_joining,'%d/%m/%Y')
    self.months = (today.year - self.d2.year) * 12 + today.month - self.d2.month
    self.age = today.year - self.d1.year - ((today.month, today.day) < (self.d1.month, self.d1.day)) #
    #print(self.age)
    if self.age >= 25 and self.age <= 65:
      print(self.age)
    else:
      print("Age should be between 25 to 65...")
  
  #To display Employee Details
  def display_employee_details(self):
    print("Employee Details:")
    print(f"Employee name: {self.name} \nAge: {self.age} \nGender: {self.gender} \nDate of Birth: {self.d1.date()} \nDate of Joining: {self.d2.date()} \nSalary: {self.salary} \nDesignation: {self.designation} \nHobbies: {self.hobbies}")
  
  #To Update Details of Employees
  def update_employee_details(self, name = '',gender = '', age = ''):
    if name != '':
      self.name = name
    elif gender != '':
      self.gender = gender
    elif age != '':
      self.date_of_birth = input("Enter your date of birth also(DD/MM/YYYY): ")
      self.date_format()
      if self.age == age:
        pass
      else:
        print("age does not match you date of birth...")
        exit()
    self.display_employee_details()
  
  #For Salary Increament
  def promote_employee(self,inc_salary = 10,level = 1):
    self.salary = self.salary + (self.salary*inc_salary)*0.01
    self.designation += level  

  #For salary Decreament
  def demote_employee(self,dec_salary = 10,level = 1):
    self.salary = self.salary - (self.salary*dec_salary)*0.01
    self.designation -= level 

  #TO save details into file
  def save_employee_file(self):

    header = ['Name','Gender','Date_of_Birth','Number_of_Months', 'Salary', 'Designation','Hobbies']
    data = [self.name,self.gender,self.date_of_birth,str(self.months),str(self.salary),str(self.designation),self.hobbies]

    with open('Employees.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        writer.writerow(data)
  
  # To Add Hobbies
  def add_hobbies(self,add_hobbie):
    if type(add_hobbie) == type([]):
      self.hobbies.extend(add_hobbie)
    else:
      self.hobbies.append(add_hobbie)
    
  
  #To Remove Hobbies
  def remove_hobbies(self,rm_hobby):
    if rm_hobby in self.hobbies:
      self.hobbies.remove(rm_hobby)
    else:
      print("There is no such hobby")

  #Count of Employees
  def count_of_employees(self):
    count_emp = pd.read_csv("Employees.csv")
    return len(count_emp)
  
  #To show Experience of Employees
  def employee_experience(self,rname):
    with open('Employees.csv') as f:
      reader = csv.DictReader(f)
      for i in reader:
        if i['Name'] == rname:
          y = int(i['Number_of_Months']) // 12
          m = int(i['Number_of_Months']) % 12
          break
    print("Experience of {} is : {} Years and {} Months".format(rname,y,m))

if __name__ == "__main__": # Main function to take input from user and call all the functions
  
  name = input("Enter name of Employee: ")
  gender = input("Enter Gender(M/F): ")
  dob = input("Enter your Date of Birth (DD/MM/YYYY): ")
  doj = input("Enter your Date of Joining (DD/MM/YYYY): ")
  hobbies = []
  print("Enter any two Hobbies: ")
  for i in range(0,2):
    a = input()
    hobbies.append(a)

  #creating an object to call all the functions  
  emp = Employee(name,gender,dob,doj,hobbies)
  emp.date_format()