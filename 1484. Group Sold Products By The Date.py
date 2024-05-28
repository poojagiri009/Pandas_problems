import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    mydict = {}
    for i in range(len(activities)):
        sd = activities['sell_date'][i]
        prod = activities['product'][i]
        if sd not in mydict:
            mydict[sd] = set()
        mydict[sd].add(prod)
    result = []
    for key,value in mydict.items():
        temp = []
        for prod in value:
            temp.append(prod)
        temp.sort()
        s=""
        for i in range(len(temp)):
            s = s + temp[i]
            if i != len(temp)-1:
                s=s+','
        result.append([key,len(value),s])
    return pd.DataFrame(result,columns=['sell_date','num_sold','products']).sort_values(by='sell_date')






    #Using pandas
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.groupby('sell_date')
    result = df.agg(
        num_sold = ('product','nunique'),
        products = ('product',lambda x: ','.join(sorted(set(x))))
    ).reset_index()
    result.sort_values(by='sell_date',inplace=True)
    return result






        