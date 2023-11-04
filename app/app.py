from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/content-1")
def content_1():
    return render_template("public/content-1.html")

@app.route("/content-2")
def content_2():
    return render_template("public/content-2.html")

@app.route("/content-3")
def content_3():
    return render_template("public/content-3.html")

@app.errorhandler(404)
def not_found(error):
    return render_template("public/404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)