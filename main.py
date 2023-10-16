import helper
from flask import Flask, request, Response, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")#Führt zu Index
def index():
    todos = helper.get_all()
    return render_template('index.html', todos=todos)#Hier werden die Daten an die Index.html Datei übergeben


@app.route('/add', methods=["POST"])#Add wird aufgerufen wenn ein POST Request gemacht wird
def add():
    title = request.form.get("title")
    helper.add(title)
    return redirect(url_for("index"))


@app.route('/update/<int:index>')#URL mit Platzhalter, wird an Update Funktion übergeben.
def update(index):
    helper.update(index)
    return redirect(url_for("index"))

@app.route("/download")
def get_csv():
    return Response(
        helper.get_csv(),
        mimetype="text/csv",
        headers={"Content-disposition":"attachment; filename=zu-bbbearbeiten.csv"},
    )
