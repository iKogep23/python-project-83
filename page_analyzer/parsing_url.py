#!/usr/bin/env python3


from bs4 import BeautifulSoup
import requests


def parsing_url(name):
    resp = requests.get(name, timeout=3)
    soup = BeautifulSoup(resp.text, 'html.parser')
    url_h1 = soup.h1.string if soup.h1 else ''
    url_title = soup.title.string if soup.title else ''
    res = soup.find('meta', {'name': 'description'})
    url_description = res.get('content') if res else ''
    return url_h1, url_title, url_description
