from openai import OpenAI

# Create the OpenAI client
client = OpenAI(api_key="<YOUR_OPENAI_API_KEY>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", 
     "content": "prompt"}
  ]
)

print(response.choices[0].message.content)