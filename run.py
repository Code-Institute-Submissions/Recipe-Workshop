import os
from flask import Flask, render_template, url_for, redirect, request, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("NONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Global Variables

new = mongo.db.recipes
user = mongo.db.users


@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/recipe')
def get_recipe():

    return render_template("public/recipe.html", recipes=mongo.db.recipe.find())

@app.route('/new_recipe', methods=["GET", "POST"])
def new_recipe():

    return render_template("public/new_recipe.html")




@app.route('/register', methods=["GET", "POST"])
def user_registration():
 
    if request.method == "POST":
        req = request.form

        username = req["username"]
        email = req["email"]
        password = req["password"]

        new_user = {
            "username" : username,
            "email" : email,
            "password" : password
        }
        user.insert_one(new_user)
        print(new_user)
        return redirect(request.url)

    return render_template("public/register.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("public/404.html"), 404

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=True)