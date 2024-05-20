const async = require('async');
const request = require('request');

const baseUrl = "https://www.hackthebox.com/achievement/machine/1694822/";
const achievementIds = ["590", "591", "592", "..."]; // Add more IDs

const delayMs = 1000; // 1 second delay

async.eachLimit(achievementIds, 1, (id, callback) => {
  const url = baseUrl + id;
  setTimeout(() => {
    // Simulate HTTP request (replace with actual request)
    request(url, (error, response, body) => {
      if (error) {
        console.error("Error:", error);
      } else {
        // Check response for validity (replace with actual logic)
        console.log(`ID ${id} - Valid: true`); // Replace with validity check
      }
      callback();
    });
  }, delayMs);
}, (err) => {
  if (err) {
    console.error("Error:", err);
  } else {
    console.log("All checks completed.");
  }
});
