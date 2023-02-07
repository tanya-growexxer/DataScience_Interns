class Employee:
  def __init__(self,user_name,gender,hobbies,date_of_birth,date_of_joining,salary=10000,designation="L1"):
    self.user_name=user_name
    self.gender=gender
    self.hobbies=[]
    self.salary=salary
    self.designation=designation
    self.date_of_birth=date_of_birth
    self.date_of_joining=date_of_joining
    if date_of_birth and date_of_joining != "%d-%m-%y":
      date_of_birth.strftime("%d-%m-%y")
      date_of_joining.strftime("%d-%m-%y")
    else:
      return date_of_birth,date_of_joining
    
  def display(self):
      print(self.user_name,self.gender,self.date_of_birth,self.date_of_joining,self.hobbies)
  
  def update_employee_details(self,n,g,a):
    self.name=n
    self.gender=g
    self.age=a
    try:
      if self.age>=25 and self.age<=65:
        return self.age
    except:
      print("not valid age")

  def promote_employee(self,increased_salary):
    self.increased_salary =  salary +((salary*10)%100)

  def demote_employee(self,decreased_salary):
    self.decreased_salary = salary-((salary*10)%100)

  def add_hobbies(self,hobbies):
    if i in hobbies:
      hobbies.append(i)

  def remove_hobbies(self,hobbies):
    for i in hobbies:
      hobbies.remove(i)




em = Employee("akhilesh","male",["games","music"],"02/01/2002","01/03/2021",10000,"L1")
em.display()





