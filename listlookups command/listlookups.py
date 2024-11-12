
try:
    import requests
    from requests.auth import HTTPBasicAuth
    import splunk.Intersplunk as si

    url = "https://localhost:8089/services/data/lookup-table-files?output_mode=json"
    auth = HTTPBasicAuth('admin', 'admin143')

    response = requests.get(url, auth=auth, verify=False)
    lookup_tables_info = []
    for entry in response.json().get('entry', []):
        table_info = {
            'name': entry.get('name'),
            'id': entry.get('id'),
            'updated': entry.get('updated'),
            'author': entry.get('author'),
            'path': entry.get('content', {}).get('eai:data'),
            'disabled': entry.get('content', {}).get('disabled', False),
            'permissions': entry.get('acl', {}).get('perms', {}),
            'sharing': entry.get('acl', {}).get('sharing', 'N/A')
        }
        lookup_tables_info.append(table_info)


    si.outputResults(lookup_tables_info)
except Exception as e:
    si.generateErrorResults([{"data":e}])
