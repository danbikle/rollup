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
    # goog python pandas string operations
    ts1s_sr = fx0_df.ts.str.slice(0,17)
    'bye'
'bye'
