import os
import random
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    body = request.values.get('Body', None)
    frm = request.values.get('From', None)
    resp = MessagingResponse()

    # Message Logic 
    seen_it = set()
    with open('assets/response.log','r+') as res:
        for line in res:
            seen_it.add(line.split(' says ')[0])

    with open('assets/response.log','a+') as res:
        res.write(frm + " says " + body + '\n')

    # 1st Reply Message
    if frm not in seen_it:
        resp.message("May the new decade find you great happiness and prosperity.")
    else: # Subsequent Reply Messages
        emoji = ['🎉','🎊','🥂','🌃','🎆','🎈','🥳']
        resp.message(emoji[random.randint(0,len(emoji)-1)])

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

