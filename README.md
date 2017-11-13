# README.md

This repo contains demonstrations of 'rolling up' Forex time series data.

The idea of 'roll-up' is simple.

I follow these steps to roll-up prices from micro-second observations to one-second observations:

* Get a zip file full of micro-second observations from the web(for EUR/USD data for example)
* Read the zip file into a CSV format and then a tablular data structure with rows and columns
* For each observation extract the one-second value from the observation timestamp
* Load the one-second values into the data structure as a new column called: 'ts1s'
* Use group-by syntax to extract a smaller data structure containing mean prices at one-second intervals
* Write the smaller structure to a compressed CSV file

The above steps can be used within loops if the micro-second observations are spread across multiple files.

The data for this repo comes from the world of Forex.

You can find the actual data at the google-drive-URL listed below:

https://drive.google.com/drive/folders/1jMFSP-_wTtt5rtdtQuQdtPQr6087xz6K

The above URL leads to 5 large tar files:

```bash
audusd.tar
eurusd.tar
gbpusd.tar
usdcad.tar
usdjpy.tar
```

Each tar file contains many zip files.

Each zip file contains many observations.

Each observation is a subsecond sampling of Forex prices.

Now that you have the general idea about one roll-up strategy and a URL leading to data, you can start.

# Steps to collect one second roll-ups

* Clone this repo to your home folder

```bash
cd ~
git clone https://github.com/danbikle/rollup
```

* Make a data folders in the above repo:

```bash
mkdir -p ~/rollup/data/forex_tarfiles/
cd    ~/rollup/data/
```

* Study the URL below:

* https://drive.google.com/drive/folders/1jMFSP-_wTtt5rtdtQuQdtPQr6087xz6K

* Copy Forex tar files from the above URL to 'data/forex_tarfiles' folder under the repo:

* When done you should see five tar files in that folder:

```bash
cd    ~/rollup/data/
ll forex_tarfiles/*tar
```

* I saw this:
```bash
dan@h79:~ $ 
dan@h79:~ $ cd ~/rollup/data/
dan@h79:~/rollup/data $ du -sh forex_tarfiles/
11G	forex_tarfiles/
dan@h79:~/rollup/data $ 
dan@h79:~/rollup/data $ ll forex_tarfiles/*tar
-rw-rw-r-- 1 dan dan 2113423360 Nov 11 16:09 forex_tarfiles/audusd.tar
-rw-rw-r-- 1 dan dan 3000883200 Nov 11 16:13 forex_tarfiles/eurusd.tar
-rw-rw-r-- 1 dan dan 2398720000 Nov 11 16:12 forex_tarfiles/gbpusd.tar
-rw-rw-r-- 1 dan dan 1845934080 Nov 11 16:13 forex_tarfiles/usdcad.tar
-rw-rw-r-- 1 dan dan 2438963200 Nov 11 16:13 forex_tarfiles/usdjpy.tar
dan@h79:~/rollup/data $ 
dan@h79:~/rollup/data $
```

* Install Anaconda Python in your home folder. I work on Linux so I used the commands below:

```bash
cd ~
wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
bash Anaconda3-5.0.1-Linux-x86_64.sh
mv anaconda3/bin/curl anaconda3/bin/curl-ana
echo 'export PATH="${HOME}/anaconda3/bin:$PATH"' >> ~/.bashrc
bash
```

* Un-tar zip files from the tar files into a folder called: 'zip':

```bash
cd ~/rollup/data
mkdir zip
cd    zip
tar xf ~/rollup/data/forex_tarfiles/audusd.tar
tar xf ~/rollup/data/forex_tarfiles/eurusd.tar
tar xf ~/rollup/data/forex_tarfiles/gbpusd.tar
tar xf ~/rollup/data/forex_tarfiles/usdcad.tar
tar xf ~/rollup/data/forex_tarfiles/usdjpy.tar
```

* When I ran the above commands on my laptop, the zip folder had observations going back to 2010.

* I used a few lines of simple Python-Pandas calls to inspect the first zip file:

```bash
dan@h79:~/rollup/data $ cd ..
dan@h79:~/rollup $ cd python/
dan@h79:~/rollup/python $ python
Python 3.6.2 |Anaconda, Inc.| (default, Sep 30 2017, 18:42:57) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> my_df = pd.read_csv('../data/zip/AUDUSD-2010-01.zip')
>>> my_df.head()
   AUD/USD  20100103 21:28:00.773  0.89808  0.89832
0  AUD/USD  20100103 21:28:16.897  0.89806  0.89836
1  AUD/USD  20100103 21:30:36.304  0.89770  0.89830
2  AUD/USD  20100103 21:30:36.550  0.89766  0.89804
3  AUD/USD  20100103 21:30:40.813  0.89801  0.89832
4  AUD/USD  20100103 21:31:06.413  0.89803  0.89834
>>>


>>> my_df = pd.read_csv('../data/zip/AUDUSD-2010-01.zip',names=['pair','ts','bid','ask'])
>>> my_df.head()
      pair                     ts      bid      ask
0  AUD/USD  20100103 21:28:00.773  0.89808  0.89832
1  AUD/USD  20100103 21:28:16.897  0.89806  0.89836
2  AUD/USD  20100103 21:30:36.304  0.89770  0.89830
3  AUD/USD  20100103 21:30:36.550  0.89766  0.89804
4  AUD/USD  20100103 21:30:40.813  0.89801  0.89832
>>>
```

* You should try the above Python-Pandas calls on your laptop.

* If you see something similar to what I display above, then you are on the right track.

* Next, run the script listed below which should roll-up prices from micro-second observations to one-second observations.

```bash
cd ~/rollup/python
~/anaconda3/bin/python rollup1s.py
```

* The script should write the rolled-up prices to this folder:

```bash
~/rollup/data/csv1s/
```

* I ran the above script on my laptop and it needed 92 minutes to complete.



