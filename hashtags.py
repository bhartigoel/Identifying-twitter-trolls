import csv
import pandas as pd
import pprint

# hashtags = []
#
# with open('ira_tweets_csv_hashed.csv', encoding="utf8", mode='r') as f:
#     reader = csv.reader(f, delimiter=',')
#     for row in reader:
#         hashtags.append(row[27])
#
# df = pd.DataFrame(hashtags,columns=['Word Count:'])
# final_results = df.apply(pd.value_counts)
# final_results.to_csv('hashtags.csv')
#
# print (final_results)

hashtag_counter = dict()

df = pd.read_csv(
        'ira_tweets_csv_hashed.csv',
        skipinitialspace=True,
        usecols=['hashtags']
    )

def count_hashtag(row):
    if type(row['hashtags']) == str:
        real_hastags = row['hashtags'][1:-1].split(', ')
        for tag in real_hastags:
            if tag in hashtag_counter:
                hashtag_counter[tag][1] += 1
            elif tag != '':
                hashtag_counter[tag] = [tag, 1]


df.apply(lambda row: count_hashtag(row), axis=1)

hashtag_counter_df = pd.DataFrame.from_dict(
    hashtag_counter,
    orient='index',
    columns=['hashtag', 'count']
)

hashtag_counter_df = hashtag_counter_df.sort_values(by=['count'], ascending=False)
hashtag_counter_df['cumulative_count'] = hashtag_counter_df['count'].cumsum()

hashtag_counter_df.to_csv('hashtags.csv', index=False)
