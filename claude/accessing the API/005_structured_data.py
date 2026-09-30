# Before making any API calls, you need to install the required packages and configure your API key securely.
# Make sure the parent claude folder has a .env file with your ANTHROPIC_API_KEY set.

from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from anthropic import Anthropic
import json

client = Anthropic()
model = "claude-sonnet-5"

# functions to help manage chat messages and interact with the API
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

# Start with an empty message list
messages = []

# Add the initial user question
add_user_message(messages, "Generate a very short EventBridge rule as valid JSON. Return only the JSON, without Markdown fences.")

text = chat(messages)

# Clean up and parse the JSON
clean_json = json.loads(text.strip())

print("Clean JSON:", clean_json)

