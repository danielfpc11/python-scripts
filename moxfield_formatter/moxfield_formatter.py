import json
import os
import time

moxfield_formatter_path = 'moxfield_formatter'

def load_json(path):
    with open(path) as json_file:
        return json.load(json_file)['data']

def process_pages(pages_path):
    merged_pages = sum(list(map(lambda filename: load_json(f'{pages_path}/{filename}'), os.listdir(pages_path))), [])
    with open(f'{moxfield_formatter_path}/output/output-{round(time.time() * 1000)}.json', 'w') as output:
        json.dump({'data': merged_pages}, output)

process_pages(f'{moxfield_formatter_path}/pages')