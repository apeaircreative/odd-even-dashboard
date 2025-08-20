def stream_odd_even():
    print("Enter numbers (type 'quit' to stop):")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Stream ended.")
            break
        try:
            num = int(user_input)
            print(f"{num} → {'Even' if num % 2 == 0 else 'Odd'}")
        except ValueError:
            print("Please enter a valid number or 'quit'.")

# Example usage
stream_odd_even()
