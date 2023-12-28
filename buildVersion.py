# v1.6: Added '-' to fix the wrong pipeline id

import requests
from requests.auth import HTTPBasicAuth
import json
import sys
import os

master_dict = {'1': {'art_url': 'https://p-gp2-artifactory.imovetv.com/ui/native/qt-local/SlingTV-Roku-CI-Phoenix/',
                     'device_name': 'Roku', 'player_name': 'SlingTV_Roku'},
               '2': {
                   'art_url': 'https://p-gp2-artifactory.imovetv.com/ui/native/react-native-sling-ui-app-gradle-local/release_common/',
                   'device_name': 'Amazon Fire TV', 'player_name': 'SlingTV_Android'},
               '3': {
                   'art_url': 'https://p-gp2-artifactory.imovetv.com/ui/native/react-native-sling-ui-app-gradle-local/LAT/samsung/',
                   'device_name': 'Samsung TV', 'player_name': 'SlingTV_Samsung'},
               '4': {
                   'art_url': 'https://p-gp2-artifactory.imovetv.com/ui/native/react-native-sling-ui-app-gradle-local/LAT/lg/hwa/',
                   'device_name': 'LG TV', 'player_name': 'SlingTV_LG'},
               '5': {
                   'art_url': 'https://p-gp2-artifactory.imovetv.com/ui/native/react-native-sling-ui-app-gradle-local/LAT/vizio/',
                   'device_name': 'Vizio TV', 'player_name': 'SlingTV_Vizio'},
               '6': {
                   'art_url': 'https://p-gp2-artifactory.imovetv.com/ui/native/react-native-sling-ui-app-gradle-local/LAT/xbox/',
                   'device_name': 'Xbox One', 'player_name': 'SlingTV_Xbox'},
               '7': {
                   'art_url': 'https://p-gp2-artifactory.imovetv.com/ui/native/react-native-sling-ui-app-gradle-local/LAT/comcast/',
                   'device_name': 'Linux STB', 'player_name': 'SlingTV_Comcast2'},
               '8': {
                   'art_url': 'https://p-gp2-artifactory.imovetv.com/ui/native/react-native-sling-ui-app-gradle-local/release_common/',
                   'device_name': 'Apple TV', 'player_name': 'SlingTV_tvOS'},
               '9': {
                   'art_url': 'https://p-gp2-artifactory.imovetv.com/ui/native/react-native-sling-ui-app-gradle-local/release_common/',
                   'device_name': 'Apple iPhone', 'player_name': 'SlingTV_iOS'},
               '10': {
                   'art_url': 'https://p-gp2-artifactory.imovetv.com/ui/native/react-native-sling-ui-app-gradle-local/release_common/',
                   'device_name': 'Android Phone', 'player_name': 'SlingTV_Android'},
               '11': {
                   'art_url': 'https://p-gp2-artifactory.imovetv.com/ui/native/react-native-sling-ui-app-gradle-local/release_common/',
                   'device_name': 'Android TV', 'player_name': 'SlingTV_Android', 'device_model': 'AirTV Mini'},
               }


def take_input():
    input_req = input('''Select platform index to get the latest version & artifactory URL:
    1 for Roku
    2 for Amazon
    3 for Samsung
    4 for LG
    5 for Vizio
    6 for Xbox
    7 for Comcast
    8 for Apple TV
    9 for Apple iPhone
    10 for Android Phone
    11 for AirTV Mini
    0 for EXIT

    ''')

    if input_req == '0':
        quit()
    else:
        print("Selected platform is", master_dict[input_req]['device_name'])
        query_artifactory_url(input_req)


def query_app_ver(index):
    if index == '11':
        url = "https://api.conviva.com/insights/3.0/metrics/unique-devices/group-by/dimension-tag/appVersion?granularity=P1D&device_name=%s&device_model=%s" % (
        (master_dict[index]['device_name']), (master_dict[index]['device_model']))
    else:
        url = "https://api.conviva.com/insights/3.0/metrics/unique-devices/group-by/dimension-tag/appVersion?granularity=P1D&device_name=%s&player_name=%s" % (
        (master_dict[index]['device_name']), (master_dict[index]['player_name']))

    auth = HTTPBasicAuth('XSsrZUdQ7QFWAJLGSv15jX', '5hoNiuUzA3G15JT4KVU3Bs6eipkmKtSSjkucwq2UdY9E')

    response = requests.get(url, auth=auth)
    # print (response)
    response_dict = response.json()
    pretty = json.dumps(response_dict, indent=4)
    # print (pretty)
    app_ver = response_dict['time_series'][0]['dimensional_data'][0]['dimension']['value']
    total_devices = int(response_dict['total']['unique_devices']['count'])
    picked_devices = int(response_dict['time_series'][0]['dimensional_data'][0]['metrics']['unique_devices']['count'])
    pick_per = round(((picked_devices / total_devices) * 100), 2)
    print("app version is: " + app_ver, "with unique devices: " + str(pick_per) + "%")

    if index == '6':
        return app_ver.replace('.70', '')
    elif (index == '2') and (len(app_ver) > 10):
        return app_ver[:6]
    else:
        return app_ver


def query_artifactory_url(index):
    if index == '2':
        url = ("Artifactory URL is: " + master_dict[index]['art_url']) + "%s" % (
                    str(query_pipelineId(index)) + "/Android/" + "\n")
        print(url)
        print("******************************************************************************")
        return take_input()
    elif index == '8':
        url = ("Artifactory URL is: " + master_dict[index]['art_url']) + "%s" % (
                    str(query_pipelineId(index)) + "/Apple/tvOS/ten-foot/" + "\n")
        print(url)
        print("******************************************************************************")
        return take_input()
    elif index == '9':
        url = ("Artifactory URL is: " + master_dict[index]['art_url']) + "%s" % (
                    str(query_pipelineId(index)) + "/Apple/iOS/mobile/" + "\n")
        print(url)
        print("******************************************************************************")
        return take_input()
    elif index == '10':
        url = ("Artifactory URL is: " + master_dict[index]['art_url']) + "%s" % (
                    str(query_pipelineId(index)) + "/Android/mobile/" + "\n")
        print(url)
        print("******************************************************************************")
        return take_input()
    elif index == '11':
        url = ("Artifactory URL is: " + master_dict[index]['art_url']) + "%s" % (
                    str(query_pipelineId(index)) + "/Android/" + "\n")
        print(url)
        print("******************************************************************************")
        return take_input()
    else:
        url = ("Artifactory URL is: " + master_dict[index]['art_url']) + "%s" % (str(query_app_ver(index)) + "\n")
        print(url)
        print("******************************************************************************")
        return take_input()


def query_pipelineId(index):  # This is specific for RNUI clients platforms
    token = 'glpat-xNZersi_yFmdcVUgyHro'
    header = {
        'Authorization': f'Bearer {token}'
    }

    payload = {
        'search': 'v',
    }

    app_ver = query_app_ver(index)
    print(app_ver)

    resp = requests.get("https://gitlab.com/api/v4/projects/25159562/repository/tags?search=v%s" % app_ver + '-',
                        headers=header, json=payload)
    # print(resp.status_code)
    response_dict = resp.json()
    pretty = json.dumps(response_dict, indent=4)
    # print (pretty)
    resp_name = response_dict[0]['name']
    # print (resp_name)
    pipeline_id = resp_name[-9:]
    # print (pipeline_id)
    return pipeline_id


take_input()
