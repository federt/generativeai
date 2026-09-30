# Before making any API calls, you need to install the required packages and configure your API key securely.
# Make sure the parent claude folder has a .env file with your ANTHROPIC_API_KEY set.

from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-5"

message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]
)

print(message.content[0].text)