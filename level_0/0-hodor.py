import requests

l0url = "http://158.69.76.135/level0.php"

for i in range(1024):

     requests.post(
     	l0url, 
     	data = {'id':'390', 'holdthedoor':'Submit'}
 	)
