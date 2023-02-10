import os
import sys

import re
from math import floor

from dateutil import relativedelta
from datetime import datetime, date


class Employee():
    # Specified date format
    __date_format__ = '%d/%m/%Y'

    # Regular expression string format to check if string contain only alphabets and spaces or not.
    # Used to verify name and hobbies.
    __re_check_format__ = r'[a-zA-Z\s]+$'

    # file name used to save employee details
    __file_name__ = 'emp_details.csv'

    def __init__(self, name, gender, dob, doj, hobbies):

        self.name = name
        self.gender = gender
        self.dob = dob
        self.doj = doj
        self.hobbies = hobbies
        self.salary = 10000.0
        self.designation = 'L1'
        self.age = 0

        self.__check_input__()

    def __check_input__(self):
        incorrect_input = []

        # Check name
        if not bool(re.match(self.__re_check_format__, self.name)):
            incorrect_input.append('name')

        # Check gender
        if self.gender.isalpha() and self.gender.lower() in ['female', 'f', 'male', 'm']:
            self.gender = self.gender[0].upper()
        if self.gender not in ['F', 'M']:
            incorrect_input.append('gender')

        # Check format for date of birth (dob) i.e. DD/MM/YYYY or not
        # If correct, convert to datetime format
        try:
            self.dob = datetime.strptime(self.dob, self.__date_format__).date()
        except:
            incorrect_input.append('dob')

        # Check format for date of joining (doj) i.e. DD/MM/YYYY or not
        # If correct, convert to datetime format
        try:
            doj_date_obj = datetime.strptime(self.doj, self.__date_format__).date()
            if (date.today() - doj_date_obj).days >= 0:
                self.doj = doj_date_obj
            else:
                incorrect_input('doj')
        except:
            incorrect_input.append('doj')

        # Check hobbies
        # Should contain (alphabets and spaces only) or can be empty.
        if len(self.hobbies) != 0:
            for hobbie in self.hobbies:
                if not bool(re.match(self.__re_check_format__, hobbie)):
                    incorrect_input.append('hobbies')
                    break

        if len(incorrect_input) != 0:
            print('\nIncorrect input in the following:')
            for idx, error in enumerate(incorrect_input):
                print('\t' + str(idx + 1) + '. ' + error)

            sys.exit()

        else:
            # Caclulate age
            self.age = self.__calculate_age__(self.dob)

            # Check if age is in valid range or not
            if self.age not in range(25, 66):
                print('Age not in the given range.')
                sys.exit()
            else:
                print('Object created successfully.')

    def __str__(self):
        return f"Employee details:\n\
                     1. Name: {self.name}\n\
                     2. Gender: {self.gender}\n\
                     3. Date of birth (DOB): {self.dob.strftime(self.__date_format__)}\n\
                     4. Age: {self.age}\n\
                     5. Date of joining (DOJ): {self.doj.strftime(self.__date_format__)}\n\
                     6. Hobbies: {', '.join(self.hobbies)}\n\
                     7. Salary: {self.salary}\n\
                     8. Designation: {self.designation}"

    def display_emp_details(self):
        print(self)

    def __calculate_age__(self, dob):
        today_date = date.today()

        # rough age will be current_year - dob_year
        age = today_date.year - dob.year

        # If in current year, dob (date,month) is passed i.e. birthday has passed in current year, 
        # then substract 1 else nothing has to be done
        if (today_date.month, today_date.day) < (dob.month, dob.day):
            age -= 1

        return age

    def update_emp_details(self, name='', gender='', dob=''):

        # Update name
        # If valid then update else don't
        if len(name) != 0:
            if not bool(re.match(self.__re_check_format__, name)):
                print("Invalid name input.")
            else:
                self.name = name
                print('Name updated.')

        # Update gender
        # If valid then update else don't
        if len(gender) != 0:
            if gender.isalpha() and gender.lower() in ['female', 'f', 'male', 'm']:
                gender = gender[0].upper()
            if gender not in ['F', 'M']:
                print('Invalid gender input.')
            else:
                self.gender = gender
                print('Gender updated.')

        # Update age (dob)
        # Check format for date of birth (dob) i.e. it is in DD/MM/YYYY or not
        # If correct, then update else don't
        if len(dob) != 0:
            try:
                dob = datetime.strptime(dob, self.__date_format__).date()
                # Caclulate age
                age = self.__calculate_age__(dob)

                # Check if age is in valid range or not
                if age not in range(25, 66):
                    print('Age not in the given range.')
                else:
                    self.age = age
                    print('Age updated.')

            except:
                print("Invalid dob input")

    def promote_emp(self, increment=10, level=1):

        # Check inputs
        if type(increment) == int and type(level) == int:
            print(f'Old salary: {self.salary}')
            self.salary = round((self.salary + (self.salary * (increment / 100))), 4)
            print(f'Updated salary: {self.salary}')

            print(f'\nOld designation: {self.designation}')
            old_level = int(self.designation[1:])
            self.designation = 'L' + str(old_level + level)
            print(f'Updated designation: {self.designation}')

        else:
            print("Invalid parameter input.")

    def demote_emp(self, decrement=10, level=1):

        # Check inputs
        if type(decrement) == int and type(level) == int:
            print(f'Old salary: {self.salary}')
            updated_salary = round((self.salary - (self.salary * (decrement / 100))), 4)

            # If salary is negative or zero, set it to 1 for updation
            if updated_salary <= 1.0:
                self.salary = 1.0
            else:
                self.salary = updated_salary
            print(f'Updated salary: {self.salary}')

            print(f'\nOld designation: {self.designation}')
            old_level = int(self.designation[1:])
            if old_level > 1:
                self.designation = 'L' + str(old_level - level)
            print(f'Updated designation: {self.designation}')


        else:
            print("Invalid parameter input.")

    def save_emp_details(self):

        # Caclulate emp_exp using dateutil module
        emp_exp_months = relativedelta.relativedelta(date.today(), self.doj)
        emp_exp_months = emp_exp_months.months + (emp_exp_months.years * 12)

        # Create string of hobbies from list to store in csv file
        hobbies_data = ' '.join(self.hobbies)

        # Check if csv file present or not
        # If not, then create file with specified headers
        if not os.path.exists(self.__file_name__):
            with open(self.__file_name__, 'w') as fp:
                fp.write('name,gender,dob,experience_(months),salary,designation,hobbies\n')

        # Write data to file
        with open(self.__file_name__, 'a+') as fp:
            fp.write(
                f'{self.name},{self.gender},{str(self.dob.strftime(self.__date_format__))},{emp_exp_months},{self.salary},{self.designation},{hobbies_data}\n')

    def add_hobbies(self, new_hobbies=''):

        if len(new_hobbies) != 0:
            if type(new_hobbies) == str:
                self.hobbies.append(new_hobbies)
            if type(new_hobbies) == list:
                self.hobbies.extend(new_hobbies)
            # to filter any duplicate hobbies
            self.hobbies = list(set(self.hobbies))

    def remove_hobbies(self, del_hobbies=''):
        if len(del_hobbies) != 0 and len(self.hobbies) != 0:
            if type(del_hobbies) == str:
                if del_hobbies in self.hobbies:
                    self.hobbies.remove(del_hobbies)
            if type(del_hobbies) == list:
                self.hobbies = list(set(self.hobbies) - set(del_hobbies))

    def emp_count(self):

        # Check if csv file exist or not
        if not os.path.exists(self.__file_name__):
            print(f"{self.__file_name__} does not exist.")
        else:
            with open(self.__file_name__, 'r') as fp:
                emp_data = fp.readlines()

            # There could be duplicate entries, so using set to filter result
            # substracting 1 to remove header count
            total_entries = len(emp_data) - 1
            unique_entries = len(set(emp_data)) - 1

            print(f"Total entries in csv file: {total_entries}")
            print(f"Unique entries in csv file: {unique_entries}")
            # return total_entries, unique_entries

    def get_emp_experience(self, emp_name=''):

        # check if the emp name is valid and csv file exist
        if len(emp_name) != 0 and bool(re.match(self.__re_check_format__, emp_name)) and os.path.exists(
                self.__file_name__):

            with open(self.__file_name__, 'r') as fp:
                emp_data = fp.readlines()

            # emp data from csv files without header
            emp_data = list(set(emp_data[1:]))

            # Try and except to counter error if given emp details not present in csv file
            try:
                for entry in emp_data:
                    data = entry[:-1].split(',')
                    if emp_name in data:
                        emp_exp_months = int(data[3])

                        # Calculate years and months from tolal experience in months
                        if emp_exp_months / 12 > 1.0:
                            exp_year = floor(emp_exp_months / 12)
                            exp_month = emp_exp_months % 12
                        else:
                            exp_year = 0
                            exp_month = emp_exp_months % 12
                    break

                print(f"Experience of {emp_name}: {exp_year} year {exp_month} month")
            except:
                print(f'No info found for {emp_name}')

        else:
            print('Error.\n Possible cause: invalid emp_name or emp_details.csv does not exist.')


name = input('Enter name: ')
gender = input('Enter gender: ')
dob = input('Enter date of birth [DD/MM/YYYY]: ')
doj = input('Enter date of joining [DD/MM/YYYY]: ')
hobbies = input('Enter hobbies [space seperated ex: h1 h2]: ')

hobbies = hobbies.split(' ')

emp_obj = Employee(name, gender, dob, doj, hobbies)
# emp_obj = Employee('Rekha', 'female', '31/01/1998', '07/02/2023', ['dance'])

# emp_obj.display_emp_details()
# emp_obj.update_emp_details()

