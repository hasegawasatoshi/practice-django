import requests
import json
import pprint

url = "http://localhost:8000/sensor/"

serial_number = 'BMTL-123456'
display_name1 = 'テスト機'
display_name2 = u'テスト機（改）'


headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


# Create a new sensor
print('## Create a new sensor')
response = requests.request(
    "POST", url, headers=headers, data=json.dumps({
        'serial_number': serial_number,
        'display_name': display_name1
    }))
print(f'Status Code = {response.status_code}')
pprint.pprint(response.json())
print('')

# Get a list of sensors
print('## Create a sensor list')
response = requests.request("GET", url, headers=headers)
print(f'Status Code = {response.status_code}')
pprint.pprint(response.json())
print('')

# Get sensor details
print('## Create sensor details')
response = requests.request("GET", url + serial_number, headers=headers)
print(f'Status Code = {response.status_code}')
pprint.pprint(response.json())
print('')

# Update sensor details
print('## Update the sensor details')
response = requests.request(
    "PUT", url + serial_number, headers=headers, data=json.dumps({
        'serial_number': serial_number,
        'display_name': display_name2
    }))
print(f'Status Code = {response.status_code}')
pprint.pprint(response.json())
print('')

# delete the sensor
print('## Delete the sensor')
response = requests.request("DELETE", url + serial_number, headers=headers)
print(f'Status Code = {response.status_code}')
pprint.pprint(response.text)
print('')
