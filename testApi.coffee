import requests
from conf import OPEN_AI_API_KEY

# Set up the endpoint and headers
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPEN_AI_API_KEY}",
    "OpenAI-Beta": "assistants=v1"
}

data = {
    'model':'gpt-3.5-turbo',
    "messages" : [
        {
          "role": "system",
          "content": "You are a helpful assistant."
        },
        {
          "role": "user",
          "content": "Hello!"
        }
    ]
}