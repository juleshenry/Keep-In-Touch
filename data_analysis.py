#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import random
import time
import os
import numpy as np
import pandas as pd
import matplotlib.dates as md
from dateutil import parser
import matplotlib.pyplot as plt
from send_messages import get_number_name_tuples

def get_name(s):
    numb_name_list = get_number_name_tuples()
    for tup in numb_name_list:
        if tup[0].strip().replace('+','') == s:
            return tup[1]
    return str(tup)

def get_res_dict():
    resp = ''
    try:
        with open('assets/response.log','r+') as file:
            for i in file:
                resp += i.replace('\n','')
    except:
        raise Exception('No response.log exists')
    res_dict = {}
    for i in resp.split('+'):
        name = get_name(i.split(' ')[0])
        quote = ' ' + ' '.join(i.split(' ')[1:])
        if name not in res_dict.keys():
            res_dict.update({name: ([quote],1)})
        elif name in res_dict.keys():
            # print(res_dict.get(name))
            info_resp = res_dict.get(name)
            quote_list = info_resp[0]
            quote_list += [quote]
            new_cnt = info_resp[1]+1
            res_dict.update({name: (quote_list,new_cnt)})
    return res_dict

def write_out_res_dict(filename):
    res_dict = get_res_dict()
    reply_txt = ''
    filename = 'assets/' + filename
    for k in res_dict.keys():
        if res_dict.get(k) is not None:
            reply_txt += str(k) + str(res_dict.get(k)[0]).replace('says','') + '\n'
    with open(filename,'a+') as o:
        o.write(reply_txt)

def plot_freq_hist():
    res_dict = get_res_dict()
    res_freq_dict = {}
    for k in res_dict.keys():
        res_freq_dict.update({k:res_dict.get(k)[1]})
    res_freq_dict = {k: v for k, v in sorted(res_freq_dict.items(), key=lambda item: item[1],reverse=True)}
    plt.bar(res_freq_dict.keys(), res_freq_dict.values(), edgecolor='black', linewidth=1.2, color='b')
    plt.xticks([])
    plt.show()

def plot_pulse_time_chart():
    freq_list = []
    try:
        with open('assets/post_times.txt') as f:
            for i in f:
                d = i.split('[')[1].split(']')[0]
                freq_list += [parser.parse(d)]
    except:
        print('WARNING: Please copy Flask POST request time log into assets/post_times.txt')
    sr_dt = pd.Series(freq_list, name='Request_Time') 
    df = pd.DataFrame(sr_dt)
    count = sr_dt.size
    ones = np.ones(count, dtype=int)
    df['Counts'] = ones

    quantile_list = [.25,.5,.75]
    quantiles = df['Request_Time'].quantile(quantile_list)
    
    for i, q in enumerate(quantiles):
        print(f"Quantile {quantile_list[i]}: {q}")
        plt.axvline(x=q,c=(0,quantile_list[i],0))

    plt.scatter(df['Request_Time'].tolist(), df['Counts'].tolist(), s = 2, c='red')
    plt.xlim(df['Request_Time'].iloc[0],df['Request_Time'].iloc[-1])
    plt.xticks( rotation= 80 )
    ax = plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%-d %H:%M:%S')
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(8) 
    ax.xaxis.set_major_formatter(xfmt)
    plt.subplots_adjust(bottom=.5)
    plt.ylim(.9, 1.1)
    ax.get_yaxis().set_ticks([])
    plt.show()

write_out_res_dict('replies.txt')
plot_freq_hist()
plot_pulse_time_chart()