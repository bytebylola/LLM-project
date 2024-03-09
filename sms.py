import os
from twilio.rest import Client

account_sid ='ACedddd78041e2ef37db22ddb717bafeca'
auth_token = 'fe3359325839ac8bf55e31d0daeade2f'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15098225799',
                     to='+918095296336'
                 )

print(message.sid)
