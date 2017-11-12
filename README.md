# README.md

This repo contains demonstrations of 'rolling up' time series data.

The data comes from the world of Forex.

Each observation is a subsecond sampling of Forex prices.

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

