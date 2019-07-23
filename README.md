# Cpython Pull Requests

## What does Cpython Pull Requests do?
Cpython Pull Requests (formerly pulls) is a Flask app to find the PRs opened against a given file in the [cpython](https://github.com/python/cpython/) repository. This is where contributors can find work to do and core developers can look for stale PRs that might be awaiting their review.   
Take a test drive at [cpython-pulls.herokuapp.com](https://cpython-pulls.herokuapp.com)

## Features
* Uses [GitHub's GraphQL API](https://developer.github.com/v4/guides/intro-to-graphql/)  
  (So we are fast! ~26 seconds for one request)
* Refreshes data every 5 minutes  
  (We all love fresh data. Yum!)
* Consistent URLs  
  (For each search your URL gets updated to something like: [cpython-pulls.herokuapp.com?files=pythonrun](https://cpython-pulls.herokuapp.com?files=pythonrun))
* Search for multiple files at once  
  (A URL like [cpython-pulls.herokuapp.com?files=travis,coverage](https://cpython-pulls.herokuapp.com?files=travis,coverage) will show you PRs opened for files matching `travis` OR `coverage`)
* Case insensitive search  
  (No more straining your pinky for that shift ⌨)

## Setup
### Generating Personal access token
You need to create a personal access token at [https://github.com/settings/tokens](https://github.com/settings/tokens) of your GitHub account. The token doesn't need to have any particular scope. The default public access works fine.  
**NOTE**: This token will be used via `GH_AUTH` environment variable.

### Local setup
* `pip install -r requirements.txt`
* Edit `.env.sample` and save it as `.env`
* `FLASK_APP=views.py flask run`  
   You can also do:  
   `export FLASK_APP=views.py`  
   `flask run`
* Wait... ⌛ (~26 Sec)
* Hurry to [127.0.0.1:5000](127.0.0.1:5000)!

### Heroku setup
* Go to [Heroku dashboard](https://dashboard.heroku.com/new-app) and create a new app. 
* Connect to GitHub or push directly to heroku remote.
* Go to `Settings -> Config Vars` and add `GH_AUTH` as your key, and your access token as value.
* Now, as soon as you push, you're live!  
  (Well not so soon. Deploying will take around ~26 seconds to fetch data for the first time)

## Contributors
Head to [CONTRIBUTORS.txt](CONTRIBUTORS.txt) to see the list of all the awesome contributors.


![Pulls-Screenshot](static/images/sample.gif)

:-)
