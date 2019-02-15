import requests

import json

controller='sandboxdnac.cisco.com'

def getnetworkdevicecount():
	
	url = "https://" + controller + "/api/v1/ticket"
	
	payload = {"username":"devnetuser","password":"Cisco123!"}

	
	header = {"content-type": "application/json"}

	response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)
	r_json=response.json()

	
	ticket = r_json["response"]["serviceTicket"]

	return ticket
