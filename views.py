from flask import Flask, render_template
import pull_request_files
from apscheduler.schedulers.background import BackgroundScheduler

files = pull_request_files.main()


def timed_job():
    global files
    files = pull_request_files.main()


scheduler = BackgroundScheduler()
scheduler.add_job(timed_job, 'interval', minutes=1)
scheduler.start()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'very-hard-to-guess-key'


@app.route("/")
@app.route("/index")
def index():
    results = files

    final_results = dict()
    for file_name in results.keys():
        if not file_name.startswith('Misc'):
            final_results[file_name] = results[file_name]
    return render_template('index.html', results=final_results)


if __name__ == '__main__':
    app.run(debug=True)
