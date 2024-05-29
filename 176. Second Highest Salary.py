import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee['salary'].rank(method='dense',ascending=False)
    employee = employee.drop_duplicates('rank')
    print(employee)
    if len(employee) < 2:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    else:
        return employee[employee['rank'] == 2][['salary']].rename(columns={'salary':'SecondHighestSalary'})



#another way
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    s = set()
    for i in range(len(employee)):
        sal = employee['salary'][i]
        s.add(sal)
    print(s)
    result=[]
    for salary in s:
        result.append(salary)
    result.sort(reverse=True)
    if 2 > len(result):
        return pd.DataFrame([None],columns=['SecondHighestSalary'])
    return pd.DataFrame([result[1]],columns=['SecondHighestSalary'])



import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(['salary'])
    if len(employee) < 2:
        return pd.DataFrame([None],columns=['SecondHighestSalary'])
    employee = employee.sort_values('salary', ascending=False)
    return (employee[['salary']].head(2).tail(1)).rename(columns={'salary':'SecondHighestSalary'})



#drop id
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(['salary'])
    if len(employee) < 2:
        return pd.DataFrame([None],columns=['SecondHighestSalary'])
    employee = employee.sort_values('salary', ascending=False)
    employee.drop('id',axis=1,inplace=True)
    return (employee.head(2).tail(1)).rename(columns={'salary':'SecondHighestSalary'})


#using unique
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = sorted(employee["salary"].unique(), reverse=True)
    nth = None if len(salaries) < 2 else salaries[1]
    return pd.DataFrame({"SecondHighestSalary": [nth]})