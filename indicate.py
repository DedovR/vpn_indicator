# https://github.com/limpbrains/somebar
# https://github.com/philipbl/pyAnyBar
# https://github.com/tonsky/AnyBar

from anybar import AnyBar
from requests import get
import json
import os
import time

external_ip = ""
any_bar_port = 11111
delay = 60

def init_somebar():
    cmd = 'nohup somebar -p' + str(any_bar_port) + ' &'
    os.system(cmd)

def get_ip():
    response = get('https://api.ipify.org?format=json').text
    parsed_json = json.loads(response)
    return parsed_json["ip"]

def main():
    init_somebar()

    while True:
        ip = get_ip()
        if external_ip == ip:
            AnyBar(port=any_bar_port).change('green')
        else:
            AnyBar(port=any_bar_port).change('exclamation')

        time.sleep(delay)

main()


