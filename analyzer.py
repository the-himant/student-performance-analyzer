import numpy as np
import pandas as pd



SUBJECTS = ['Math','Physics','Chemistry','English']



# =============================
#   SHOW ALL STUDENTS
# =============================

def show_all_student(data):
    return (data)



# =============================
#   SHOW ALL STUDENTS RESULT
# =============================

def show_student_result(data):
    data['Total'] = data[SUBJECTS].sum(axis=1)
    data['Percentage'] = (data['Total'] / 400)*100
    return data



# =================================
#   SHOW MEAN OF EACH SUBJECTS
# =================================

def show_sub_avg(data):
    return (data[SUBJECTS].mean(axis=0))



# =============================
#   SEARCH STUDENT'S DATA
# =============================

def search_user_result(data,student_name):
    if student_name not in data['Name'].values:
        return 'No student found!'
    student_result = data[data['Name']==student_name]
    return student_result



def show_toppers(data):
    toppers = data.nlargest(3,'Percentage')
    return toppers