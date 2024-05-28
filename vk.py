import sys
import json

import requests


class API:

    api_expand_url = 'https://api.vk.ru/method/utils.checkLink'
    api_get_shorten_url = 'https://api.vk.ru/method/utils.getShortLink'
    api_get_link_info = 'https://api.vk.ru/method/utils.getLinkStats'
    header_api_key = None

    def __init__(self, apiKey):
        self.header_api_key = {'Authorization': f'Bearer {apiKey}'}
        return

    def check_out_response(self, response):
        try:
            response.raise_for_status()
            if not (response.status_code == 200
                    and not ('error' in json.loads(response.text))):
                raise requests.exceptions.HTTPError
        except requests.exceptions.HTTPError:
            print('Response error')
            print("Status Code: " + str(response.status_code))
            print(json.loads(response.text)['error']['error_msg'])
            sys.exit()
        return

    def url_click_info(self, key):
        print('Trying to get link info..')
        response = requests.post(
                            self.api_get_link_info,
                            headers=self.header_api_key,
                            params={"key": key, 'v': '5.236'}
                            )
        self.check_out_response(response)
        response_json = json.loads(response.text)
        if ('stats' in response_json['response']
                and response_json['response']['stats'] != []):
            response_json = response_json['response']['stats']
            views_count = 0
            for i in response_json:
                views_count += i['views']
            print(f'Views count of vk.cc/{key} = {views_count}')
        else:
            print('No stats for now')
        return

    def shorten_url(self, url):
        print('Trying to shorten your url..')
        response = requests.post(
                            self.api_get_shorten_url,
                            headers=self.header_api_key,
                            params={"url": url, 'v': '5.236'}
                            )
        self.check_out_response(response)
        shortened_link = json.loads(response.text)['response']['short_url']
        print(f'Shortened link for {url} is {shortened_link}')
        return

    def expand_url(self, url):
        print('Trying to get source url..')
        response = requests.post(
                            self.api_expand_url,
                            headers=self.header_api_key,
                            params={"url": url, 'v': '5.236'}
                            )
        self.check_out_response(response)
        expanded_link = json.loads(response.text)['response']['link']
        print(f'Source link for {url} is {expanded_link}')
        return
