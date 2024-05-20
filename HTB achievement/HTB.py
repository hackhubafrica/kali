import aiohttp
import asyncio
import time

# Define the base URL
base_url = "https://www.hackthebox.com/achievement/machine/1694822/"

# Define the list of achievement IDs to fuzz
# Add more IDs to this list as needed
achievement_ids = ["590", "591", "592", "593", "594"]
for i in range(1, 2001):
  achievement_ids.append(str(i))

# Asynchronous function to check the validity of an achievement ID with delay
async def check_achievement(session, achievement_id, delay=1):  # Added delay argument
  # Construct the full URL
  url = base_url + achievement_id

  # Introduce a delay before sending the request
  await asyncio.sleep(delay)  # Delay for 1 second by default

  # Send an asynchronous HTTP GET request to the URL
  async with session.get(url) as response:
    # Read the response content
    content = await response.text()

    # Check for the specified messages in the response content
    if "Invalid Achievement" in content or "This achievement does not appear to be valid!" in content:
      print(f"Achievement ID {achievement_id} is invalid.")
    else:
      print(f"Achievement ID {achievement_id} is valid.")

# Main function to run the asynchronous tasks
async def main():
  # Create an asynchronous HTTP session
  async with aiohttp.ClientSession() as session:
    # Create tasks for each achievement ID
    tasks = [check_achievement(session, achievement_id) for achievement_id in achievement_ids]

    # Run the tasks concurrently with delay between each
    for task in tasks:
      await task
      await asyncio.sleep(1)  # Delay between tasks for 1 second

# Run the main function
asyncio.run(main())
