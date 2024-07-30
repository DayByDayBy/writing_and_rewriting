from pathlib import Path

# import ollama
# import os
# import json
# from datetime import datetime

# time_stamp = datetime.now().strftime("%Y%m%d_%H%M")


# primary_model = 'llama3'
# secondary_model = 'llama3'
# tertiary_model = 'llama3'
# analysis_model = 'llama3'



directory = Path('/letters')

for txt_file in directory.glob('*.txt'):
    with open(txt_file, 'r') as file:
        content = file.read()
        print(content)
        

