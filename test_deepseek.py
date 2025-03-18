# Please install OpenAI SDK first: `pip3 install openai`


from openai import OpenAI

deepseek_api = 'sk-de48a6e00e6c46be89c2137a770abb27'

client = OpenAI(api_key=deepseek_api, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)