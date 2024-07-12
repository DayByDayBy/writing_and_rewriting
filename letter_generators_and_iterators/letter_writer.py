import ollama
import os
import json
from datetime import datetime

cv = './info/cv.txt'
# jd = '.info/jd/txt'

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])