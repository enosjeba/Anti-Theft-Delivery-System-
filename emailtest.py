

#! /usr/bin/python

# Imports
import requests

def send_simple_message():
    print("I am sending an email.")
    return requests.post(
        "https://api.mailgun.net/v3/sandboxded521de48ff43d882fd24ac0e37f192.mailgun.org/messages",
        auth=("api", "9ff2862027ac32335ef517d658dce8c4-054ba6b6-308e33d7"),
        
        data={"from": "Security Alert: Antitheft@mailgun.co",
            "to":["skhumaira0707@gmail.com"],
            "subject": "Visitor Alert",
            "html": "<html> Hello. </html> "})
                  
request = send_simple_message()

print ('Status: '+format(request.status_code))
print ('Body:'+ format(request.text))

