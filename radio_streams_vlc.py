#! /snap/bin/pypy3
'''`radio_streams_vlc` displays a list of Internet radio stations along with
numbers for users to make selections. Press "h" for help.'''
from os import chdir
from csv import reader
from subprocess import run

def station_selection():
    '''`station_selection()` method displays a list of Internet radio stations
from a CSV database, and prompts the user make a selection.'''
    chdir('/home/foo/scripts/radio_streams_vlc/')  # helps to find txt files
    cyan = '\x1b[38;2;72;201;176m'  # format text RGB: 72, 201, 176
    yelo = '\x1b[38;2;244;208;63m'
    orng = '\x1b[38;2;220;118;51m'
    reset = '\x1b[0m'  # reset to default
    urls = {}  # number selection: station URL

    with open('ascii_radio.txt', 'r') as ascii_art:
        [print(f'{cyan}{line[:-1]}{reset}') for line in ascii_art]  # ASCII art

    with open('stations.csv', 'r') as _file:
        _reader = reader(_file)  # csv reader object
        for number, record in enumerate(_reader, 1):
            print(f'{cyan}{number:>2}{reset}  {yelo}{record[0]:}{reset}  \
{orng}{record[1]}{reset}')  # print radio station list
            urls[number] = record[2]  # append number with URL to dictionary

    station_num = int(input('Enter station number: '))  # input station number

    # pass CLI args to VLC media player, including radion station URL
    run(['/snap/bin/vlc', '--intf', 'ncurses', urls[station_num]], check=True)


if __name__ == '__main__':
    station_selection()
