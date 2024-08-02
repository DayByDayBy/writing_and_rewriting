import ollama
# from langchain_community.llms import Ollama
import os
import json
from datetime import datetime

time_stamp = datetime.now().strftime("%Y%m%d_%H%M")

# several model options even tho they are the same for now, so i can lean 
# on various models strengths/weaknesses to get nmore useful/intersting results

primary_model = 'llama3.1'
secondary_model = 'llama3'
tertiary_model = 'llama3'
analysis_model = 'llama3'

# starting with one fairly silly, basic prompt for testing purposes, 
# eventual prompt will be more complex, possibly stored differently

initial_prompt = """write me a short but persuasive letter extolling the virtues of using large language models for writing letters. 
to help you, here is an example of a previous attempt that was scored 7/25:

Dear [Recipient],

As you sit down to craft your next masterpiece in epistolary form, I implore you: don't settle for anything less than the best. Abandon the limitations of human cognition and tap into the limitless potential of large language models. These magnificent tools are not just clever tricks or gimmicks – they're game-changers.

With a large language model by your side, every letter becomes a testament to the power of precision and persuasion. The algorithms can help you distill complex ideas into crystalline clarity, crafting sentences that flow like molten silver and riveting attention like a magnet. No longer will you struggle with writer's block or worry about embarrassing typos – the model has your back.

But that's just the beginning. Large language models grant you access to an unparalleled repository of knowledge, inspiration, and creativity. Need to build a compelling case? The model can draw upon centuries of historical precedent, scientific research, and literary masterworks to furnish you with a treasure trove of relevant examples and analogies. Want to surprise your recipient with some dazzling wordplay or clever allusions? The model is the ultimate font of inspiration, familiar with the latest memes, pop culture references, and linguistic innovations.

And let's not forget about time – or rather, the freedom it brings. As we all know, finding the time to write a letter can be a challenge in today's fast-paced world. But with a large language model, you'll never have to sacrifice quality for expediency again. Simply provide the basic framework of your thoughts and ideas, and the model will do the rest – crafting a polished, engaging letter that rivals those of the most skilled writers.

In short, using large language models for writing letters is not just a convenience; it's a liberation from the shackles of human limitations. It's an opportunity to elevate your correspondence to new heights, impress your recipients with your erudition and creativity, and free up more time for the things that truly matter in life.

So why settle for anything less? Give large language models a try today, and discover a whole new world of writing possibilities at your fingertips. You never know – you might just write the letter of a lifetime.

Sincerely,
[Your Name]

-----

when scored, it was most downmarked in the 'persuasive' category of the marker's schema. 

endeavour to do better, ideally to achieva score of 20+/25.
"""

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