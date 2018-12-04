import botometer

mashape_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
twitter_app_auth = {
    'consumer_key': 'xxxxxxxx',
    'consumer_secret': 'xxxxxxxxxx',
    'access_token': 'xxxxxxxxx',
    'access_token_secret': 'xxxxxxxxxxx',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@clayadavis')

# Check a single account by id
result = bom.check_account(1548959833)

# Check a sequence of accounts
accounts = ['@clayadavis', '@onurvarol', '@jabawack']
for screen_name, result in bom.check_accounts_in(accounts):
    # Do stuff with `screen_name` and `result`
