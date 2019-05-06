import json
from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'very-hard-to-guess-key'


@app.route("/")
@app.route("/index")
def index():
    with open('files_to_pr.txt', 'rb') as files_to_pr:
        # results = json.loads(json.dumps(files_to_pr.read()))
        results = json.loads(files_to_pr.read())
    final_results = dict()
    import ipdb; ipdb.set_trace()
    for file_name in results.keys():
        if not file_name.startswith('Misc'):
            final_results[file_name] = results[file_name]
    return render_template('index.html', results=final_results)


if __name__ == '__main__':
    app.run(debug=True)
