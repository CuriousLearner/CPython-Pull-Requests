# pulls
Get Files for all open Pull Requests

Basic code to query Github and get the open PRs by file name.

If you want to look at the code that fetches and processes the data:
`pull_request_files.py` creates a list of dictionaries containing title, number and files of a PR.  You need to create a 
personal access token at settings/Developer settings of your github account. The token doesn't need to have any
scope. The default public access works fine.

`process_pulls.py` The main function returns file names and all the pull requests for that file. It uses the list of
dictionaries returned by `pull_request_files.py

`views.py` Aside from the flask code, it also contains code for APScheduler. It updates the `files` variable in the background
at specific intervals.

:-)
