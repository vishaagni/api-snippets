# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Let's grab lunch at Milliways tomorrow!",
    to="+15558675310",
    from_="+14158141829",
    media_url="http://www.example.com/cheeseburger.png"
)
print(message.sid)
