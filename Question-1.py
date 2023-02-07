#Importing the necessary modules
from datetime import date
import csv  
import sys
import pandas as pd

#Creating the class employee
class Employee:
  #Class variables
  salary=10000
  total_emp=0
  designation=1

  #Instantiating the necessary fiels with the values of the input given by user
  def __init__(self,name,gender,dob,dof_join):
   
    self.name=name
    self.gender=gender
    self.dob=dob
    self.dof_join=dof_join
    self.hobbies=[]
    self.total_emp+=1
    self.d={}
    self.d["Name"]=self.name
    self.d["Gender"]=self.gender
    self.d['Salary']=self.salary
    self.d["DOB"]=self.dob
    self.d["Date of Joining"]=self.dof_join
    self.d["Designation"]=self.designation
        
    #Procedure for calculating the number of months worked by employee in the company till joining data
    Date,month,year=self.dof_join.split("/")
    form=date(int(year),int(month),int(Date))
    today = date.today()
    self.Number_Of_Months_Worked=(today.year - form.year)* 12 + today.month - form.month

   
    #Procedure for formatting he date of birth of the employee in dd-mmm-yyyy form
    Date,month,year=self.dof_join.split("/")
    form=date(int(year),int(month),int(Date))
    self.temp_dob=form.strftime("%d/%b/%Y")

  
    
 #Checking if the age entered by user is within specified range or not
  def validateAge(self):
    # try:
      
      dd,mm,yyyy=self.dob.split("/")
      dt=date(int(yyyy),int(mm),int(dd))
      today = date.today()
      age = today.year - dt.year -((today.month, today.day) <(dt.month, dt.day))
      if age>=25 and age<=65:
        self.d["Age"]=age
        return age
      else:
        return "Not a valid Age!"

    # except:
    
 #Updating employee details using keyword arguments and a dictionary where in we have stored all the values regarding to a particular employeee
  def update_emp_details(self,**kwargs):
    if 'Name' in kwargs:
      self.d['Name']=kwargs['Name']
    elif 'Gender' in kwargs:
      self.d['Gender']=kwargs['Gender']

    elif 'age' in kwargs:
      self.d['Age']=kwargs['Age']
    else:
      return 'sorry cant be updated'
    
  #Method for promoting the employee
  def promote_employee(self,inc_value=10,design_prom=1):
      self.salary=self.salary+self.salary*(inc_value*0.01)
      self.designation=design_prom

      self.d["Salary"]+=self.d["Salary"]*(inc_value*0.01)
      self.d['Designation']=design_prom

  #Method for demoting the employee
  def demote_employee(self,dec_value=10,design_dem=1):
      self.salary=self.salary-self.salary*(dec_value*0.01)
      self.designation=design_dem

      self.d["Salary"]-=self.d["Salary"]*(dec_value*0.01)
      self.d['Designation']=design_dem
    

  #Adding the hobbies of the user 
  def add_hobbies(self,new_hobbies):
    
    if type(new_hobbies)==type([]):
      self.hobbies.extend(new_hobbies)#Extending the hobbies list if user already has some list of values
      self.d['hobbies']=new_hobbies

    else:
      self.hobbies.append(new_hobbies)#Appending the hobbies list to the list of hobbies
      self.d['hobbies']=new_hobbies

    
  #Displaying employee details 
  def display_emp_details(self):
    print(f"Employee_num:{self.total_emp}")
    print(f"Employee  Name:{self.name}")
    print(f"Employee Gender: {self.gender}")
    print(f"Designation: {self.designation}")
    print(f"Employee Hobbies: {self.hobbies}")
    print(f"Date of birth {self.dob}")
    print(f"Date of Joining : {self.dof_join}")
  


  def remove_hobbies(self,hobby):
    if type(self.hobbies)==type([]):
      self.hobbies.remove(hobby)
    else:
      self.hobbies.pop()
      print("No hobbies inserted")


  #Getting the employees experience in months and years from the months spent till date of joining
  def get_emp_experience(self,name):
     df = pd.read_csv('employees.csv')[lambda x: x['Name']==name]
     years=int(df["Number_Of_Months_Worked"])//12
     months=int(df["Number_Of_Months_Worked"])%12
     print(f'Employees experience is {years} years and {months} months')
  
  #Saving the employee details
  def save_emp_details(self):

    #While we are creating the file it will be in write mode but when we will insert further recoeds it will be in append mode
    header=['Name','Gender','Date_Of_Birth','Number_Of_Months_Worked','Salary', 'Designation', 'Hobbies']

   
    data = [self.name,self.gender,self.temp_dob,self.Number_Of_Months_Worked,self.salary,self.designation,self.hobbies]
    with open('employees.csv', 'w', encoding='UTF8') as f:
       writer = csv.writer(f)

      # write the header
       writer.writerow(header)

      # write the data
       writer.writerow(data)


  #Method will give the count of Total number of employess in the company
  def total_emp1(self):
   
      results = pd.read_csv('employees.csv')
      return len(results)




if __name__=="__main__":

  name=input("Enter employee's name")
  gender=input("Enter your gender (F/M)")
  dob=input("Enter your date of birth in mm/dd/yyy ::")
  d_of_join=input("Enter your date of joining mm/dd/yyy ::")
  e1=Employee(name,gender,dob,d_of_join)

  e1.add_hobbies(['Playing'])
  e1.save_emp_details()
  e1.get_emp_experience(name)
  # e1.validateAge()
  # e1.total_emp1()

  # e1.promote_employee()

  print("<===========Employee Details===========>")
  e1.display_emp_details()
