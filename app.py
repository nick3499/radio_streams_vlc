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
    '''Select and play selected station.'''
    # hash table of numbers associated with URLs
    URLS = station_list.URLS
    # input station selection number
    yellow = '\x1b[1;7;38;2;244;208;63m'
    reset = '\x1b[0m'
    radio = '\U0001F4FB'
    station_num = int(input(f'\n{radio} {yellow} Enter station number {reset}: '))
    print('')
    # ===  MPV  ===
    run(['/bin/mpv', '--no-video', URLS[station_num]], check=True)
    # ===  VLC  ===
    # run(['/usr/bin/vlc', '--intf', 'ncurses', URLS[station_num]], check=True)
    # run(['/usr/bin/vlc', '--audio', '-I', 'qt', URLS[station_num]], check=True)
    # ===  MPG123  ===
    # run(['/usr/bin/mpg123', '--cpu', 'x86-64', '-v', '--title', 
    #      '--long-tag', URLS[station_num]], check=True)
    # ===
    # callback
    station_selection()


if __name__ == '__main__':
    station_selection()
