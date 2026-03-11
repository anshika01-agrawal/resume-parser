from flask import Flask, render_template, request
import os
from parser import parse_resume

app = Flask(__name__)

UPLOAD_FOLDER = "resumes"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    name, email, phone, skills = parse_resume(filepath)

    return render_template(
        "result.html",
        name=name,
        email=email,
        phone=phone,
        skills=skills
    )


if __name__ == "__main__":
    app.run(debug=True)