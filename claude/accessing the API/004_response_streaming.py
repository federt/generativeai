# Before making any API calls, you need to install the required packages and configure your API key securely.
# Make sure the parent claude folder has a .env file with your ANTHROPIC_API_KEY set.


# Understanding Stream Events
# When you enable streaming, Claude sends back several types of events:

# MessageStart - A new message is being sent
# ContentBlockStart - Start of a new block containing text, tool use, or other content
# ContentBlockDelta - Chunks of the actual generated text
# ContentBlockStop - The current content block has been completed
# MessageDelta - The current message is complete
# MessageStop - End of information about the current message


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


# Start with an empty message list
messages = []

# Add the initial user question
add_user_message(messages, "Write a 1 sentence description of a fake database")

# Scenario 1: Stream the response from the API and print each event as it arrives
stream = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    stream=True
)

for event in stream:
    print(event)

print("----------------- Streaming Scenario 1 complete. -----------------")
print("")

# Scenario 2: Rather than printing each event, we print only the text chunks as they arrive using the SDK's simplified streaming interface
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        print(text, end="")

print("")
print("----------------- Streaming Scenario 2 complete. -----------------")
print("")

# Scenario 3: Getting the complete message for database storage after streaming
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        # Send each chunk to your client
        pass

     # Get the complete message for database storage
    final_message = stream.get_final_message()
    # Store the final message in your database
    print(final_message)    

print("")
print("----------------- Streaming Scenario 3 complete. -----------------")