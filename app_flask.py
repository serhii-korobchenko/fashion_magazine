from flask import Flask, render_template


app = Flask(__name__)
app.debug = True
app.env = "development"


@app.route("/", strict_slashes=False)
def index():

    return render_template("Home_page.html")


@app.route("/heartess_collection/", strict_slashes=False)
def heartess_collection():

    return render_template("Heartess Collection.html")





if __name__ == "__main__":
    app.run()
