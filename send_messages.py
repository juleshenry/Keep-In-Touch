#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import time
import os
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

def phone_s_clean(s):
    if s[0:2] != '+1': 
        s = '+1' + s
    elif s[0] == '1':
        s = '+' + s
    return s.replace('\n','').replace('(','').replace(')','').replace('-','').replace(' ','')

def get_number_name_tuples():
    contacts = []
    try:
        with open('assets/contacts.vcf','r+') as f:
            want_tel = False
            for line in f:         
                if 'N' == line.split(':')[0]:
                    k = -2
                    while -k <= len(line.split(';')):
                        if len(line.split(';')[k]) > 1:
                            # print(line.split(';')[k])
                            break
                        k -=1
                    name_candidate = line.split(';')[k].split(' ')[0]
                    want_tel =~ want_tel
                if 'END' in line.split(';')[0] and want_tel:
                    name_candidate = ''
                    want_tel =~ want_tel
                if 'TEL' in line.split(';')[0] and want_tel:
                    contacts += [(phone_s_clean(line.split(':')[1]),name_candidate)]
                    want_tel =~ want_tel
    except:
        print("Warning: no contacts.vcf given in assets folder")
    return contacts

def send_msg(sender_name):
    contacts = get_number_name_tuples()
    try:
        account_sid = ''# os.environ['ACNT']
        auth_token = '' # os.environ['AUTH']
    except:
        raise Exception('Warning: environment variables for API call not set')
    client = Client(account_sid, auth_token)
    your_name = sender_name
    for tup in contacts:
        time.sleep(1)
        number, name = tup[0], tup[1]
        try: # The first message your contact will receive
            message = client.messages \
                            .create(
                                body=f"Happy New Year, {name}!!! (~‾⌣‾)~\nCheers, {your_name}",
                                from_='+12028731104',
                                to=f"{number}"
                            )
        except:
            continue
    print(time.asctime())
    print(message.sid)

# *** Uncomment at your own risk ***
# send_msg('Foo Bar')
