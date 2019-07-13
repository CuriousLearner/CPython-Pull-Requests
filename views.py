from flask import Flask, render_template
import pull_request_files
from apscheduler.schedulers.background import BackgroundScheduler

pr_data = pull_request_files.main()


def timed_job():
    global pr_data
    pr_data = pull_request_files.main()


scheduler = BackgroundScheduler()
scheduler.add_job(timed_job, 'interval', minutes=5)
scheduler.start()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'very-hard-to-guess-key'


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', results=pr_data)


if __name__ == '__main__':
    app.run(debug=True)
