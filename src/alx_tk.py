import requests

def get_req(target):
	resp = requests.get(target)
	return resp

def headerss(target):
	test =  []
	resp = requests.get(target)
	for key , value in resp.headers.items():
	    a = key + value
	    test.append(a)
	return test
def gb(target):
	res = requests.get(target)
	return res.text
#target = "https://www.google.com"
#print header(target)