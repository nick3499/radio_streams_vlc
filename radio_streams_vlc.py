#!/usr/bin/env python
'''`vlc_radio_wrapper` module contains the `station_selection()` method which
displays a list of Internet radio stations from which the user chooses a
station by the number in the left column.'''
from csv import reader
from subprocess import run


def station_selection():
    '''`station_selection()` method displays a list of Internet radio stations
from a CSV database, and prompts the user make a selection.'''
    c1 = '\x1b[38;2;72;201;176m'  # cyan; format text RGB: 72, 201, 176
    c2 = '\x1b[38;2;244;208;63m'  # yellow
    c3 = '\x1b[38;2;220;118;51m'  # orange
    res = '\x1b[0m'  # reset to default
    urls = {}  # number selection: station URL
    pwd = '/scripts/py/vlc_radio_wrapper'  # module root directory

    with open(f'{pwd}/txt/ascii_radio.txt', 'r') as ascii_art:
        [print(f'{c1}{line[:-1]}{res}') for line in ascii_art]  # ASCII art

    # list stations
    with open(f'{pwd}/csv/stations.csv') as csv_file:
        csv_rec_list = list(enumerate(reader(csv_file), 1))  # csv reader object
        for num, rec in csv_rec_list:
            # print color-formatted radio station list
            print(f'{c1}{num:>2}{res}  {c2}{rec[0]:}{res}  {c3}{rec[1]}{res}')
            urls[num] = rec[2]  # append number with URL to dictionary

    station_num = int(input('Enter item number: '))  # input station number

    # pass CLI args to VLC media player, including radio station URL
    run(['/snap/bin/vlc', '--intf', 'ncurses', urls[station_num]], check=True)


if __name__ == '__main__':
    station_selection()  # if standalone
