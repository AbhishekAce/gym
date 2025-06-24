from flask import Flask, render_template, request, redirect, url_for
import json
import datetime
import os

app = Flask(__name__)
DATA_FILE = "gym_log.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

def calc_streak(data):
    if not data:
        return 0
    data = sorted(data)
    streak = 1
    for i in range(len(data)-1, 0, -1):
        d1 = datetime.date.fromisoformat(data[i])
        d2 = datetime.date.fromisoformat(data[i-1])
        if (d1 - d2).days == 1:
            streak += 1    //add streak makes people  like the  game
        else:
            break
    return streak

@app.route("/")
def index():
    data = load_data()
    streak = calc_streak(data)
    return render_template("index.html", streak=streak, log=data[::-1])

@app.route("/log", methods=["POST"])
def log_today():
    today = datetime.date.today().isoformat()
    data = load_data()
    if today not in data:
        data.append(today)
        save_data(data)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
