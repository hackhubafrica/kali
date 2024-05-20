import openai

# Hardcoded API key (Ensure this is secure in production)
openai.api_key = "sk-proj-PypJ5NH1vNkGf0w3G4PPT3BlbkFJZ6IsW9rCWdr5eBbCbn2r"

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except openai.error.RateLimitError:
        return "Rate limit exceeded. Please check your plan and billing details."
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("ChatGPT: ", response)
