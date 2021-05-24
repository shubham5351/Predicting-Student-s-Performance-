import pickle

from flask import Flask

app = Flask(__name__, template_folder="templates")
model = pickle.load(open("model.pkl", 'rb'))


@app.route("/")
def index():
    return "<h1 align='center'>Student prediction system<h1>"


@app.route("/predict")
def predict():
    return "<h1 align='center'>Prediction<h1>"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
