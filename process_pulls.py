import json
from collections import defaultdict

with open('pull_requests.json', 'r') as input_file:
    pulls = json.load(input_file)


def pr_by_file():
    files = defaultdict(set)
    for pr in pulls:
        for file in pr['files']['nodes']:
            filename = file['path']
            files[filename].add(pr['number'])
    return files


def change_values_to_list():
    files = pr_by_file()
    for filename, pr in files.items():
        files[filename] = list(pr)
    files = dict(sorted(files.items()))
    with open('pr_files.json', 'w') as outfile:
        return json.dump(files, outfile)


if __name__ == "__main__":
    change_values_to_list()
