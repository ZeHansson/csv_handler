import constants
from stock import *


def main():

    tickers_list = make_ticker_list(read_data(constants.INPUT_PATH))

    tickers = []
    tickers = make_new_ticker_list(tickers_list, tickers)
    
    csv_rows =make_rows(tickers)
    
    if constants.UPDATE:
            write_data(constants.OUTPUT_PATH, csv_rows , "a")
    else : 
            write_data(constants.OUTPUT_PATH, csv_rows , "w")
        
    print(f"file \n{constants.OUTPUT_PATH}\n created!")

def make_new_ticker_list(tickers_list, tickers):
    for tick in tickers_list:
        if len(tickers) > 0:
            tickers.append(stock(tick, None))
        else: 
            tickers.append(stock(tick, True))
    return tickers

def make_rows(tickers):
    csv_rows =["","","","","","","","","",""]
    for i in range(len(tickers)):
        tickers[i].convert_to_csv(i)
        
        csv_rows[0] = f"{csv_rows[0]}{tickers[i].get_rows()[0]}"
        csv_rows[1] = f"{csv_rows[1]}{tickers[i].get_rows()[1]}"
        csv_rows[2] = f"{csv_rows[2]}{tickers[i].get_rows()[2]}"
        csv_rows[3] = f"{csv_rows[3]}{tickers[i].get_rows()[3]}"
        csv_rows[4] = f"{csv_rows[4]}{tickers[i].get_rows()[4]}"
        csv_rows[5] = f"{csv_rows[5]}{tickers[i].get_rows()[5]}"
        csv_rows[6] = f"{csv_rows[6]}{tickers[i].get_rows()[6]}"
        csv_rows[7] = f"{csv_rows[7]}{tickers[i].get_rows()[7]}"
        csv_rows[8] = f"{csv_rows[8]}{tickers[i].get_rows()[8]}"
        csv_rows[9] = f"{csv_rows[9]}{tickers[i].get_rows()[9]}"

    return csv_rows


def read_data(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data

def write_data(path, csv_rows, type):
    with open(path, type) as f:
        for row in csv_rows:
            f.write(row + "\n")
        f.close()

def make_ticker_list(input_data):
    ticker_list = input_data.replace(" ","").upper().split(",")
    return ticker_list

main()