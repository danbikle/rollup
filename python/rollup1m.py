"""
rollup1m.py
This script should roll-up prices from one-second observations in bz2 files to one-minute observations.

The bz2 files should be read from ../data/csv1s/*bz2
The results should get written to ../data/csv1m/

Demo:
~/anaconda3/bin/python rollup1m.py

"""

import glob
import pandas as pd
import pdb
import os

# I should ensure that the output folder exists:
os.system('mkdir -p ../data/csv1m/')

fn_l = glob.glob('../data/csv1s/*bz2')

for fn_s in sorted(fn_l):
    pdb.set_trace()
    fx0_df = pd.read_csv(fn_s)
    ts1m_sr        = fx0_df.ts1s.str.slice(0,14)
    fx0_df['ts1m'] = ts1m_sr
    # I should group-by ts1m and avg bid, ask
    ask_sr = fx0_df.groupby('ts1m').ask.mean()
    bid_sr = fx0_df.groupby('ts1m').bid.mean()
    # I should create a DF from bid_sr, ask_sr with ts1m as the index:
    fx1_df = pd.DataFrame({'bid':bid_sr, 'ask':ask_sr})
    # I should write it to CSV:
    'bye'
'bye'
