#!/bin/python3
'''Generate M3U8 playlist from CSV database.'''
from csv import reader


def gen_m3u8():
    '''Generate playlist.'''
    # open CSV database
    with open('stations.csv') as csv_file:
        # CSV reader object
        csv_read = reader(csv_file)
        # print playlist designation
        print('#EXTM3U')
        # iterate through names, genre lists and urls of CSV database
        for name, genres, url in csv_read:
            # print first line of playlist item info
            print(f'#EXTINF:-1,{name}——{genres}')
            # print second line
            print(url)


if __name__ == '__main__':
    gen_m3u8()