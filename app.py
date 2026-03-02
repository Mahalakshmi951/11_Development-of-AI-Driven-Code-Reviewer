from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this in production

# Dummy credentials
USER_CREDENTIALS = {
    "admin": "password123"
}

# =========================
# LOGIN ROUTE
# =========================
@app.route("/", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("dashboard"))

    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


# =========================
# DASHBOARD ROUTE
# =========================
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    complexity_score = None
    review = ""
    syntax_error = None

    if request.method == "POST":
        code = request.form.get("code", "")
        lines = code.strip().split("\n")
        num_lines = len(lines)

        # Dummy complexity scoring logic
        if num_lines <= 1:
            complexity_score = 80
        elif num_lines <= 5:
            complexity_score = 60
        else:
            complexity_score = 40

        review = f"""
Review Feedback:
- The code has {num_lines} line(s).
- Simple and works as intended.
- Consider adding error handling, comments, or a main function.
- Follow consistent naming conventions and coding standards.
""".strip()

        # Syntax check
        try:
            compile(code, "<string>", "exec")
        except Exception as e:
            syntax_error = str(e)

    return render_template(
        "dashboard.html",
        complexity_score=complexity_score,
        review=review,
        syntax_error=syntax_error
    )


# =========================
# LOGOUT ROUTE
# =========================
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


# =========================
# RUN APPLICATION
# =========================
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )