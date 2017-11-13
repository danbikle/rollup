"""
rollup1s.py
This script should roll-up prices from micro-second observations in zip files to one-second observations.

The zip files should be read from ../data/zip/*zip
The results should get written to ../data/csv1s/

Demo:
~/anaconda3/bin/python rollup1s.py

"""

import glob
import pandas as pd
import pdb
import os

# I should ensure that the output folder exists:
os.system('mkdir -p ../data/csv1s/')

fn_l = glob.glob('../data/zip/*zip')

for fn_s in sorted(fn_l):
    fx0_df = pd.read_csv(fn_s, names=['pair','ts','bid','ask'])
    ts1s_sr        = fx0_df.ts.str.slice(0,17)
    fx0_df['ts1s'] = ts1s_sr
    # I should group-by ts1s and avg bid, ask
    ask_sr = fx0_df.groupby('ts1s').ask.mean()
    bid_sr = fx0_df.groupby('ts1s').bid.mean()
    # I should create a DF from bid_sr, ask_sr with ts1s as the index:
    fx1_df = pd.DataFrame({'bid':bid_sr, 'ask':ask_sr})
    # I should write it to CSV:
    csvn_s = fn_s.replace('zip','csv').replace('/csv/','/csv1s/')
    fx1_df.to_csv(csvn_s+'.bz2',float_format='%4.6f',compression='bz2')
    print('Wrote: ',csvn_s+'.bz2')
    # I can inspect output with python:
    # pd.read_csv(csvn_s+'.bz2').head()
    # Or bash:
    # bzip2 -cd AUDUSD-2010-01.csv.bz2|head
    delete(fx0_df)
    delete(fx1_df)
    delete(ts1s_sr)
    'bye'
'bye'
