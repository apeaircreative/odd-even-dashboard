function autoStreamOddEven() {
  console.log("Starting automated Odd/Even stream... (Press Ctrl+C to stop)");

  setInterval(() => {
    let num = Math.floor(Math.random() * 100) + 1; // 1 to 100
    console.log(num + " → " + (num % 2 === 0 ? "Even" : "Odd"));
  }, 1000); // every 1 second
}

// Start the stream
autoStreamOddEven();
