from flask import Flask, render_template

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/contact")
def contact():
  return "contact to my email"

@app.route("/<username>")
def potato(username):
  return f"Hello {username} how are you doing"

app.run(host="0.0.0.0")