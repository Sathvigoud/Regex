import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form["test_string"]
    regex = request.form["regex"]

    matches = re.findall(regex, test_string)
    if not matches:
        no_match_message = "No match found!"
    else:
        no_match_message = None

    return render_template("index.html", test_string=test_string, regex=regex, matches=matches, no_match_message=no_match_message)

@app.route("/validate-email", methods=["POST"])
def validate_email():
    email = request.form["email"]
    email_regex = r'[\w.%+-]+@[\w.-]+[\w]+\.[\w]{2,}'
    is_valid = re.match(email_regex, email) is not None

    if is_valid:
        validation_message = "The email is valid!"
    else:
        validation_message = "The email is not valid."

    

   
    return render_template("validate_email.html", email=email, is_valid=is_valid, validation_message=validation_message)

if __name__ == "__main__":
    app.run(debug=True)
