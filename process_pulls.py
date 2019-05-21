
import json
from collections import defaultdict
from pprint import pprint

with open('pull_requests.json', 'r') as input_file:
    pulls = json.load(input_file)

def pr_by_file():
    files = defaultdict(set)
    for pr, values in pulls.items():
        for file in values['files']:
            filename = file['filename']
            files[filename].add(pr)
    return files

# pprint(pr_by_file())

def change_values_to_list():
    files = pr_by_file()
    for filename, pr in files.items():
        files[filename]=list(pr)
    files = dict(sorted(files.items()))
    with open('test_with.json', 'w') as outfile:
        return json.dump(files, outfile)

if __name__ == "__main__":
    change_values_to_list()
