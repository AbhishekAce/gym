import json
import datetime
import os

DATA_FILE = "gym_log.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

def log_today():
    today = datetime.date.today().isoformat()
    data = load_data()
    if today in data:
        print("You already logged today!")
    else:
        data.append(today)
        save_data(data)
        print("Logged gym session for today!")

def view_streak():
    data = sorted(load_data())
    if not data:
        print("No gym sessions logged yet.")
        return
    streak = 1
    for i in range(len(data)-1, 0, -1):
        d1 = datetime.date.fromisoformat(data[i])
        d2 = datetime.date.fromisoformat(data[i-1])
        if (d1 - d2).days == 1:
            streak += 1
        else:
            break
    print(f"Your current gym streak is: {streak} days.")

def main():
    while True:
        print("\nGym Habit Tracker")
        print("1. Log today's gym session")
        print("2. View current streak")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        if choice == "1":
            log_today()
        elif choice == "2":
            view_streak()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
