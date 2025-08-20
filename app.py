from flask import Flask, jsonify, render_template
import threading
import time
import random

app = Flask(__name__)

# Global counters + lock
even_count, odd_count = 0, 0
streaming = True

def number_stream():
    global even_count, odd_count, streaming
    while True:
        if streaming:
            num = random.randint(1, 100)
            if num % 2 == 0:
                even_count += 1
                with open("evens.txt", "a") as f:
                    f.write(str(num) + "\n")
                print(f"{num} → Even")
            else:
                odd_count += 1
                with open("odds.txt", "a") as f:
                    f.write(str(num) + "\n")
                print(f"{num} → Odd")
        time.sleep(1)  # Wait 1s between numbers

# Flask Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def get_data():
    return jsonify({"even": even_count, "odd": odd_count})

@app.route("/start")
def start():
    global streaming
    streaming = True
    return "Stream started."

@app.route("/stop")
def stop():
    global streaming
    streaming = False
    return "Stream stopped."

# Launch background thread
threading.Thread(target=number_stream, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=True)
