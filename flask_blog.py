from flask import Flask, render_template, url_for
from forms import RegistratonForm, LoginForm
app = Flask(__name__)

# add secrete key
app.config["SECRET_KEY"] = "27b6dcd360704809fc675ebe7db64540"
posts = [
    {
        "author": "Torzor Hub",
        "title": "Blog post 1",
        "content": "first post content",
        "date_posted": "April 20, 2018"
    },
     {
        "author": "jane Doe",
        "title": "Blog post 2",
        "content": "second post content",
        "date_posted": "April 20, 2018"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
@app.route("/about")
def about():
    return render_template('about.html', title="About")
@app.route("/register")
def register():
    form = RegistratonForm() #this create an instance of the form
    return render_template("register.html", title="Register", form=form)
    # with form=form we have access to the instance above
@app.route("/login")
def login():
    form = LoginForm() #this create an instance of the form
    return render_template("login.html", title="Login", form=form)
    # with form=form we have access to the instance above

if __name__ == "__main__":
    app.run(debug=True)
