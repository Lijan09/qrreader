from flask import Flask, render_template, url_for, Response, redirect, request

app = Flask(__name__)

@app.route("/")
def test():
    return render_template("signup.html")


@app.route("/", methods=["GET", "POST"])
def testdata():
    if request.method == "POST":
        test = request.form["fname"]

        print (type(test))

        return redirect(url_for("test"))


if __name__ == "__main__":
    app.run(debug=True)
