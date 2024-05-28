import os

from dotenv import load_dotenv
from urllib.parse import urlparse

import vk


if __name__ == '__main__':
    load_dotenv()
    user = vk.API(os.environ['API_KEY'])
    print('Input your link')
    url = input()
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'vk.cc':
        user.url_click_info(parsed_url.path[1:])
        user.expand_url(url)
    else:
        user.shorten_url(url)
