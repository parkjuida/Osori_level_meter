import requests
import json

list_osori_repo_url = 'https://api.github.com/orgs/HyOsori/repos?access_token=6a49e18d2cf83edf2d8717b42517fccec77d1e6f'
# params = {'key1': 'value1', 'key2': 'value2'}

# GET
response = requests.get(list_osori_repo_url)
repo_infos = json.loads(response.text)
# Response, status etc

# print(response.status_code)
# print("================================================")
# print(repo_infos)

# GET with params in URL
# r = requests.get(url, params=params)

# POST with form-encoded data
# r = requests.post(url, data=params)

# POST with JSON
# import json
# r = requests.post(url, data=json.dumps(payload))

commit_counts = {'name': 1}

print("총 Repository 개수 : %d" % len(repo_infos))

for repo_info in repo_infos:
    try:
        print(repo_info['name'])
    except:
        continue

    contribute_info_url = "https://api.github.com/repos/HyOsori/%s/contributors?access_token=6a49e18d2cf83edf2d8717b42517fccec77d1e6f" % repo_info['name']
    response = requests.get(contribute_info_url)

    contribute_infos = json.loads(response.text)
    for contribute_info in contribute_infos:
        try:
            commit_counts[contribute_info['login']] += contribute_info['contributions']
            # print(contribute_info['login'])
            # print(contribute_info['contributions'])
        except:
            try:
                commit_counts.update({contribute_info['login']: contribute_info['contributions']})
            except:
                continue

for id in commit_counts:
    print(id + ":" + str(commit_counts[id]))
