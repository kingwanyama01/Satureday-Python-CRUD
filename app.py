from flask import Flask,render_template,request,redirect,url_for,flash,session
from flask_bcrypt import generate_password_hash, check_password_hash
from database_and_tables_file import User,Product
app = Flask(__name__)
app.secret_key = "uteujytkjykjdydkyy"

@app.route('/',methods=["GET","POST"])
def register():  # put application's code here
    if request.method == "POST":
        userName = request.form["u_name"]
        userEmail = request.form["u_email"]
        userPassword = request.form["u_pass"]
        encryptedUserPassword = generate_password_hash(userPassword)
        User.create(name = userName, email = userEmail, password = encryptedUserPassword)
        flash("User created successfully")
    return render_template("register.html")

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        userEmail = request.form["u_email"]
        userPassword = request.form["u_pass"]
        try:
            user = User.get(User.email == userEmail)
            encryptedPassword = user.password
            if check_password_hash(encryptedPassword,userPassword):
                flash("Login successful")
                session["loggedIn"] = True
                session["userName"] = user.name
                return redirect(url_for("home"))
        except:
            flash("Wrong email or password")
    return render_template("login.html")

@app.route("/home")
def home():
    if not  session["loggedIn"]:
        return redirect(url_for("login"))
    return  render_template("home.html")


if __name__ == '__main__':
    app.run()
