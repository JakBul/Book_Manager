import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# Main set up for the project and connecting to the env.py keys
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# 'Home Page' where the user can see the available categories
@app.route("/")
@app.route("/home")
def home():
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("home.html", categories=categories)


# 'Books Page' where the user can see the current books from the database
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    return render_template("books.html", books=books)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Functionality on the 'Books Page' where the user can search through the
    books in database, the index is set up on MongoDB
    """
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    return render_template("books.html", books=books)


# 'Register Page' where the user can register to our page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into the 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("home"))
    return render_template("register.html")


# 'Sign In Page' where the user can sign in to our page
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if the username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure the hashed password matches the user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("home"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Passowrd")
                return redirect(url_for("signin"))

        else:
            # the username doesn't exist
            flash("Incorrect Username and/or Passowrd")
            return redirect(url_for("signin"))

    return render_template("signin.html")


# 'Sign Out' in the navigation menu where the user can sign out from our page
@app.route("/signout")
def signout():
    # remove the user from the session cookies
    flash("You have been signed out")
    session.pop("user")
    return redirect(url_for("signin"))


# 'Add Book' page where the user can add the book
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    # check if the user is logged in
    if not session.get('user'):
        return render_template("404.html")
    if request.method == "POST":
        must_read = "on" if request.form.get("must_read") else "off"
        book = {
            "category_name": request.form.get("category_name"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "image_url": request.form.get("image_url"),
            "book_summary": request.form.get("book_summary"),
            "must_read": must_read,
            "book_url": request.form.get("book_url"),
            "created_by": session["user"]
        }
        mongo.db.books.insert_one(book)
        flash("Book Successfully Added")
        return redirect(url_for("get_books"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_book.html", categories=categories)


# 'Edit' button on the card of a book opens the page 'Edit Book'
@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    """
    Check if there is a book with the matching ID, any user is logged in and
    the logged in user is the user who added the book to the database
    """
    if not book or not session.get('user') or session['user'] != book[
            'created_by']:
        return render_template("404.html")
    if request.method == "POST":
        must_read = "on" if request.form.get("must_read") else "off"
        submit = {
            "$set": {"category_name": request.form.get("category_name"),
                     "book_name": request.form.get("book_name"),
                     "author_name": request.form.get("author_name"),
                     "image_url": request.form.get("image_url"),
                     "book_summary": request.form.get("book_summary"),
                     "must_read": must_read,
                     "book_url": request.form.get("book_url"),
                     "created_by": session["user"]}
        }
        mongo.db.books.update_one({"_id": ObjectId(book_id)}, submit)
        flash("Book Successfully Updated")

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_book.html", book=book, categories=categories)


# 'Delete' button on the card of a book that deletes the book from the database
@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    """
    Check if there is a book with the matching ID, any user is logged in and
    the logged in user is the user who added the book to the database
    """
    if not book or not session.get('user') or session['user'] != book[
            'created_by']:
        return render_template("404.html")
    mongo.db.books.delete_one({"_id": ObjectId(book_id)})
    flash("Book Successfully Deleted")
    return redirect(url_for("get_books"))


# 'Manage Categories' page made for the administrator to access the database
@app.route("/get_categories")
def get_categories():
    # check if there is any user logged in and if the user is the administrator
    if session.get('user') and session['user'] == "admin":
        categories = list(mongo.db.categories.find().sort("category_name", 1))
        return render_template("categories.html", categories=categories)
    else:
        return render_template("404.html")


# 'Add Category' page made for the administrator to access the database
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # check if there is any user logged in and if the user is the administrator
    if not session.get('user') or session['user'] != "admin":
        return render_template("404.html")
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# 'Edit Category' page made for the administrator to access the database
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    """
    Check if there is a category with the matching ID, any user is logged in
    and the logged in user is the administrator
    """
    if not category or not session.get('user') or session['user'] != "admin":
        return render_template("404.html")
    if request.method == "POST":
        submit = {
            "$set": {"category_name": request.form.get("category_name")}
        }
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    return render_template('edit_category.html', category=category)


# 'Delete' button on the card of a category that deletes it from the database
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    """
    Check if there is a category with the matching ID, any user is logged in
    and the logged in user is the administrator
    """
    if not category or not session.get('user') or session['user'] != "admin":
        return render_template("404.html")
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


# '404 page' to handle any errors on the website
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


# '500 page' to handle any errors on the servers
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')


# Main setup for host and port
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
