# pour lancer l'application, 2 solutions :
# * python main.py
# * FLASK_APP=main.py flask run

from flask import Flask, render_template, request, abort, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# flask WTF config
import os

SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY
csrf = CSRFProtect(app)
# fin config


class NewUser(FlaskForm):
    name = StringField("name", validators=[DataRequired(), Length(min=2, max=30)])
    age = IntegerField("age", validators=[DataRequired()])


@app.route("/")
def index():
    return "Hello World !"


MEMBERS = [
    {"name": "John", "age": 25},
    {"name": "Mary", "age": 21},
    {"name": "Jane", "age": 22},
    {"name": "Peter", "age": 29},
    {"name": "Anne", "age": 28},
]


def get_member_from_name(name):
    for member in MEMBERS:
        if member["name"] == name:
            return member
    return None


@app.route("/welcome1/<string:name>")
def welcome_1(name: str):
    return f"Welcome {name} !"


@app.route("/welcome2/<string:name>")
def welcome_2(name: str):
    member = get_member_from_name(name)
    if member:
        # ne pas utiliser dans un cas réel, car vraiment peu performant
        # utiliser plutôt une vraie base de données
        context = {"member": member, "members": MEMBERS}
        return render_template("welcome.html", **context)
    # une fonction de vue ne peut pas ne rien retourner
    abort(404)


@app.route("/new-member1", methods=["GET", "POST"])
def new_member_without_flask_wtf():
    if request.method == "GET":
        return render_template("new_member.html")
    elif request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        print(request.form)
        if name:
            MEMBERS.append({"name": name, "age": age})
            flash(f"New member added: {name=} -- {age=}")
            return redirect("/success")
        else:
            # le formulaire n'étant pas lié (bound) on ne pas afficher les erreurs
            # on devrait les afficher manuellement (assez fastidieux)
            return render_template("new_member.html")


@app.route("/new-member2", methods=["GET", "POST"])
def new_member_with_flask_wtf():
    form = NewUser()
    if form.validate_on_submit():
        print(form, form.data)
        MEMBERS.append({"name": form.data["name"], "age": form.data["age"]})

        # pour comprendre comment fonctionne flash
        # https://stackoverflow.com/questions/76214242/
        # cette fonction permet d'afficher des données pour la requete suivante seulement
        flash(f"New member added: {form.data["name"]=} -- {form.data["age"]=}")
        return redirect("/success")
    return render_template("new_member_wtf.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html")


@app.errorhandler(404)
def erreur_404(error):
    print(error)
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
