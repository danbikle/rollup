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

Each zip file contains many observations (in CSV format).

Each observation is a subsecond sampling of Forex prices.

Now that you have the general idea about one roll-up strategy and a URL leading to data, you can start.

# Steps to collect one second roll-ups

* Clone this repo to your home folder (not some other folder).

```bash
cd ~
git clone https://github.com/danbikle/rollup
```

* Make data folders in the above repo:

```bash
mkdir -p ~/rollup/data/forex_tarfiles/
cd       ~/rollup/data/
```

* Study the URL below:

* https://drive.google.com/drive/folders/1jMFSP-_wTtt5rtdtQuQdtPQr6087xz6K

* Copy Forex tar files from the above URL to 'data/forex_tarfiles' folder under the repo:

* When done you should see five tar files in that folder:

```bash
ls -la ~/rollup/data/forex_tarfiles/*tar
```

* I saw this:
```bash
dan@h79:~ $ 
dan@h79:~ $ cd ~/rollup/data/
dan@h79:~/rollup/data $ du -sh forex_tarfiles/
11G	forex_tarfiles/
dan@h79:~/rollup/data $ 
dan@h79:~/rollup/data $ ls -la forex_tarfiles/*tar
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
mkdir -p ~/rollup/data/zip
cd       ~/rollup/data/zip
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
```

It appears the data has no column headings.
I used a Pandas parameter named: 'names' to add my headings:

```bash
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

* I used three shell commands to inspect the output:

```bash
dan@h79:~/rollup $ du -sh ~/rollup/data/csv1s # How large is the output?
1.9G	/home/dan/rollup/data/csv1s
dan@h79:~/rollup $ 
dan@h79:~/rollup $


dan@h79:~/rollup $ ls -la ~/rollup/data/csv1s/ | head
total 1963144
drwxrwxr-x 2 dan dan    20480 Nov 12 18:06 .
drwxrwxr-x 7 dan dan     4096 Nov 12 21:53 ..
-rw-rw-r-- 1 dan dan  2871751 Nov 12 16:34 AUDUSD-2010-01.csv.bz2
-rw-rw-r-- 1 dan dan  2348084 Nov 12 16:34 AUDUSD-2010-02.csv.bz2
-rw-rw-r-- 1 dan dan  3167067 Nov 12 16:34 AUDUSD-2010-03.csv.bz2
-rw-rw-r-- 1 dan dan  2814488 Nov 12 16:35 AUDUSD-2010-04.csv.bz2
-rw-rw-r-- 1 dan dan  4727926 Nov 12 16:35 AUDUSD-2010-05.csv.bz2
-rw-rw-r-- 1 dan dan  4113280 Nov 12 16:35 AUDUSD-2010-06.csv.bz2
-rw-rw-r-- 1 dan dan  3817810 Nov 12 16:35 AUDUSD-2010-07.csv.bz2
dan@h79:~/rollup $ 
dan@h79:~/rollup $ 


