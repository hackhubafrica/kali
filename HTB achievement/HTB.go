package main

import (
  "fmt"
  "net/http"
  "time"
)

func checkAchievement(url string, delay time.Duration) bool {
  // Simulate HTTP request (replace with actual logic)
  time.Sleep(delay)
  // ... (check response for validity)
  return true // Replace with actual validity check
}

func main() {
  baseUrl := "https://www.hackthebox.com/achievement/machine/1694822/"
  achievementIds := []string{"59
