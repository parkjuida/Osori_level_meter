import requests
import json


def get_osori_commit_counts_all():

    list_osori_repo_url = 'https://api.github.com/orgs/HyOsori/repos?\
    access_token=6a49e18d2cf83edf2d8717b42517fccec77d1e6f'

    # GET
    response = requests.get(list_osori_repo_url)
    repo_infos = json.loads(response.text)

    commit_counts = {}

    print("총 Repository 개수 : %d" % len(repo_infos))

    for repo_info in repo_infos:
        try:
            print(repo_info['name'])
        except:
            continue

        contribute_info_url = "https://api.github.com/repos/HyOsori/%s/contributors?access_token=\
        6a49e18d2cf83edf2d8717b42517fccec77d1e6f" % repo_info['name']
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

    return commit_counts


def get_osori_commit_counts(id):

    list_osori_repo_url = 'https://api.github.com/users/%s/events?\
    access_token=6a49e18d2cf83edf2d8717b42517fccec77d1e6f' % id

    # params = {'key1': 'value1', 'key2': 'value2'}

    # GET
    response = requests.get(list_osori_repo_url)
    event_infos = json.loads(response.text)

    commit_counts = 0

    print("총 Event 개수 : %d" % len(event_infos))

    for event in event_infos:
        try:
            print(event['name'])
        except:
            continue

        contribute_info_url = "https://api.github.com/repos/HyOsori/%s/contributors?access_token=\
        6a49e18d2cf83edf2d8717b42517fccec77d1e6f" % repo_info['name']
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

    return commit_counts

