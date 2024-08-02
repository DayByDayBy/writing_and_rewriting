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
to help you, here is an example of a previous attempt that was scored 9/25:

Dear [Recipient],

Imagine being able to craft letters that not only convey your ideas with precision but also resonate with your audience on a deeper level. Letters that are infused with creativity, flair, and a hint of personality. This is no longer the stuff of imagination, thanks to the advent of large language models.

These powerful tools have the potential to revolutionize the art of letter-writing, allowing you to tap into a vast repository of knowledge, inspiration, and linguistic expertise. With a large language model by your side, every letter becomes an opportunity to showcase your unique voice, perspective, and passion.

The benefits are twofold. Firstly, these models can help you overcome the most common hurdles in writing – finding the right words, structuring your thoughts, and avoiding errors. No longer will you struggle with writer's block or worry about embarrassing typos. The model's algorithms will guide you through the process, ensuring that your letter is polished, engaging, and error-free.

Secondly, large language models grant you access to a treasure trove of knowledge and inspiration. Need to make a compelling case? The model can draw upon centuries of historical precedent, scientific research, and literary masterworks to furnish you with a wealth of relevant examples and analogies. Want to surprise your recipient with some witty wordplay or clever allusions? The model's got the inside scoop on the latest memes, pop culture references, and linguistic innovations.

But here's the thing: using large language models is not just about convenience – it's about elevating your correspondence to new heights. It's an opportunity to connect with your audience on a deeper level, showcase your creativity and flair, and leave a lasting impression. So why settle for ordinary letters when you can craft extraordinary ones?

In short, the benefits of using large language models for writing letters are too compelling to ignore. They offer a game-changing combination of precision, creativity, and convenience that can help you achieve your goals and exceed your expectations.

So why wait? Give large language models a try today, and discover a whole new world of writing possibilities at your fingertips.

Sincerely,

[Your Name]

-----

when scored, it was marked down in large part for being too much of a 'sales pitch'.*

endeavour to do better, ideally to achieva score of 20+/25.

*
in discussion afterwards an idea was considered: as the marking scheme is unkown and teh feedback limited, it is hard to discern the exact reason for the low score. indeed, the task may even have 'hidden' parameters that the client was unable or unwilling to articulate; if so, to excel may require the task to be figured out and then completed, rather than simply completed. of course, it was agreed, the only way to learn more would be through repeat attempts, and comparing failure and sucess.


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
    
# nice basic print formatting, likely uneccessary once the other parts are built, but handy for debug etc