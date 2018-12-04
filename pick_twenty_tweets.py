import pandas as pd

df = pd.read_csv(
        'ira_tweets_csv_hashed.csv',
        skipinitialspace=True
    )

twenty_df = pd.DataFrame(columns=df.columns)

unique_user_ids = df['userid'].unique()
print(len(unique_user_ids))

for uid in unique_user_ids[:1000]:
    twenty_df = pd.concat([twenty_df, df[df.userid == uid][:20]])

twenty_df.to_csv('twenty_tweets_per_user.csv')
