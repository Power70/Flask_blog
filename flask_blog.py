from flask import Flask, render_template, url_for, flash, redirect
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
@app.route("/register", methods=["GET", "POST"])
# to accept a post request add allowed methods in our routes
def register():
    form = RegistratonForm() #this create an instance of the form
    # form validation
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)
    # with form=form we have access to the instance above
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm() #this create an instance of the form
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
        return redirect(url_for("login"))
    return render_template("login.html", title="Login", form=form)
    # with form=form we have access to the instance above

if __name__ == "__main__":
    app.run(debug=True)
