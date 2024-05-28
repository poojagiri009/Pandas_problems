import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merge1 = orders.merge(company,on='com_id',how='left')[['order_id','sales_id','name']]
    df = merge1[merge1['name'] == 'RED']
    df1 = sales_person[~sales_person['sales_id'].isin(df['sales_id'])]
    return df1[['name']]




#another way
import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    com_id = -1
    for i in range(len(company)):
        name = company['name'][i]
        if name == 'RED':
            com_id = company['com_id'][i]
            break
    empids=set()
    for i in range(len(orders)):
        cid = orders['com_id'][i]
        salesid = orders['sales_id'][i]
        if cid == com_id:
            empids.add(salesid)
    result=[]
    for i in range(len(sales_person)):
        sales_id = sales_person['sales_id'][i]
        name = sales_person['name'][i]
        if sales_id not in empids:
            result.append([name])
    return pd.DataFrame(result,columns=['name'])



    #another way finding unique sales ids
import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.merge(company,on='com_id',how='left')[['order_id','sales_id','name']]
    df = df[df['name'] == 'RED']
    sales_ids = df.sales_id.unique()
    print(sales_ids)
    df1 = sales_person[~sales_person['sales_id'].isin(sales_ids)]
    return df1[['name']]