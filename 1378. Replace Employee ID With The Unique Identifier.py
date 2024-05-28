#Using pandas
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employee_uni,on='id',how='left')
    return df[['unique_id','name']]



#Another way
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    mydict={}
    for i in range(len(employee_uni)):
        # id = employee_uni['id'][i]
        # unique_id=employee_uni['unique_id'][i]
        mydict[employee_uni['id'][i]] = employee_uni['unique_id'][i]
    result=[]
    for i in range(len(employees)):
        eid = employees['id'][i]
        name=employees['name'][i]
        uid=np.NaN
        if eid in mydict:
            uid = mydict[eid]
        result.append([uid,name])
    return pd.DataFrame(result,columns=['unique_id','name'])