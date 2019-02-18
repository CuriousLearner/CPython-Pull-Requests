
import json
from collections import defaultdict
from pprint import pprint

with open('pull_requests.json', 'r') as input_file:
    pulls = json.load(input_file)

file_to_pr = defaultdict(set)
for pr, values in pulls.items():
    for file in values['files']:
        filename = file['filename']
        file_to_pr[filename].add(pr)

