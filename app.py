#!/bin/python3
'''Play internet radio selection in media player.'''
from subprocess import run
from ascii_art import get_ascii_art
import station_list

# dump ASCII art header
print(get_ascii_art())
# dump station list
station_list.get_station_list()


def station_selection():
    '''Play selected station.'''
    # obj: number/station name/genres/url
    URLS = station_list.URLS
    # station number selection input
    station_num = int(input('\x1b[38;2;72;201;176mEnter station number\
\x1b[0m: '))
    # ===  VLC  ===
    # run(['/usr/bin/vlc', '--intf', 'ncurses', URLS[station_num]], check=True)
    # run(['/usr/bin/vlc', '--audio', '-I', 'qt', URLS[station_num]], check=True)
    # ===  mpv  ===
    run(['/usr/bin/mpv', URLS[station_num]], check=True)
    # ===
    # color-themed logo
    c_1 = '\x1b[38;2;220;118;51m'
    c_2 = '\x1b[38;2;244;208;63m'
    res = '\x1b[0m'
    print(f'{c_1}+~+~+~+~+~+~+~+~+~+~+~+~+~+{res}')
    print(f'{c_1}<{c_2}R{c_1}|{c_2}A{c_1}|{c_2}D{c_1}|{c_2}I{c_1}|{c_2}O{c_1}>\
{c_2} {c_1}<{c_2}S{c_1}|{c_2}T{c_1}|{c_2}R{c_1}|{c_2}E{c_1}|{c_2}A{c_1}|{c_2}M\
{c_1}|{c_2}S{c_1}>{res}')
    print(f'{c_1}+~+~+~+~+~+~+~+~+~+~+~+~+~+{res}')
    # callback
    station_selection()


if __name__ == '__main__':
    station_selection()
