import splunk.Intersplunk as s
import requests
from requests.auth import HTTPBasicAuth

# Define the URL and authentication details
url = "https://localhost:8089/services/server/control/restart"
username = "admin"
password = "admin143"

# Send the POST request
response = requests.post(url, auth=HTTPBasicAuth(username, password), verify=False)

# Check the response
if response.status_code == 200:
    s.outputResults([{"data":"Server restart initiated successfully."}])
else:
     s.generateErrorResults([{"data":"Failed to restart the se"}])

