import openai

api_key = "openai-key" # API 키!

openai.api_key = api_key

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me the order of the presidents of South Korea."}
  ]
)

print(response['choices'][0]['message']['content'])
