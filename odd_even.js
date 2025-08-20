const fs = require("fs");

function logStreamOddEven() {
  console.log("Streaming numbers... Logging to evens.txt and odds.txt (Press Ctrl+C to stop)");

  setInterval(() => {
    let num = Math.floor(Math.random() * 100) + 1;

    if (num % 2 === 0) {
      fs.appendFileSync("evens.txt", num + "\n");
      console.log(num + " → Even");
    } else {
      fs.appendFileSync("odds.txt", num + "\n");
      console.log(num + " → Odd");
    }
  }, 1000);
}

// Start stream
logStreamOddEven();
