from analyzer import show_all_student,show_student_result,show_sub_avg,search_user_result,show_toppers,pass_fail_statistics,high_low_sub_score,class_stats,student_ranking
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
    marks_data = show_student_result(data)

    while True:
        print(OPTIONS)
        try:
            user_choice = int(input("Enter your choice:- "))
            if validate_input(user_choice,10):
                match user_choice:
                    case 1:
                        # calling the function and printing the output
                        print(show_all_student(data))
                    case 2:
                        # geting the student's name
                        student_name = input("Enter the student name:- ")

                        # calling function and save its output in variable
                        result = search_user_result(marks_data,student_name)

                        # Printing the result
                        print(f'==== Result of {student_name}====')
                        print(result)
                    case 3:
                        # Showing all student total marks and percentage
                        print(marks_data)
                    case 4:
                        # Showing subject wise average
                        print("=====Average Marks of Each Subjects=====")
                        print(show_sub_avg(data))
                    case 5:
                        # Showing first 3 toppers
                        toppers = show_toppers(marks_data)
                        print('==== Toppers =======')
                        print(toppers)
                        
                    case 6:
                        # Pass/Fail Statistics
                        output = pass_fail_statistics(marks_data)
                        print(output)
                    case 7:
                        output = high_low_sub_score(marks_data)
                        print(output)
                    case 8:
                        output = class_stats(marks_data)
                        print(output)
                    case 9:
                        ranking_result = student_ranking(marks_data)
                        print('=== Ranking Result ===')
                        print(ranking_result)
                    case 10:
                        print('Thanks for using our Application :) ')
                        break
            else:
                print('Choose correct service number!')
            time.sleep(1)
        
            is_continue = input('Do you want to continue (Press any key to Continue or N for No):- ')
            if is_continue.lower() == 'n':
                print('Thanks for using our Application :) ')
                break

        except ValueError:
            print("Please use option numbers like( 1 or 2 )")


