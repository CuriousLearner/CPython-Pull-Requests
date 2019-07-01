from dotenv import load_dotenv, find_dotenv
import json
from inspect import cleandoc
import os
import requests
import process_pulls

load_dotenv(find_dotenv())
url = 'https://api.github.com/graphql'
oauth_token = os.environ.get("GH_AUTH")
headers = {'Authorization': f'bearer {oauth_token}'}


def get_pull_request_details(endCursor=None):
    graphql_query = '''query($previousEndCursor:String) {
                         repository(owner:"python", name:"cpython") {
                           pullRequests(states: OPEN, first: 100, after: $previousEndCursor) {
                               nodes {
                                 title
                                 number
                                 files(first: 100) {
                                   nodes{
                                     path
                                   }
                                 }
                               }
                               pageInfo {
                                 endCursor
                                 hasNextPage
                               }
                               totalCount
                           }
                         }
                       }
                       '''
    github_query = {}
    github_query["query"] = cleandoc(graphql_query)
    if endCursor is not None:
        query_variables = f'''{{
                                "previousEndCursor": "{endCursor}"
                           }}
                           '''
        github_query["variables"] = cleandoc(query_variables)
    github_query = json.dumps(github_query)
    response = requests.post(url, data=github_query, headers=headers)
    response.raise_for_status()
    response = json.loads(response.content)
    if 'errors' in response:
        for error in response['errors']:
            print(error['message'])
        exit()
    return response


def main():
    page = 1
    print(f'[*] Fetching page {page}')
    response = get_pull_request_details()
    pull_requests = response['data']['repository']['pullRequests']['nodes']
    print(f'[✓] Fetched page {page} ')
    while response['data']['repository']['pullRequests']['pageInfo']['hasNextPage']:
        page = page + 1
        print(f'[*] Fetching page {page}')
        response = get_pull_request_details(response['data']['repository']['pullRequests']['pageInfo']['endCursor'])
        print(f'[✓] Fetched page {page} ')
        pull_requests = pull_requests + response['data']['repository']['pullRequests']['nodes']

    print('Getting PR by files')
    files = process_pulls.main(pull_requests)
    print('Done!')
    return files


if __name__ == "__main__":
    main()
