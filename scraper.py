#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import datetime
import json
import time


def get_line(text, option):
    
    solar = 'Position of the Sun: Subsolar Point'
    lunar = 'Position of the Moon: Sublunar Point'
    choice = solar if option == 'solar' else lunar
    
    start_index = text.find(choice) + len(choice) + 5
    end_index = text.find('</p>', start_index)
    temp = text[start_index:end_index]
    
    remove_these = [
        '<p>', '<tr>', '</tr>', '<td class=r>', '</td>', '<td>', '&nbsp;'
    ]
    
    for elem in remove_these:
        temp = temp.replace(elem, '')
    
    return temp.lower()


def get_datetime(text):
    
    start_index = text.find(',') + 2
    end_index = text.find('utc') - 1
    temp = text[start_index:end_index]
    fmt = '%B %d, %Y at %H:%M:%S'
    
    return tuple(str(datetime.datetime.strptime(temp, fmt)).split())


def get_coord(text):
    
    start_index_lat = text.find('e:') + 3
    end_index_lat = text.find("'", start_index_lat)
    temp_lat = text[start_index_lat:end_index_lat]
    degree_lat, minute_lat = temp_lat.split('°')
    dd_lat = round(int(degree_lat) + (int(minute_lat) / 60), 4)
    
    start_index_long = text.find('e:', end_index_lat) + 3
    end_index_long = text.find("'", start_index_long)
    temp_long = text[start_index_long:end_index_long]
    degree_long, minute_long = temp_long.split('°')
    dd_long = round(int(degree_long) + (int(minute_long) / 60), 4)
    
    return dd_lat, dd_long # dd = decimal degrees


def make_json(solar_datetime, solar_coord, lunar_datetime, lunar_coord):
    
    data = {
        "sun": {
            "date": solar_datetime[0],
            "time": solar_datetime[1],
            "latitude": solar_coord[0],
            "longitude": solar_coord[1],
        },
        "moon": {
            "date": lunar_datetime[0],
            "time": lunar_datetime[1],
            "latitude": lunar_coord[0],
            "longitude": lunar_coord[1],
        }
    }
    
    return json.dumps(data)


def run_bot():
    
    URL = 'https://www.timeanddate.com/worldclock/sunearth.html'
    SCRAPE_INTERVAL = 600 # 600 seconds or 10 minutes
    
    while True:

        page = requests.get(URL).text
        
        solar_line = get_line(page, 'solar')
        lunar_line = get_line(page, 'lunar')
        
        solar_datetime = get_datetime(solar_line)
        lunar_datetime = get_datetime(lunar_line)
        
        solar_coord = get_coord(solar_line)
        lunar_coord = get_coord(lunar_line)
        
        data = make_json(solar_datetime, solar_coord, lunar_datetime, lunar_coord)
        
        # TODO: send data to database
        print(data)
        
        time.sleep(SCRAPE_INTERVAL)
        

run_bot()