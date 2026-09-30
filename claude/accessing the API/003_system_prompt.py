# Before making any API calls, you need to install the required packages and configure your API key securely.
# Make sure the parent claude folder has a .env file with your ANTHROPIC_API_KEY set.

from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-5"


# functions to help manage chat messages and interact with the API
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text

# Start with an empty message list
messages = []

system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

# Add the initial user question
add_user_message(messages, "How do I solve 5x + 2 = 3 for x?")

# Get Claude's response
answer = chat(messages, system=system_prompt)

print("Answer:", answer)




