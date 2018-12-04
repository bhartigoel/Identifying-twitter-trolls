import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
from collections import Counter


#import Levenshtein as Lev

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

# import datau
fileu = os.path.join('C:\\Users\\bharti\\Desktop\\Social_Media_Mining\\Notebooks\\final paper', 'ira_users_csv_hashed.csv')
datau = pd.read_csv(fileu)
print datau.head()

#filet = os.path.join('C:\\Users\\bharti\\Desktop\\Social_Media_Mining\\Notebooks\final paper', 'merged_tweets.csv')
#datat = pd.read_csv(filet)

#datat['tweet_has_link']=np.where(datat['text'].notnull() &   datat['text'].str.contains("http"),1,0)
#datat['weekday'] = datat['created_at'].str[0:3]
#datat['weekdate'] = datat['created_at'].str[11:13]


# print datau head


#1
datau['less_than_30_followers']=np.where(datau['follower_count']<30,1,0)
#2
#datau['default_profile_image']=np.where(datau['default_profile_image']==1,1,0)
#3
datau['not_geo_located']=np.where(datau['user_reported_location'].isnull(),0,1)
#4
datau['following_count_zero']=np.where(datau['following_count']<10,0,1)

#5
datau['description_has_link']=datau['user_profile_description'].notnull() &   datau['user_profile_description'].str.contains("http") 
#6
datau['50:1']=datau['follower_count']/(datau['following_count']+1)



#7
#datau['hastag']= datat['num_hashtags'].groupby(datat['user_id']).mean().reset_index()['num_hashtags']
#df= len(datat.user_id.unique())
#print len(datat['num_hashtags'].groupby(datat['user_id']).mean())
#8

#datau['avg_hyperlink_in_tweets']= datat['tweet_has_link'].groupby(datat['user_id']).mean().reset_index()['tweet_has_link']
#9-15
#df= pd.DataFrame(datat.groupby(['user_id']).weekday.value_counts().unstack(fill_value=0))
#normalized_df=pd.DataFrame((df-df.min())/(df.max()-df.min()))

#df_hastag=pd.DataFrame(datat['num_hashtags'].groupby(datat['user_id']).mean())
#df_avg_hyperlink= pd.DataFrame(datat['tweet_has_link'].groupby(datat['user_id']).mean())

#print normalized_df['Mon']
##datau['Mon']= normalized_df['Mon'].reset_index()['Mon']
##datau['Tue']= normalized_df['Tue'].reset_index()['Tue']
##datau['Wed']= normalized_df['Wed'].reset_index()['Wed']
##datau['Thu']= normalized_df['Thu'].reset_index()['Thu']
##datau['Fri']= normalized_df['Fri'].reset_index()['Fri']
##datau['Sat']= normalized_df['Sat'].reset_index()['Sat']
##datau['Sun']= normalized_df['Sun'].reset_index()['Sun']

#normalized_df.rename(columns={'user_id': 'id'}, inplace=True)
#result = pd.concat([ df_hastag,normalized_df,],axis=1)
#result = pd.concat([ df_avg_hyperlink,result,],axis=1)
files = os.path.join('C:\\Users\\bharti\\Desktop\\Social_Media_Mining\\Notebooks\\final paper', 'merged_featuresg.csv')
#result['id']=result['user_id']

#result.rename(index=str, columns={'user_id': 'id'})
datau.to_csv(files, sep=',')
#fileu = os.path.join('C:\\Users\\bharti\\Desktop\\Social_Media_Mining\\Hackathon\\data', 'featuresg.csv')
datar= pd.read_csv(files)

#datar.rename(index=str, columns={'user_id': 'id'})
#datar['id']=datar['user_id']
#print datau['hastag']
#datar = pd.merge(datau, datar, on='id')
#filetf = os.path.join('C:\\Users\\bharti\\Desktop\\Social_Media_Mining\\Hackathon\\data', 'merged_features_tweet.csv')
#datar.to_csv(filetf, sep=',')
print datau.head()
#print datat.head()

#plt.hist(np.log(datac['follower_count']+1),bins='auto')
#plt.title('logarithmic plot of follower_count for twitter troll data')
#plt.show()


filec = os.path.join('C:\\Users\\bharti\\Desktop\\Social_Media_Mining\\Notebooks\\final paper', 'collected_user_data.csv')
datac = pd.read_csv(filec)
plt.hist(np.log(datac['followers_count']+1),bins='auto')
plt.title('logarithmic plot of follower_count for twitter user data (coolected by us)')
plt.show()
#print datau['50:1']

letter_countsu = Counter(datau['account_language'])
letter_countsc = Counter(datac['lang'])
df1 = pd.DataFrame.from_dict(letter_countsu, orient='index')

df1['troll']=df1[0]

df1.drop(df1.columns[[ 0]], axis=1)#print df1
print df1
df2 = pd.DataFrame.from_dict(letter_countsc, orient='index')
df2['user']=df2[0]

df3=pd.concat([df2*100/len(datac.index), df1*100/len(datau.index)], axis=1, join_axes=[df2.index])
#df3.drop(df3.columns[ [0]], axis=1)
print df3
#print sum(letter_countsu)
#df1.plot(kind='bar')
df3.loc[:,['troll','user']].plot(kind='bar')
#ax = df1.plot(kind='bar')
#df2.plot(kind='bar',ax=ax)
plt.show()
