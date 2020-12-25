import os
from flask import (Flask, flash,
                   render_template, redirect, request,
                   session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination, get_page_args
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Home Page
@app.route("/")
@app.route("/get_artists")
def get_artists():
    artists = mongo.db.artists.find().sort([("_id", -1)]).limit(5)
    return render_template("artists.html", artists=artists)


# Show All the Artists in the database, in alphabetical order
@app.route("/all_artists")
def all_artists():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    per_page = 5

    offset = page * per_page - per_page

    total = mongo.db.artists.find().count()

    artists = list(mongo.db.artists.find().sort("artist_name", 1))

    pagination_artists = artists[offset: offset + per_page]

    pagination = Pagination(page=page, per_page=per_page,
                            offset=offset, total=total,
                            css_framework='bootstrap4')

    return render_template("all-artists.html", artists=pagination_artists,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


# Search Functionality
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    artists = list(mongo.db.artists.find({"$text": {"$search": query}}))

    return render_template("search.html", artists=artists)


# Register Functionality
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username is already in use. Please try another one.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Well done! Now go ahead and add your profile!")
        return redirect(url_for("add_profile", username=session["user"]))

    return render_template("register.html")


# Login Functionality
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username").capitalize()))
                return redirect(
                    url_for("profile", username=session["user"]))
            else:
                flash("Oops! Check username and password again")
                return redirect(url_for("login"))

        else:
            flash("Oops! Check username and password again")
            return redirect(url_for("login"))

    return render_template("login.html")


# Display personal profile to user
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    artist = mongo.db.artists.find_one(
        {"created_by": session["user"]})

    if session["user"]:
        return render_template(
            "profile.html", username=username, artist=artist)

    return redirect(url_for('login'))


# Logout Functionality
@app.route("/logout")
def logout():
    flash("See you next time!")
    session.pop("user")
    return redirect(url_for('login'))


# Add Profile after registering new user
@app.route("/add_profile/<username>", methods=["GET", "POST"])
def add_profile(username):

    username = mongo.db.users.find_one(
        {"username": session["user"]})

    if request.method == "POST":
        artist = {
            "artist_name": request.form.get("artist_name"),
            "address": request.form.get("address"),
            "city": request.form.get("city"),
            "country": request.form.get("country"),
            "phone": request.form.get("phone"),
            "email": request.form.get("email"),
            "facebook": request.form.get("facebook"),
            "instagram": request.form.get("instagram"),
            "profile_url": request.form.get("profile_url"),
            "languages": request.form.get("languages"),
            "style": request.form.get("style"),
            "bio": request.form.get("bio"),
            "created_by": session["user"],
            "photo_1": request.form.get("photo_1"),
            "photo_2": request.form.get("photo_2"),
            "photo_3": request.form.get("photo_3"),
            "photo_4": request.form.get("photo_4"),
            "photo_5": request.form.get("photo_5"),
            "photo_6": request.form.get("photo_6")
        }

        mongo.db.artists.insert_one(artist)
        flash("Great, your profile is now added!")
        return redirect(url_for('profile', username=session['user']))

    return render_template("add-profile.html", username=username)


# Edit user's profile
@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    artist = mongo.db.artists.find_one(
        {"created_by": session["user"]})

    if session["user"]:

        if request.method == "POST":

            submit = {
                "artist_name": request.form.get("artist_name"),
                "address": request.form.get("address"),
                "city": request.form.get("city"),
                "country": request.form.get("country"),
                "phone": request.form.get("phone"),
                "email": request.form.get("email"),
                "facebook": request.form.get("facebook"),
                "instagram": request.form.get("instagram"),
                "profile_url": request.form.get("profile_url"),
                "languages": request.form.get("languages"),
                "style": request.form.get("style"),
                "bio": request.form.get("bio"),
                "created_by": session["user"],
                "photo_1": request.form.get("photo_1"),
                "photo_2": request.form.get("photo_2"),
                "photo_3": request.form.get("photo_3"),
                "photo_4": request.form.get("photo_4"),
                "photo_5": request.form.get("photo_5"),
                "photo_6": request.form.get("photo_6")
            }

            mongo.db.artists.update({"created_by": session["user"]}, submit)
            flash("Great, your profile is now updated!")
            return redirect(url_for('profile', username=session['user']))

    return render_template(
        "edit-profile.html", username=username, artist=artist)


# Ask for confirmation when user clicks on "delete profile"
@app.route("/confirm_delete/<username>", methods=["GET", "POST"])
def confirm_delete(username):

    return render_template("confirm-delete.html")


# Delete user's profile
@app.route("/delete/<username>")
def delete_profile(username):
    mongo.db.artists.remove({"created_by": session["user"]})
    flash("Your profile has been deleted. We hope to have you back soon!")
    return redirect(url_for('get_artists'))


# Show Artist Page: page acessible to all users
@app.route("/show_artist/<artist_id>")
def show_artist(artist_id):
    artist = mongo.db.artists.find_one(
        {"_id": ObjectId(artist_id)})
    return render_template("artist-page.html", artist=artist)


# Show Artists specialized in Manga style: page acessible to all users
@app.route("/show_manga")
def show_manga():
    artists = list(mongo.db.artists.find(
        {"$text": {"$search": "manga anime"}}))
    return render_template("show-styles.html", artists=artists)


# Show Artists specialized in Nordic style: page acessible to all users
@app.route("/show_nordic")
def show_nordic():
    artists = list(mongo.db.artists.find(
        {"$text": {"$search": "nordic viking"}}))
    return render_template("show-styles.html", artists=artists)


# Show Artists specialized in Japanese style: page acessible to all users
@app.route("/show_japanese")
def show_japanese():
    artists = list(mongo.db.artists.find(
        {"$text": {"$search": "japanese"}}))
    return render_template("show-styles.html", artists=artists)


# Show Artists specialized in Realistic style: page acessible to all users
@app.route("/show_realism")
def show_realism():
    artists = list(mongo.db.artists.find(
        {"$text": {"$search": "realism realistic"}}))
    return render_template("show-styles.html", artists=artists)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
