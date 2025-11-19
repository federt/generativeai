from openai import OpenAI
from toon import encode 
import json
import os



client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

users = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}, 
    {"id": 2, "name": "Jane Doe", "email": "jane.doe@example.com"},
    {"id": 3, "name": "Mark Smith", "email": "mark.smith@example.com"},
    {"id": 4, "name": "Sarah Johnson", "email": "sarah.johnson@example.com"},
    {"id": 5, "name": "David Lee", "email": "david.lee@example.com"},
    {"id": 6, "name": "Emily Davis", "email": "emily.davis@example.com"},
    {"id": 7, "name": "Michael Brown", "email": "michael.brown@example.com"},
    {"id": 8, "name": "Olivia Wilson", "email": "olivia.wilson@example.com"},
    {"id": 9, "name": "Daniel Martinez", "email": "daniel.martinez@example.com"},
    {"id": 10, "name": "Sophia Garcia", "email": "sophia.garcia@example.com"},
    {"id": 11, "name": "James Rodriguez", "email": "james.rodriguez@example.com"},
    {"id": 12, "name": "Ava Martinez", "email": "ava.martinez@example.com"},
    {"id": 13, "name": "William Davis", "email": "william.davis@example.com"},
    {"id": 14, "name": "Isabella Wilson", "email": "isabella.wilson@example.com"},
    {"id": 15, "name": "Ethan Garcia", "email": "ethan.garcia@example.com"},
    {"id": 16, "name": "Mia Martinez", "email": "mia.martinez@example.com"},
    {"id": 17, "name": "Jacob Davis", "email": "jacob.davis@example.com"},
    {"id": 18, "name": "Oliver Wilson", "email": "oliver.wilson@example.com"},
    {"id": 19, "name": "Lucas Garcia", "email": "lucas.garcia@example.com"},
    {"id": 20, "name": "Mason Davis", "email": "mason.davis@example.com"},
]

response1 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What roles does the following users have:\n{json.dumps(users)}"}
    ]
)

response_1_tokens = response1.usage.total_tokens
response_1_output = response1.choices[0].message.content

encoded_users = encode(users)
response_2 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What roles does the following users have:\n{encoded_users}"}
    ]
)

response_2_tokens = response2.usage.total_tokens
response_2_output = response2.choices[0].message.content
print(response1.choices[0].message.content)