dan@h79:~/rollup $ ls -la ~/rollup/data/csv1s/ | tail
-rw-rw-r-- 1 dan dan 10035652 Nov 12 18:03 USDJPY-2017-01.csv.bz2
-rw-rw-r-- 1 dan dan  8077095 Nov 12 18:03 USDJPY-2017-02.csv.bz2
-rw-rw-r-- 1 dan dan  9463666 Nov 12 18:04 USDJPY-2017-03.csv.bz2
-rw-rw-r-- 1 dan dan  8050948 Nov 12 18:04 USDJPY-2017-04.csv.bz2
-rw-rw-r-- 1 dan dan  9262043 Nov 12 18:05 USDJPY-2017-05.csv.bz2
-rw-rw-r-- 1 dan dan  9079336 Nov 12 18:05 USDJPY-2017-06.csv.bz2
-rw-rw-r-- 1 dan dan  5526826 Nov 12 18:05 USDJPY-2017-07.csv.bz2
-rw-rw-r-- 1 dan dan  5930854 Nov 12 18:06 USDJPY-2017-08.csv.bz2
-rw-rw-r-- 1 dan dan  5348660 Nov 12 18:06 USDJPY-2017-09.csv.bz2
-rw-rw-r-- 1 dan dan  5250981 Nov 12 18:06 USDJPY-2017-10.csv.bz2
dan@h79:~/rollup $ 
dan@h79:~/rollup $ 
```


* If you got this far on your laptop, you should keep going

* I see the files in csv1s to be the first stage of a 3 stage rollup

* To start on the second stage, inpsect this script:

https://github.com/danbikle/rollup/blob/master/python/rollup1m.py

* Next, run the above script with these shell commands:

```bash
cd ~/rollup/python
~/anaconda3/bin/python rollup1m.py
```

* I ran the above script and saw some output which is displayed below:

```bash
dan@h79:~ $ 
dan@h79:~ $ cd ~/rollup/python
dan@h79:~/rollup/python $ 
dan@h79:~/rollup/python $ 
dan@h79:~/rollup/python $ ~/anaconda3/bin/python rollup1m.py
Wrote:  ../data/csv1m/AUDUSD-2010-01.csv.bz2
Wrote:  ../data/csv1m/AUDUSD-2010-02.csv.bz2
Wrote:  ../data/csv1m/AUDUSD-2010-03.csv.bz2
Wrote:  ../data/csv1m/AUDUSD-2010-04.csv.bz2

SNIP ...

Wrote:  ../data/csv1m/USDJPY-2017-07.csv.bz2
Wrote:  ../data/csv1m/USDJPY-2017-08.csv.bz2
Wrote:  ../data/csv1m/USDJPY-2017-09.csv.bz2
Wrote:  ../data/csv1m/USDJPY-2017-10.csv.bz2
dan@h79:~/rollup/python $ 
dan@h79:~/rollup/python $ 
dan@h79:~/rollup/python $ 
```

* The above script needed 15 minutes to run on my laptop.

* The output folder was smaller than the input folder:

```bash
dan@h79:~/rollup/python $ cd ~/rollup/data/
dan@h79:~/rollup/data $ 
dan@h79:~/rollup/data $ du -sh csv1s csv1m
1.9G	csv1s
95M	csv1m
dan@h79:~/rollup/data $ 
dan@h79:~/rollup/data $
```

* I inspected the first and last files in the output folder:

```bash
dan@h79:~/rollup/data $ bzip2 -cd csv1m/AUDUSD-2010-01.csv.bz2 | head
ts1m,ask,bid
20100103 21:28,0.898340,0.898070
20100103 21:30,0.898245,0.897845
20100103 21:31,0.898340,0.898030
20100103 21:32,0.898275,0.897310
20100103 21:34,0.898290,0.897690
20100103 21:36,0.898737,0.897947
20100103 21:37,0.898855,0.898205
20100103 21:38,0.898670,0.898240
20100103 21:39,0.898710,0.898225
dan@h79:~/rollup/data $
dan@h79:~/rollup/data $


dan@h79:~/rollup/data $ bzip2 -cd csv1m/USDJPY-2017-10.csv.bz2 | head
ts1m,ask,bid
20171001 21:03,112.620443,112.466786
20171001 21:04,112.617667,112.486333
20171001 21:05,112.573250,112.497125
20171001 21:06,112.574225,112.484707
20171001 21:07,112.566472,112.486515
20171001 21:08,112.592050,112.461283
20171001 21:09,112.587962,112.456269
20171001 21:10,112.533788,112.492685
20171001 21:11,112.547400,112.491900
dan@h79:~/rollup/data $ 
dan@h79:~/rollup/data $
```

* If you got this far on your laptop, you should keep going

* I see the files in csv1m to be the second stage of a 3 stage rollup

* To start on the third stage, inspect this script:

https://github.com/danbikle/rollup/blob/master/python/rollup5m.py

* Next, run the above script with these shell commands:

```bash
cd ~/rollup/python
~/anaconda3/bin/python rollup5m.py
```


* I ran the above script and saw some output which is displayed below:

```bash
dan@h79:~ $ 
dan@h79:~ $ cd ~/rollup/python
dan@h79:~/rollup/python $ 
dan@h79:~/rollup/python $ 


