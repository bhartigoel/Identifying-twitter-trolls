import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
from collections import Counter

fileu = os.path.join('C:\\Users\\bharti\\Desktop\\Social_Media_Mining\\Notebooks\\final paper', 'ira_tweets_csv_hashed.csv')
datau = pd.read_csv(fileu)
datau['len_prfl_desc']=np.where(datau['tweet_text'].notnull() ,  datau['tweet_text'].str.len(),0)
print datau.head()


filec = os.path.join('C:\\Users\\bharti\\Desktop\\Social_Media_Mining\\Notebooks\\final paper', 'collected_tweet_data.csv')
datac = pd.read_csv(filec)
datac['len_prfl_desc']=np.where(datac['text'].notnull() ,  datac['text'].str.len(),0)
print datac.head()


#boxplot2 = datac.boxplot(column=['len_prfl_desc'])
len_prfl_desc_user=pd.DataFrame(datac['len_prfl_desc'])
len_prfl_desc_user['type']='user'
len_prfl_desc_troll=pd.DataFrame(datau['len_prfl_desc'])
len_prfl_desc_troll['type']='troll'
frames = [len_prfl_desc_user,len_prfl_desc_troll]
len_prfl_desc= pd.concat(frames)
print len_prfl_desc.head()

boxplot1 = len_prfl_desc.boxplot(by=['type'])

#plt.hist(np.log(datac['followers_count']+1),bins='auto')
#plt.title('logarithmic plot of follower_count for twitter user data (coolected by us)')
plt.show()
#print datau['50:1']

letter_countsu = Counter(datau['account_language'])
letter_countsc = Counter(datac['lang'])
df1 = pd.DataFrame.from_dict(letter_countsu, orient='index')

df1['troll']=df1[0]

df1.drop(df1.columns[[ 0]], axis=1)
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
