const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log("Enter numbers (type 'quit' to stop):");

rl.on("line", (input) => {
  if (input.toLowerCase() === "quit") {
    console.log("Stream ended.");
    rl.close();
  } else {
    let num = Number(input);
    if (!isNaN(num)) {
      console.log(num + " → " + (num % 2 === 0 ? "Even" : "Odd"));
    } else {
      console.log("Enter a valid number or 'quit'.");
    }
  }
});
