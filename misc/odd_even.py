import random
import time
import threading
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class OddEvenDashboard:
    def __init__(self, root):
        self.running = False
        self.even_count, self.odd_count = 0, 0
        self.steps, self.evens, self.odds = [], [], []
        self.step = 0

        # Setup UI
        self.label = ttk.Label(root, text="Odd/Even Dashboard", font=("Arial", 16))
        self.label.pack(pady=10)

        self.start_button = ttk.Button(root, text="Start Stream", command=self.start_stream)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(root, text="Stop Stream", command=self.stop_stream)
        self.stop_button.pack(pady=5)

        # Matplotlib Figure inside Tkinter
        self.fig, self.ax = plt.subplots(figsize=(5,3))
        self.ax.set_title("Real-Time Odd vs Even Count")
        self.ax.set_xlabel("Steps")
        self.ax.set_ylabel("Count")
        self.canvas = FigureCanvasTkAgg(self.fig, root)
        self.canvas.get_tk_widget().pack()

    def stream_numbers(self):
        while self.running:
            self.step += 1
            num = random.randint(1, 100)
            if num % 2 == 0:
                self.even_count += 1
                with open("evens.txt", "a") as f:
                    f.write(str(num) + "\n")
                print(f"{num} → Even")
            else:
                self.odd_count += 1
                with open("odds.txt", "a") as f:
                    f.write(str(num) + "\n")
                print(f"{num} → Odd")

            # Update data
            self.steps.append(self.step)
            self.evens.append(self.even_count)
            self.odds.append(self.odd_count)

            # Update graph
            self.ax.clear()
            self.ax.plot(self.steps, self.evens, label="Evens", color="blue")
            self.ax.plot(self.steps, self.odds, label="Odds", color="red")
            self.ax.legend()
            self.canvas.draw()

            time.sleep(1)

    def start_stream(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.stream_numbers, daemon=True).start()

    def stop_stream(self):
        self.running = False

# Run UI
root = tk.Tk()
root.title("Odd or Even Dashboard")
app = OddEvenDashboard(root)
root.mainloop()
