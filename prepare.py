import pandas as pd

def report_col_with_null_df(df):
    need_attention_col = []
    num_null = []
    
    #null_pd = pd.DataFrame()
    for c in df.columns.tolist():
        
        if df[c].isnull().sum() != 0:
            need_attention_col.append(c)
            num_null.append(df[c].isnull().sum())
        
        null_pd = pd.DataFrame(need_attention_col).T
        null_pd = pd.concat([null_pd, (pd.DataFrame(num_null).T)])

    return null_pd


def report_col_with_null(df):
    need_attention_col = []
    num_null = []
    
    #null_pd = pd.DataFrame()
    for c in df.columns.tolist():
        print(c)
        print('------------------------------------------------------------')
        print('Number of nulls in', c,'is: {}'.format(df[c].isnull().sum()))
        print('------------------------------------------------------------')
        print('Number of unique items: {}'.format(df[c].value_counts(ascending = False)))
        print('------------------------------------------------------------')
        if df[c].isnull().sum() != 0:
            need_attention_col.append(c)
            num_null.append(df[c].isnull().sum())
            
        else:
            print('good to go!')
        #simple_list = [need_attention_col]
        #simple_list.append(num_null)
        #null_pd = pd.DataFrame(simple_list)
        
        null_pd = pd.DataFrame(need_attention_col).T
        null_pd = pd.concat([null_pd, (pd.DataFrame(num_null).T)])
        
        
        #row=pd.Series(need_attention_col,num_null)
        #null_pd.append([row],ignore_index=True)
        #null_pd = pd.DataFrame(need_attention_col).T
        #null_pd['number_of_nulls'] = num_null.T
        #null_pd.append(num_null,ignore_index=True)
    return null_pd
#null_pd
    