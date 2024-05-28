import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['rnk'] = activity.groupby('player_id')['event_date'].rank()
    return activity[activity['rnk'] == 1][['player_id','event_date']].rename(columns={'event_date':'first_login'})



#another way

    import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    dictionary={}
    for i in range(len(activity)):
        pid = activity['player_id'][i]
        ed = activity['event_date'][i]
        if pid in dictionary:
            if ed < dictionary[pid]:
                dictionary[pid] = ed
        else:
            dictionary[pid] = ed

    result = []
    for (key,value) in dictionary.items():
        result.append([key,value])
    return pd.DataFrame(result,columns=['player_id','first_login'])


#another way
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby(['player_id'])['event_date'].min().reset_index()
    return df.rename(columns={'event_date':'first_login'})


