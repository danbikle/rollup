# README.md

This repo contains demonstrations of 'rolling up' time series data.

The idea of 'roll-up' is simple.

I follow these steps to roll-up prices from micro-second observations to one-second observations:

* Get a zip file full of micro-second observations from the web(for EURUSD data for example)
* Unzip the file into a CSV file
* Read the CSV file into a tablular data structure with rows and columns
* For each observation extract the one-second value from the observation timestamp
* Load the one-second values into the data structure as a new column called: 'ts1s'
* Sort the data structure by ts1s
* Find the mean prices for each ts1s group in the structure
* Use group-by syntax to extract a smaller data structure containing mean prices at one-second intervals
* Write the smaller structure to CSV file

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

* Make a data folder in the above repo:

```bash
mkdir ~/rollup/data/
cd    ~/rollup/data/
```

* Study the URL below:

* https://drive.google.com/drive/folders/1jMFSP-_wTtt5rtdtQuQdtPQr6087xz6K

* Copy Forex tar files from the above URL to 'data' folder under the repo:

* When done you should see something like this:

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




