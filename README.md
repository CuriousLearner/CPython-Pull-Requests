# pulls
Get Files for all open Pull Requests

Basic code to query Github and get the open PRs by file name.

`files_to_pr_20190218.txt` is a mapping of the file names to pull request numbers as of 18 February 2019.
`files_to_pr_20190409.txt` is a mapping of the file names to pull request numbers as of 9 April 2019.

If you want to look at the source JSON or the code that made the JSON:

`pull_requests.json` is the output for the CPython repo as of 9 April 2019.
It might be easiest to work with this to avoid hitting Github.

`pull_request_files.py` creates the JSON.  You need to create a Github token to
not hit the rate limit.  This isn't optimized at all and may take several minutes
to run.

`process_pulls.py` prints the file names and all the pull requests for that file.
Of course the JSON may yield more interesting results than just this, but it's a
start.  :-)
