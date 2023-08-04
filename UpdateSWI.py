import requests
import json

##Site WAN Update to set bandwidth 100/100


Tenant="Enter Tenant ID"
SiteID="Enter Site ID"
WANInterface="Enter WAN Interface ID"
Authtoken="Enter Auth token"

url = "https://api.elcapitan.cloudgenix.com/v2.7/api/tenants/{}/sites/{}/waninterfaces/{}".format(Tenant, SiteID, WANInterface)

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-auth-token': AUTHToken
}

####Get the WAN Interface Config
GET_WAN_INT_CONFIG = requests.request("GET", url, headers=headers)

###Convert to DICTIONARY
Jsonformatted = GET_WAN_INT_CONFIG.json()

###Add changed value
WANInterfaceUpdate = {'link_bw_up': 100.0, 'link_bw_down': 100.0}
Jsonformatted.update(WANInterfaceUpdate)

##Format back to type to import back in
Serialized_JSON_DATA = json.dumps(Jsonformatted)


##PUTTING DATA BACK
response = requests.request("PUT", url, headers=headers, data=Serialized_JSON_DATA)

print(response.text)
