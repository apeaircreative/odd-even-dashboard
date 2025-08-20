function oddOrEvenList(numbers) {
  numbers.forEach(num => {
    console.log(num + " → " + (num % 2 === 0 ? "Even" : "Odd"));
  });
}

// Example usage
oddOrEvenList([1, 2, 3, 4, 5, 10]);
