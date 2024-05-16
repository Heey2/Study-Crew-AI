import openai

openai.api_key = "openai-key" # API 키!

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant. Answer in Korean."},
    {"role": "user", "content": "Tell me the order of the presidents of South Korea."}
  ]
)

print(response['choices'][0]['message']['content'])
