# -*- coding: utf-8 -*-

from datetime import date
from os import makedirs
import requests
from time import sleep
import json

def main():
    with open('./config.txt', 'r') as r:
        for line in r:
            if line.find('apikey') >= 0:
                apikey = line.strip().replace('apikey=', '')

    params = {'api-key': apikey}

    if apikey is None:
        print('apiky is not given in config.txt.')
        exit()

    #'https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key=yourkey'
    base_url = 'https://api.nytimes.com/svc/archive/v1/'

    path_head = './storage/raw_data/articles'

    this_year = date.today().year
    this_month = date.today().month
    first_year = 1851
    year_range = this_year - first_year + 1

    for i in range(year_range):
        year = first_year + i

        makedirs(f'{path_head}/{year}', exist_ok=True)

        for month in range(1, 13):
            if year >= this_year and month > this_month:
                break
            print(f'{year}-{month}')


            with open(f'{path_head}/{year}/{month}.json', 'r') as r:
                js_obj = json.load(r)

                if 'fault' not in js_obj:
                    print('passed')
                    continue

            url = f'{base_url}{year}/{month}.json'
            r = requests.get(url, params=params)

            with open(f'{path_head}/{year}/{month}.json', 'w') as w:
                w.write(r.text)

            sleep(6)


if __name__ == "__main__":
    main()
