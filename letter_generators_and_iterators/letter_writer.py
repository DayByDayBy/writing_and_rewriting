import ollama
# from langchain_community.llms import Ollama
import os
import json
from datetime import datetime

time_stamp = datetime.now().strftime("%Y%m%d_%H%M")

# several model options even tho they are the same for now, so i can lean 
# on various models strengths/weaknesses to get nmore useful/intersting results

primary_model = 'llama3'
secondary_model = 'llama3'
tertiary_model = 'llama3'
analysis_model = 'llama3'

# starting with one fairly silly, basic prompt for testing purposes, 
# eventual prompt will be more complex, possibly stored differently

initial_prompt = 'write me a short but persuasive letter extolling the virtues of using large language models for writing letters'

cv = './info/cv.txt'
# jd = '.info/jd/txt'

def generate_new_text():
    response = ollama.generate(model=primary_model, prompt = initial_prompt)    
    filename = f'letters/{primary_model}_at_{time_stamp}.txt'
    with open(filename, 'w') as file:
        file.write("initial prompt: \n")
        file.write(initial_prompt + "\n\n")
        file.write(f"response: {response['response']}\n\n")
        
if __name__ == '__main__':

    print('\n')
    print('generating letter...')
    generate_new_text()
    print('\n')
    print('letter generated')
    
# nice basic print formatting, likely uneccessary once the other parts are built, but handy fpr debug etc