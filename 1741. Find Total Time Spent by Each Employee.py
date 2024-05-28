import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['timeout'] = employees['out_time'] - employees['in_time']
    df = employees.groupby(['emp_id','event_day'])['timeout'].sum().reset_index()
    print(df)
    return df[['event_day','emp_id','timeout']].rename(columns={'event_day':'day','timeout':'total_time'})



    

 #another way
 import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    dictionary = {}
    for i in range(len(employees)):
        e_id=employees['emp_id'][i]
        e_date = employees['event_day'][i]
        intime = employees['in_time'][i]
        outtime = employees['out_time'][i]
        if (e_date,e_id) in dictionary:
            dictionary[(e_date,e_id)]+= outtime-intime # adding to existing diff
        else:
            dictionary[(e_date,e_id)]= outtime-intime
    result=[]
    for (key,value) in dictionary.items():
        result.append([key[0],key[1],value])
    return pd.DataFrame(result,columns=['day','emp_id','total_time'])
