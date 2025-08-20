def split_odd_even(numbers):
    evens = []
    odds = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens, odds

# Example usage
nums = [1, 2, 3, 4, 5, 10]
evens, odds = split_odd_even(nums)
print("Evens:", evens)
print("Odds:", odds)
