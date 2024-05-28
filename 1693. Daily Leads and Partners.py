import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df =  daily_sales.groupby(
        ['date_id', 'make_name']
    ).nunique().reset_index()
    return df.rename(columns={'lead_id': 'unique_leads','partner_id': 'unique_partners'})




#Using agg function
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df= daily_sales.groupby(['date_id','make_name']).agg({
        'lead_id' : pd.Series.nunique,
        'partner_id':pd.Series.nunique
    }).reset_index()
    return df.rename(columns={'lead_id':'unique_leads','partner_id':'unique_partners'})





#Using dictionary
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    mydict={}
    for i in range(len(daily_sales)):
        date_id=daily_sales['date_id'][i]
        make_name=daily_sales['make_name'][i]
        lead_id=daily_sales['lead_id'][i]  
        partner_id=daily_sales['partner_id'][i]
        if (date_id,make_name) not in mydict:
            mydict[(date_id,make_name)] = [set(),set()] #set1 is index 0 and set2 is index 1
        mydict[(date_id,make_name)][0].add(lead_id)
        mydict[(date_id,make_name)][1].add(partner_id)
    result=[]
    for key,value in mydict.items():
        result.append([key[0],key[1],len(value[0]),len(value[1])])
    print(result)
    return pd.DataFrame(result,columns=['date_id','make_name','unique_leads','unique_partners'])