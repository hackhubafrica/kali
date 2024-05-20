#include <iostream>
#include <future>
#include <thread>
#include <vector>
#include <string>
#include <mutex>
#include <this_thread>

// Define the base URL
const std::string base_url = "https://www.hackthebox.com/achievement/machine/1694822/";

// Function to check achievement ID validity (simulates HTTP request)
bool check_achievement(const std::string& achievement_id, int delay_ms) {
  // Simulate delay
  std::this_thread::sleep_for(std::chrono::milliseconds(delay_ms));

  // Simulate response content (replace with actual HTTP request if needed)
  std::string content = "Sample response content";

  if (content.find("Invalid Achievement") != std::string::npos ||
      content.find("This achievement does not appear to be valid!") != std::string::npos) {
    std::cout << "Achievement ID " << achievement_id << " is invalid." << std::endl;
    return false;
  } else {
    std::cout << "Achievement ID " << achievement_id << " is valid." << std::endl;
    return true;
  }
}

int main() {
  // Define achievement IDs
  std::vector<std::string> achievement_ids = {"590", "591", "592", "593", "594"};
  for (int i = 1; i < 2001; ++i) {
    achievement_ids.push_back(std::to_string(i));
  }

  // Define delay
  int delay_ms = 1000; // 1 second

  // Thread pool to manage concurrent tasks
  std::vector<std::future<bool>> results;
  std::mutex mtx; // Mutex for thread-safe output

  // Launch tasks for each achievement ID
  for (const std::string& id : achievement_ids) {
    results.push_back(std::async(std::launch::async, check_achievement, id, delay_ms));
  }

  // Wait for all tasks to finish and print results
  for (auto& result : results) {
    try {
      bool valid = result.get();
      std::lock_guard<std::mutex> lock(mtx); // Acquire lock for thread-safe output
      if (valid) {
        std::cout << "Valid ID found." << std::endl;
      }
    } catch (const std::exception& e) {
      std::cerr << "Error: " << e.what() << std::endl;
    }
  }

  return 0;
}
