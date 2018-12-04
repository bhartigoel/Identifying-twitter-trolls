import json
import requests
from requests_oauthlib import OAuth1
import pandas

# Maximum number of tweets to collect
MAX_TWEETS = 1
MAX_users = 10

credentials = {
    'CONSUMER_KEY': 'LNBGwnyEp3WDKT07MTlqYh7qQ',
    'CONSUMER_SECRET': 'rYqgw0fwkPjoZEizoMaJIrkXXOk8O3nVGoZDisJ6wuO4ERK2vU',
    'TOKEN_KEY': '867061253562286080-gmtnpROw3D272myNvJ12ZQ4u6y6IuHI',
    'TOKEN_SECRET': 'tgaaJsVXqFVtZZhhfQ9qIdzGI6kolx6NquOtHciUCRves',
}

def authenticate(credentials):
    try:
        oauth = OAuth1(client_key=credentials['CONSUMER_KEY'],
                       client_secret=credentials['CONSUMER_SECRET'],
                       resource_owner_key=credentials['TOKEN_KEY'],
                       resource_owner_secret=credentials['TOKEN_SECRET'],
                       signature_type='auth_header')
        client = requests.session()
        client.auth = oauth
        return client
    except (KeyError, TypeError):
        print('Error setting auth credentials.')
        raise

# API endpoint
url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
hashtags = ['#thanksgiving', '#ThatHashtag']
client = authenticate(credentials)
users = []
with open('tweets_3.json', mode='rb') as f:
    for line in f.readlines():
        users.append(json.loads(line)['user']['id'])


for user in users:
    print(user)
    response = client.get(url, stream=True, params={'user_id': user, 'count':20})
    users=set()
    if response.ok:
        f = open("tweets.json","wb")
        num_tweets = 0
        num_users=0
        try:
            for line in response.iter_lines():
                if line:
                    num_tweets+=1
                    f.write(line + b'\n')
                    line_json = line.decode('utf8')
                    line_data = json.loads(line_json)
                    # print (line_data)
                    # print(".", end='', flush=True)
                    print(line_json)
        except KeyboardInterrupt:
            # User pressed the 'Stop' button
            print()
            # print('Data collection interrupted by user!')
        finally:
            # Cleanup -- close file and report number of tweets collected
            f.close()
            print()
            print('Collected {} tweets.'.format(num_tweets))
    else:
        print('Connection failed with status: {}'.format(response.status_code))
