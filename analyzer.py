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
    data['Pass/Fail'] = data[SUBJECTS].apply(lambda row: "Pass" if (row >= 40).all() else "Fail",axis=1)
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



def pass_fail_statistics(data):
    passed = (data['Pass/Fail'] == 'Pass').sum()
    failed = (data['Pass/Fail'] == 'Fail').sum()
    total_student = data.shape[0]

    output = f'''
Total Student => {total_student}
Passed        => {passed}
Failed        => {failed}
    '''

    return output




def high_low_sub_score(data):
    result = data[SUBJECTS].agg(['max','min'])
    return (result)



def class_stats(data):
    total = data.shape[0]
    class_avg = data['Percentage'].mean()
    highest_percentage = data['Percentage'].max()
    lowest_percentage = data['Percentage'].min()
    passed = (data['Pass/Fail'] == 'Pass').sum()
    failed = (data['Pass/Fail'] == 'Fail').sum()
    pass_percentage = (passed/total)*100
    fail_percentage = (failed/total)*100
    
    output = f"""
====== CLASS STATSTICS ====
Total Student       : {total}
Class Average       : {class_avg}
Highest Percentage  : {highest_percentage}
Lowest Percentage   : {lowest_percentage}
Pass Percentage     : {pass_percentage}
Fail Percentage     : {fail_percentage}

==== SUBJECT AVERAGE ======
{show_sub_avg(data)}
"""

    return output



def student_ranking(data):
    data = data.sort_values(by='Percentage',ascending=False)
    ranking = pd.DataFrame({
        'Name':data['Name'],
        'Percentage':data['Percentage']
    }).reset_index(names='Student ID')
    return (ranking)