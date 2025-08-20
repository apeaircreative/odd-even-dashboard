function oddOrEvenList(numbers) {
  return numbers.map(num => num + " → " + (num % 2 === 0 ? "Even" : "Odd"));
}

// Example usage
console.log(oddOrEvenList([1, 2, 3, 4, 5, 10]));
