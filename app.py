from flask import Flask, render_template
import os

app = Flask(__name__)

# Use environment variable for site title
SITE_TITLE = os.getenv("SITE_TITLE", "My Flask App")

@app.route("/")
def home():
    return render_template("home.html", title=SITE_TITLE)

@app.route("/about")
def about():
    return render_template("about.html", title=SITE_TITLE)

if __name__ == "__main__":
    app.run(debug=True)
