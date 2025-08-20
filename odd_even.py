import random
import time

def auto_stream_odd_even():
    print("Starting automated Odd/Even stream... (Press Ctrl+C to stop)")
    try:
        while True:
            num = random.randint(1, 100)  # random number between 1 and 100
            print(f"{num} → {'Even' if num % 2 == 0 else 'Odd'}")
            time.sleep(1)  # wait 1 second before next number
    except KeyboardInterrupt:
        print("\nStream stopped.")

# Example usage
auto_stream_odd_even()
