import requests
import splunk.Intersplunk as si
def get_public_ip():
    # Get public IP using ipify
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        return response.json()['ip']
    else:
        return None

def get_location_by_ip(ip_address, access_key):
    # Use the ipstack API to get location information
    url = f'https://api.ipstack.com/{ip_address}?access_key={access_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Organize data in list of dictionaries format
        location_data = {
            "IP": data.get("ip"),
            "Country": data.get("country_name"),
            "Country Code": data.get("country_code"),
            "Region": data.get("region_name"),
            "Region Code": data.get("region_code"),
            "City": data.get("city"),
            "ZIP Code": data.get("zip"),
            "Latitude": data.get("latitude"),
            "Longitude": data.get("longitude"),
            "Connection Type": data.get("connection_type")
        }
        return location_data
    else:
        return None

access_key = 'd8f34f18ec8e45b6209bedeed5fadc43'
public_ip = get_public_ip()
if public_ip:
    location_info = get_location_by_ip(public_ip, access_key)
    si.outputResults([location_info])
