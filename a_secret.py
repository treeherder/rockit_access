import eventbrite


auth_tokens = {'app_key': 'SOME_APP_KEY_HERE',
'user_key': 'YOUR_api_key_here'}
eb = eventbrite.EventbriteClient(auth_tokens)

eb = eventbrite.EventbriteClient(eb_auth_tokens)
twil_auth = {"sid":"SOME_SID", "token": "SOME_TOKEN"}