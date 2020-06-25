# Keep-In-Touch

Keep in Touch is a program that uses the Twilio API to send pulse messages to close contacts, designated in assets/contacts.vcf. 

For Linux/Mac OS, you can modify crontab like so: 

58 23 31 12 2 ~.../send_messages.py &>/tmp/send_messages.log

#Story 

On New Year's Eve 2019, I sent 160 messages to close friends and family. Although some responses were lost in the fold due to heavy traffic, most data was captured accurately. The program sent a greeting message, followed by another greeting for a first response and then returned from a random collection of appropriate emoji's. 

Pulse Response Times:
The quantiles between 2019-12-31 11:58 to 2020-01-01 14:48  were as follows:

Quantile 0.25: 2020-01-01 00:02:55.750000128
Quantile 0.5: 2020-01-01 00:30:51
Quantile 0.75: 2020-01-01 02:46:15

Visualized as deciles on a number-line:
![alt text](https://imgur.com/7a5h8rf.png)

Response Distribution:
Out of 160 recepients, 82 responses were captured in the subsequent fourteen hours after New Year's. Here is the number of responses, including the iOS reaction as a response as well. The highest response count recorded stood at 19 messages.

Histogram (excludes 0 responses)
![alt text](https://imgur.com/imwT7OB.png)
