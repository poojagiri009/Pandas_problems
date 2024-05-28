import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    exam_dict={}
    student_dict={}
    for i in range(len(students)):
        s_id=students['student_id'][i]
        s_name = students['student_name'][i]
        student_dict[s_id] = s_name
    for i in range(len(examinations)):
        s_id=examinations['student_id'][i]
        sb_name = examinations['subject_name'][i]
        if (s_id,sb_name) not in exam_dict:
            exam_dict[(s_id,sb_name)] = 0
        exam_dict[(s_id,sb_name)] += 1 #else
    subs = [] #we can iterate over df directly
    for i in range(len(subjects)):
        subs.append(subjects['subject_name'][i])
    result=[]
    for key,value in student_dict.items():
        for i in range(len(subs)):
            cnt = 0
            if (key,subs[i]) in exam_dict:
                cnt = exam_dict[(key,subs[i])]
            result.append([key,value,subs[i],cnt])
    return pd.DataFrame(result,columns=['student_id','student_name','subject_name','attended_exams']).sort_values(by=['student_id','subject_name'])
    

    #Using pandas
    import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = examinations.groupby(by=(['student_id','subject_name'])).size().reset_index(name='attended_exams')
    df1 = subjects.merge(students,how='cross').merge(df,on=('student_id','subject_name'),how='left').sort_values(by=['student_id','subject_name'])
    df1['attended_exams'] = df1['attended_exams'].fillna(0).astype(int)
    return df1[['student_id','student_name','subject_name','attended_exams']]