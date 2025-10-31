from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

<<<<<<< HEAD
    # mel
=======
    # soo?
>>>>>>> 9e03d7159e154b49feda42e621b79488a67f8886
