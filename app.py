import pickle

from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")
model = pickle.load(open("model.pkl", 'rb'))


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # first 3 rows
    gender = request.form.get('gender')
    if gender=='Male':
        gender=0
    else:
        gender=1
    guardian = request.form.get('guardian')
    if guardian=="Mother":
        guardian=0
    elif guardian=="Father":
        guardian=1
    else:
        guardian=2
    famsup = request.form.get('Famsup')
    if famsup=="Yes":
        famsup=0
    else:
        famsup=1

    # second 3 rows
    paid = request.form.get('Paid')
    if paid=="Yes":
        paid=0
    else:
        paid=1
    activity = request.form.get('Activity')
    if activity=="Yes":
        activity=0
    else:
        activity=1
    internet = request.form.get('Internet')
    if internet=="Yes":
        internet=0
    else:
        internet=1


    # third 3 rows
    medu = request.form.get('Medu')
    if medu=="None":
        medu=0
    elif medu=="Primary":
        medu=1
    elif medu=="Secondary":
        medu=2
    else:
        medu=3
    studytime = request.form.get('Study-time')

    failure = request.form.get('Failure')

    # fourth 3 rows
    go = request.form.get('Go-out')
    if go=="Very Low":
        go=0
    elif go=="Low":
        go=1
    elif go=="Medium":
        go=2
    elif go=="High":
        go=3
    else:
        go=4
    absent = request.form.get('Absences')
    health = request.form.get('Health')
    if health=="Very-Bad":
        health=0
    elif health=="Bad":
        health=1
    elif health=="Good":
        health=3
    else:
        health=4

    # Fifth 3 rows
    sem1 = request.form.get('sem1')
    sem2 = request.form.get('sem2')

    vect = [gender, guardian, famsup, paid, activity,health,go, internet, medu, int(studytime), int(failure),
            int(absent),int(sem1), int(sem2)]
    pred = model.predict([vect])

    return render_template("result.html", val = pred)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
