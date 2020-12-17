import flask
import requests
from stats_calculator import stats_calculator

app = flask.Flask(__name__)

@app.route('/')
def index():
     return flask.render_template(
        "chart.html",
    )

@app.route('/chart/dataset', methods=["GET"])
def form_edit_get():
    lst = [5, 5, 3, 4, 8, 7, 10]
    mean = stats_calculator().mean(lst)
    median = stats_calculator().median(lst)
    mode = stats_calculator().mode(lst)
    print(mean)
    print(median)
    print(mode)
    return {'mean': mean, 'median': median, 'mode': mode}

if __name__ == '__main__':
    app.run()