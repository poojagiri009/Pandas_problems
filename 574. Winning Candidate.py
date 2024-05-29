import pandas as pd

def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    if(len(vote) == 0):
        return pd.DataFrame([],columns=['name'])
    mydict = {}
    candidateIdWithMaxVotes = -1
    max_vote = 0
    for i in range(len(vote)):
        cid = vote['candidateId'][i]
        if cid not in mydict:
            mydict[cid] = 0
        mydict[cid]+=1
        if max_vote < mydict[cid]:
            max_vote = mydict[cid]
            candidateIdWithMaxVotes = cid
    name = ""
    for i in range(len(candidate)):
        cname = candidate['name'][i]
        _id = candidate['id'][i]
        if _id == candidateIdWithMaxVotes:
            name = cname
            break
    return pd.DataFrame([name],columns=['name'])




#using pandas
import pandas as pd

def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    if len(vote) == 0:
        return pd.DataFrame([],columns=['name'])
    df = vote.groupby('candidateId').size().reset_index(name='votecount')
    winner_id = df.loc[df['votecount'].idxmax(),'candidateId']
    print(winner_id)
    df = candidate[candidate['id'] == winner_id]
    return df[['name']]


