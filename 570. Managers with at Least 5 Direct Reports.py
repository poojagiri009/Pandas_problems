import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    emp_info = {}
    emp_count = {}
    for i in range(len(employee)):
        eid = employee['id'][i]
        name = employee['name'][i]
        mid = employee['managerId'][i]
        emp_info[eid] = name
        if mid not in emp_count:
            emp_count[mid] = 0
        emp_count[mid]+=1
    result=[]
    for key,value in emp_count.items():
        if value >= 5:
            if key in emp_info:
                result.append(emp_info[key])
    return pd.DataFrame(result,columns=['name'])



#Using pandas groupby
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('managerId').size().reset_index(name='count')
    df = df[df['count'] >= 5]
    result = df.merge(employee,left_on='managerId',right_on='id',how='inner')
    return result[['name']]


#Using pandas isin
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('managerId').size().reset_index(name = 'count')
    df = df[df['count']>=5]
    df = employee[employee['id'].isin(df['managerId'])][['name']]
    return df



    