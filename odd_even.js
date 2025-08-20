function splitOddEven(numbers) {
  let evens = [];
  let odds = [];
  
  numbers.forEach(num => {
    (num % 2 === 0 ? evens : odds).push(num);
  });
  
  return { evens, odds };
}

// Example usage
const result = splitOddEven([1, 2, 3, 4, 5, 10]);
console.log("Evens:", result.evens); 
console.log("Odds:", result.odds);
