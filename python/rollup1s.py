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

fn_l = glob.glob('../data/zip/*zip')

for fn_s in sorted(fn_l):
    pdb.set_trace()
    fx0_df = pd.read_csv(fn_s, names=['pair','ts','bid','ask'])
    ts1s_sr        = fx0_df.ts.str.slice(0,17)
    fx0_df['ts1s'] = ts1s_sr
    # I should group-by ts1s and avg bid, ask
    fx1_df = fx0_df.copy()[['ts1s','bid','ask']]
    bid_sr = fx1_df.groupby('ts1s').bid.mean()
    ask_sr = fx1_df.groupby('ts1s').ask.mean()
    # I should create a DF from bid_sr, ask_sr with ts1s as the index:
    fx2_df = pd.DataFrame({'bid':bid_sr, 'ask':ask_sr})
    type(fx2_df)
    fx2_df.head()
    'bye'
'bye'
