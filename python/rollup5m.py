"""
rollup5m.py
This script should roll-up prices from one-minute observations in bz2 files to one-minute observations.

The bz2 files should be read from ../data/csv1m/*bz2
The results should get written to ../data/csv5m/

Demo:
~/anaconda3/bin/python rollup5m.py

"""

import glob
import pandas as pd
import pdb
import os

print('Busy writing csv data to ../data/csv5m')

# I should ensure that the output folder exists:
os.system('mkdir -p ../data/csv5m/')

fn_l = glob.glob('../data/csv1m/*bz2')

for fn_s in sorted(fn_l):
    fx0_df     = pd.read_csv(fn_s)
    ts1m_dt_sr = pd.to_datetime(fx0_df.ts1m, utc=True)
    # I should convert series to unix-time format:
    ts1m_i_sr  = ts1m_dt_sr.dt.strftime("%s").astype('int')
    # I should create series of integers which are divisible by 300
    fx0_df['ts5m'] = (ts1m_i_sr/300).astype('int')*300
    # I should group-by ts5m and avg bid, ask
    ask_sr = fx0_df.groupby('ts5m').ask.mean()
    bid_sr = fx0_df.groupby('ts5m').bid.mean()
    # I should create a DF from bid_sr, ask_sr with ts5m as the index:
    fx1_df = pd.DataFrame({'bid':bid_sr, 'ask':ask_sr})
    # I should get the pair name from fn_s
    pair_s = fn_s[14:20]
    # I should write it to CSV:
    csvn_s = '../data/csv5m/'+pair_s+'.csv'
    fx1_df.to_csv(csvn_s,float_format='%4.6f', mode='a') # append
    # I can inspect output with python:
    # pd.read_csv(csvn_s).head()
    # Or bash:
    # bzip2 -cd ../data/csv5m/AUDUSD-2010-01.csv.bz2|head
    # I should prevent memory consumption:
    del(fx0_df)
    del(fx1_df)
    del(ts1m_dt_sr)
    del(ts1m_i_sr)
    del(ask_sr)
    del(bid_sr)
    'bye'
'bye'
