from flask import Flask, render_template, request, redirect, session, flash, url_for
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = "supersecretkey"

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password BLOB,
            attempts INTEGER DEFAULT 0,
            locked INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return redirect("/login")


# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                      (username, hashed))
            conn.commit()
            flash("Account created successfully! Please login.", "success")
            return redirect("/login")
        except:
            flash("Username already exists!", "danger")
        conn.close()

    return render_template("register.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()

        if user:

            if user[4] == 1:
                flash("Account Locked due to multiple failed attempts!", "danger")
                return redirect("/login")

            if bcrypt.checkpw(password.encode('utf-8'), user[2]):
                c.execute("UPDATE users SET attempts=0 WHERE username=?", (username,))
                conn.commit()
                session["user"] = username
                flash("Login successful!", "success")
                return redirect("/dashboard")

            else:
                attempts = user[3] + 1

                if attempts >= 3:
                    c.execute("UPDATE users SET locked=1 WHERE username=?", (username,))
                    conn.commit()
                    flash("Account Locked due to multiple failed attempts!", "danger")
                else:
                    c.execute("UPDATE users SET attempts=? WHERE username=?",
                              (attempts, username))
                    conn.commit()
                    flash(f"Invalid Password! Attempts left: {3 - attempts}", "danger")

                return redirect("/login")

        flash("User not found!", "danger")
        return redirect("/login")

    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect("/login")


# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully", "success")
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
