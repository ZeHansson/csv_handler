# csv_handler

## constants.py
Constants.py acts as a config. 
API needs to be the used api.
input is where tu pull data from
output is where to put the resulting .csv file
Update is not fully implemented yet. For now it should be false. (the intention is to flag if it should look for output first and then take input and add them in line with. currently it will add it below, which is not supported)


# To run main.py

It requries a input file that corresponds to the name in constants.

No handling of exceptions what so ever, Use at your own risk.