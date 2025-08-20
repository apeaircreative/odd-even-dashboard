import random
import time

def log_stream_odd_even():
    print("Streaming numbers... Logging to evens.txt and odds.txt (Press Ctrl+C to stop)")
    
    try:
        while True:
            num = random.randint(1, 100)
            if num % 2 == 0:
                with open("evens.txt", "a") as f:
                    f.write(str(num) + "\n")
                print(f"{num} → Even")
            else:
                with open("odds.txt", "a") as f:
                    f.write(str(num) + "\n")
                print(f"{num} → Odd")
            
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStream stopped. Numbers logged successfully.")

# Example usage
log_stream_odd_even()
