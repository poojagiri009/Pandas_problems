
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    mydict={}
    for i in range(len(actor_director)):
        actor_id=actor_director['actor_id'][i]
        director_id=actor_director['director_id'][i]
        if (actor_id,director_id) not in mydict:
            mydict[(actor_id,director_id)] = 0
        mydict[(actor_id,director_id)]+=1
    result=[]
    for key,value in mydict.items():
        if value >=3:
            result.append(key)
    return pd.DataFrame(result,columns=['actor_id','director_id'])


#Using pandas
    import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id','director_id']).size().reset_index(name='count')
    return df[df['count'] >= 3][['actor_id','director_id']]


