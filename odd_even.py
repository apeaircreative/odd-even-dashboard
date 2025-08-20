def odd_or_even_list(numbers):
    for num in numbers:
        print(f"{num} → {'Even' if num % 2 == 0 else 'Odd'}")

# Example usage
odd_or_even_list([1, 2, 3, 4, 5, 10])
