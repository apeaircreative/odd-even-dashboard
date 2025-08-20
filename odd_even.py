def odd_or_even_list(numbers):
    results = []
    for num in numbers:
        results.append(f"{num} → {'Even' if num % 2 == 0 else 'Odd'}")
    return results

# Example usage
nums = [1, 2, 3, 4, 5, 10]
print(odd_or_even_list(nums))
