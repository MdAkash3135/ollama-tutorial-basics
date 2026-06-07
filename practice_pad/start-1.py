import requests
import json

url = 'http://localhost:11434/api/generate'

# Add 'stream': False directly inside the data payload
data = {
    'model': 'llama3.2',
    'prompt': 'tell me a short story and make it funny',
    'stream': False  # <--- Crucial fix here
}

# You don't strictly need stream=False in requests.post anymore, 
# but keeping it doesn't hurt.
response = requests.post(url=url, json=data)

# This will now work perfectly without throwing an error
print(response.json())