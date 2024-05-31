import os

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def get_url_views_count(key, auth_header):
    response = requests.post(
                        'https://api.vk.ru/method/utils.getLinkStats',
                        headers=auth_header,
                        params={"key": key, 'v': '5.236'}
                        )
    response.raise_for_status()
    response = response.json()
    if 'error' in response:
        raise requests.exceptions.RequestException
    if ('stats' in response['response']
            and response['response']['stats'] != []):
        timestamping_stats = response['response']['stats']
        views_count = 0
        for timestamped_stats in timestamping_stats:
            views_count += timestamped_stats['views']
        return views_count
    return None


def shorten_url(url, auth_header):
    response = requests.post(
                        'https://api.vk.ru/method/utils.getShortLink',
                        headers=auth_header,
                        params={"url": url, 'v': '5.236'}
                        )
    response.raise_for_status()
    response = response.json()
    if 'error' in response:
        raise requests.exceptions.RequestException
    return response['response']['short_url']


def is_shorten_link(url):
    parsed_url = urlparse(url)
    return parsed_url.hostname == 'vk.cc'


if __name__ == '__main__':
    load_dotenv()
    auth_header = {'Authorization':
                   f'Bearer {os.environ['VK_SERVICE_ACCESS_KEY']}'}
    url = input('Input your link\n')
    if is_shorten_link(url):
        print('Trying to get link info..')
        parsed_url = urlparse(url)
        key = parsed_url.path[1:]
        try:
            url_views_count = get_url_views_count(key, auth_header)
            if url_views_count is None:
                print('No stats for now')
            else:
                print(f'Views count of vk.cc/{key} = {url_views_count}')
        except requests.exceptions.RequestException:
            print('Request error. Is this is a correct shorten url?')
    else:
        print('Trying to shorten your url..')
        try:
            shortened_link = shorten_url(url, auth_header)
            print(f'Shortened link for {url} is {shortened_link}')
        except requests.exceptions.RequestException:
            print('Request error. Is this is a correct url?')
