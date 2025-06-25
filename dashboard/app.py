from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    action = None
    if request.method == "POST":
        action = request.form.get("action")
        # Integrate with your gym logic here
    return render_template("index.html", action=action)

if __name__ == "__main__":
    app.run(debug=True)
