from collections import defaultdict


def pr_by_file(pull_requests):
    files = defaultdict(set)
    for pr in pull_requests:
        for file in pr['files']['nodes']:
            filename = file['path']
            files[filename].add(pr['number'])
    return files


def change_values_to_list(pull_requests):
    files = pr_by_file(pull_requests)
    for filename, pr in files.items():
        files[filename] = list(pr)
    files = dict(sorted(files.items()))
    return files


def main(pull_requests):
    return change_values_to_list(pull_requests)