dan@h79:~/rollup/python $ ~/anaconda3/bin/python rollup5m.py
Busy writing csv data to ../data/csv5m
dan@h79:~/rollup/python $ 
dan@h79:~/rollup/python $ 


dan@h79:~/rollup/python $ ls -la ../data/csv5m/
total 164928
drwxrwxr-x 2 dan dan    24576 Nov 12 23:14 ./
drwxrwxr-x 7 dan dan     4096 Nov 12 21:53 ../
-rw-rw-r-- 1 dan dan 34238569 Nov 13 16:16 AUDUSD.csv
-rw-rw-r-- 1 dan dan 32808984 Nov 13 16:17 EURUSD.csv
-rw-rw-r-- 1 dan dan 32813856 Nov 13 16:17 GBPUSD.csv
-rw-rw-r-- 1 dan dan 32598386 Nov 13 16:18 USDCAD.csv
-rw-rw-r-- 1 dan dan 36373896 Nov 13 16:18 USDJPY.csv
dan@h79:~/rollup/python $ 
dan@h79:~/rollup/python $ 
```

Notice that rollup5m.py had a duration of about 4 minutes.

Also notice that the output files are not compressed:

```bash
dan@h79:~/rollup/python $ du -sh ../data/csv5m/*csv
33M	../data/csv5m/AUDUSD.csv
32M	../data/csv5m/EURUSD.csv
32M	../data/csv5m/GBPUSD.csv
32M	../data/csv5m/USDCAD.csv
35M	../data/csv5m/USDJPY.csv
dan@h79:~/rollup/python $ 
dan@h79:~/rollup/python $ 


dan@h79:~/rollup/python $ head ../data/csv5m/*csv
==> ../data/csv5m/AUDUSD.csv <==
ts5m,ask,bid
1262582700,0.898340,0.898070
1262583000,0.898287,0.897719
1262583300,0.898743,0.898154
1262583600,0.898810,0.898414
1262583900,0.898893,0.898490
1262584200,0.898905,0.898445
1262584500,0.898817,0.898367
1262584800,0.898789,0.898437
1262585100,0.898852,0.898521

==> ../data/csv5m/EURUSD.csv <==
ts5m,ask,bid
1262582700,1.431004,1.430730
1262583000,1.430770,1.430507
1262583300,1.430667,1.430382
1262583600,1.430913,1.430610
1262583900,1.430832,1.430522
1262584200,1.430533,1.430124
1262584500,1.430241,1.429957
1262584800,1.430351,1.430098
1262585100,1.430225,1.429979

==> ../data/csv5m/GBPUSD.csv <==
ts5m,ask,bid
1262582700,1.613610,1.612887
1262583000,1.612035,1.611283
1262583300,1.611810,1.610866
1262583600,1.611708,1.611048
1262583900,1.611226,1.610816
1262584200,1.611391,1.610671
1262584500,1.611557,1.610947
1262584800,1.611461,1.610957
1262585100,1.611229,1.610783

==> ../data/csv5m/USDCAD.csv <==
ts5m,ask,bid
1262583000,1.052640,1.051770
1262583600,1.052650,1.051780
1262583900,1.052625,1.051763
1262584800,1.052540,1.051710
1262585100,1.052320,1.051670
1262585400,1.051597,1.051092
1262585700,1.051200,1.050860
1262586000,1.050981,1.050466
1262586300,1.050900,1.050248

==> ../data/csv5m/USDJPY.csv <==
ts5m,ask,bid
1262582700,93.002000,92.979500
1262583000,93.011806,92.979472
1262583300,93.001834,92.970416
1262583600,93.008867,92.967100
1262583900,93.000000,92.967000
1262584200,92.997900,92.963178
1262584500,93.015885,92.984903
1262584800,93.001022,92.977433
1262585100,93.057137,93.033794
dan@h79:~/rollup/python $ 
dan@h79:~/rollup/python $
```
