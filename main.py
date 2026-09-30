from analyzer import show_all_student,show_student_result
import pandas as pd
import numpy as np
import time

OPTIONS = '''
=======Student Performance Analyzer========
Choose the option number (eg:- 1)
1. Show All Students
2. Search a Student
3. Show Student Result
4. Subject-wise Average
5. Show Topper
6. Pass/Fail Statistics
7. SUbject Highest/Lowest
8. Class Statistics
9. Student Ranking
10. Exit

'''

# getting data 
def load_data():
    PATH_URL = r'data\student.csv'
    df = pd.read_csv(PATH_URL)
    return df

# Validating user_input
def validate_input(user_input, range_upto):
    if 0 < user_input <= 10:
        return True
    else:
        return False


if __name__ == "__main__":
    data = load_data()

    while True:
        print(OPTIONS)
        try:
            user_choice = int(input("Enter your choice:- "))
            if validate_input(user_choice,10):
                match user_choice:
                    case 1:
                        show_all_student(data)
                    case 2:
                        print('User selected option 2')
                    case 3:
                        show_student_result(data)
                    case 4:
                        print('User selected option 4')
                    case 5:
                        print('User selected option 5')
                    case 6:
                        print('User selected option 6')
                    case 7:
                        print('User selected option 7')
                    case 8:
                        print('User selected option 8')
                    case 9:
                        print('User selected option 9')
                    case 10:
                        print('Thanks for using our Application :) ')
                        break
            else:
                print('Choose correct service number!')
            time.sleep(1)
        
            is_continue = input('Do you want to continue (Press any key to Continue or N for No):- ')
            if is_continue.lower() == 'N':
                break

        except ValueError:
            print("Please use option numbers like( 1 or 2 )")


