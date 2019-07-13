from collections import defaultdict


def get_files(pull_requests):
    files = defaultdict(set)
    for pr in pull_requests:
        for file in pr['files']['nodes']:
            filename = file['path']
            files[filename].add(pr['number'])
    for filename, pr in files.items():
        files[filename] = list(pr)
        files[filename].sort()
    files = dict(sorted(files.items()))
    results = dict()
    for file_name in files.keys():
        if not file_name.startswith('Misc'):
            results[file_name] = files[file_name]
    return results


def get_titles(pull_requests):
    pr_titles = dict()
    for pr in pull_requests:
        pr_titles.update({pr['number']: pr['title']})
    return pr_titles
