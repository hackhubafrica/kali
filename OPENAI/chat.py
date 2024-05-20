import openai
import time

# Your API key (keep it secure and do not hardcode it in production code)
api_key = "sk-proj-h7DsIKjXRmRoghfyHoZ4T3BlbkFJctSwCEzUs7UBHkidn10O"

# Set the API key for OpenAI
openai.api_key = api_key

# Define a retry strategy
def create_chat_completion_with_retry(retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
                ]
            )
            return response
        except openai.error.RateLimitError:
            if attempt < retries - 1:
                print(f"Rate limit exceeded. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                raise

response = create_chat_completion_with_retry()

# Print the content of the first choice in the completion response
print(response.choices[0].message['content'])
