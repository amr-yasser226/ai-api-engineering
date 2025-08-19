from openai import OpenAI
import os

# Read API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable")

# Create the OpenAI client
client = OpenAI(api_key=api_key)

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "prompt"}
  ]
)

print(response.choices[0].message.content)
