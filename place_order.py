import time
import requests
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

pwn=GPIO.PWM(12,50)
pwn.start(5)
pwn.ChangeDutyCycle(7.5)
print("The delivery executive is at the restaurant")
time.sleep(10)
pwn.stop



pwn.start(7.5)
pwn.ChangeDutyCycle(12)
print("The delivery executive is placing the order inside the box")






def send_simple_message():
    print("I am sending an email.")
    return requests.post(
        "https://api.mailgun.net/v3/sandboxded521de48ff43d882fd24ac0e37f192.mailgun.org/messages",
        auth=("api", "9ff2862027ac32335ef517d658dce8c4-054ba6b6-308e33d7"),
        
        data={"from": "Delivery Update: Antitheft@mailgun.co",
            "to":["sahayaajith202@gmail.com"],
            "subject": "Smart Box Unlocked",
            "html": "<html> Hello, Customer we are happy to inform that your item is prepared and the door has been unlocked to placed the item inside it. Thank You!!! </html> "})
                  
request = send_simple_message()

print ('Status: '+format(request.status_code))
print ('Body:'+ format(request.text))

time.sleep(20)
pwn.stop




pwn.start(7.5)
pwn.ChangeDutyCycle(7.5)
print("The delivery has placed the item inside the box")
import requests

def send_simple_message():
    print("I am sending an email.")
    return requests.post(
        "https://api.mailgun.net/v3/sandboxded521de48ff43d882fd24ac0e37f192.mailgun.org/messages",
        auth=("api", "9ff2862027ac32335ef517d658dce8c4-054ba6b6-308e33d7"),
        
        data={"from": "Delivery Update: Antitheft@mailgun.co",
            "to":["sahayaajith202@gmail.com"],
            "subject": "Smart Box locked",
            "html": "<html> Wohooo!! your smart box has been locked and your item is arriving soon within 25-30 mins. Thank You!! </html> "})
                  
request = send_simple_message()

print ('Status: '+format(request.status_code))
print ('Body:'+ format(request.text))
time.sleep(10)
pwn.stop




