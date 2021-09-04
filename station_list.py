#!/bin/python3
'''Print color-schemed internet radio station list.'''
from csv import reader

# enumerated station URL keys
URLS = {}


def get_station_list():
    '''Get station list.'''
    # color theme
    c_1 = '\x1b[38;2;72;201;176m'
    c_2 = '\x1b[38;2;244;208;63m'
    c_3 = '\x1b[38;2;220;118;51m'
    res = '\x1b[0m'

    with open('/home/foo/.scripts/radio_streams_vlc/csv/stations.csv') as csv_file:
        # CSV reader object
        csv_rec_list = list(enumerate(reader(csv_file), 1))
        # iterate through CSV records
        for num, rec in csv_rec_list:
            # print enumerated station info to screen
            print(f'{c_1}{num:>2}{res}  {c_2}{rec[0]:}{res}  {c_3}{rec[1]}{res}')
            # append enumerated station URL key to `URLS`
            URLS[num] = rec[2]
