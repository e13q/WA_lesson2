import os

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


api_expand_url = 'https://api.vk.ru/method/utils.checkLink'
api_get_shorten_url = 'https://api.vk.ru/method/utils.getShortLink'
api_get_link_info = 'https://api.vk.ru/method/utils.getLinkStats'
header_api_key = None


def get_url_views_count(key, header_api_key):
    response = requests.post(
                        api_get_link_info,
                        headers=header_api_key,
                        params={"key": key, 'v': '5.236'}
                        )
    response.raise_for_status()
    response_json = response.json()
    if 'error' in response_json:
        raise requests.exceptions.RequestException
    if ('stats' in response_json['response']
            and response_json['response']['stats'] != []):
        response_json = response_json['response']['stats']
        views_count = 0
        for i in response_json:
            views_count += i['views']
        return views_count
    return None


def shorten_url(url, header_api_key):
    response = requests.post(
                        api_get_shorten_url,
                        headers=header_api_key,
                        params={"url": url, 'v': '5.236'}
                        )
    response.raise_for_status()
    shortened_link = response.json()
    if 'error' in shortened_link:
        raise requests.exceptions.RequestException
    return shortened_link['response']['short_url']


def is_shorten_link(url):
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'vk.cc':
        return True
    else:
        return False


if __name__ == '__main__':
    load_dotenv()
    header_api_key = {'Authorization': f'Bearer {os.environ['API_KEY']}'}
    print('Input your link')
    url = input()
    if is_shorten_link(url):
        print('Trying to get link info..')
        parsed_url = urlparse(url)
        key = parsed_url.path[1:]
        try:
            url_views_count = get_url_views_count(key, header_api_key)
            if url_views_count is None:
                print('No stats for now')
            else:
                print(f'Views count of vk.cc/{key} = {url_views_count}')
        except requests.exceptions.RequestException:
            print('Request error. Is this is a correct shorten url?')
    else:
        print('Trying to shorten your url..')
        try:
            shortened_link = shorten_url(url, header_api_key)
            print(f'Shortened link for {url} is {shortened_link}')
        except requests.exceptions.RequestException:
            print('Request error. Is this is a correct url?')
