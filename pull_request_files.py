import json
import os
import re

import requests



pulls_url = 'https://api.github.com/repos/python/cpython/pulls'
query = 'page=1&per_page=100'
oauth_token = os.environ.get("GH_AUTH")
# payload = {'page': 1, 'per_page': 100}

def _parse_header_link(headers):
    headers_link = headers.get('link').split(', ')
    links = {}
    prog = re.compile(r'<(?P<url>.*?)>; rel="(?P<rel>\w+)"')
    for link in headers_link:
        g = re.match(prog, link)
        links[g['rel']] = g['url']
    return links


def retrieve_open_issues(pulls_url):
    open_pull_requests = {}
    while True:
        response = requests.get(pulls_url, auth=('csabella', oauth_token))
        links = _parse_header_link(response.headers)
        for issue in response.json():
            open_pull_requests[issue['number']] = issue
        if 'next' not in links:
            break
        pulls_url = links['next']
    return open_pull_requests


def get_files(issues):
    for pr in issues.keys():
        response = requests.get(f"{pulls_url}/{pr}/files" + '?', auth=('csabella', oauth_token))
        issues[pr]['files'] = response.json()
    return issues


with open('pull_requests.json', 'w') as outfile:
    json.dump(get_files(retrieve_open_issues(pulls_url + '?' + query)), outfile)
