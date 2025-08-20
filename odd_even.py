import random
import time
import matplotlib.pyplot as plt

def real_time_plot():
    even_count, odd_count = 0, 0
    evens, odds = [], []
    x_axis = []

    plt.ion()  # interactive mode on
    fig, ax = plt.subplots()

    print("Streaming numbers... updating chart (Press Ctrl+C to stop)")
    try:
        i = 0
        while True:
            i += 1
            num = random.randint(1, 100)
            
            if num % 2 == 0:
                even_count += 1
                print(f"{num} → Even")
            else:
                odd_count += 1
                print(f"{num} → Odd")

            # update data
            x_axis.append(i)
            evens.append(even_count)
            odds.append(odd_count)

            # redraw graph
            ax.clear()
            ax.plot(x_axis, evens, label="Even Count", color="blue")
            ax.plot(x_axis, odds, label="Odd Count", color="red")
            ax.set_xlabel("Time (steps)")
            ax.set_ylabel("Cumulative Counts")
            ax.set_title("Real-Time Odd vs Even Counter")
            ax.legend()
            plt.pause(0.5)

            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nStreaming stopped.")
        plt.ioff()
        plt.show()

# Example usage
real_time_plot()
