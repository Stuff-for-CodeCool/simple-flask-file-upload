from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from os.path import join

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/upload"


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        try:
            f = request.files["File"]
            f.save(join(app.config["UPLOAD_FOLDER"], secure_filename(f.filename)))
            return "File saved successfully"
        except KeyError:
            return "no file found"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
