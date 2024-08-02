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
to help you, here is an example of a previous attempt that was scored 11/25:

Dear [Recipient],

As someone who values thoughtful communication, you know how important it is to craft letters that not only convey your ideas but also resonate with your audience. The art of letter-writing is a delicate balance between precision and personality, creativity and clarity.

Large language models can be a valuable tool in achieving this balance. By tapping into the collective knowledge and linguistic expertise of these powerful tools, you can elevate your correspondence to new heights. But rather than simply relying on them for convenience or efficiency, I'd like to suggest that using large language models is an opportunity to reflect on what we mean by effective communication.

At its core, effective communication involves more than just conveying information – it's about connecting with others on a deeper level. Large language models can help you tap into this connection by providing access to a vast repository of knowledge and inspiration. Whether you're seeking to make a compelling case or craft a witty response, these tools can furnish you with the relevant examples and analogies to get your point across.

Of course, using large language models is not without its challenges. One of the most significant hurdles is navigating the tension between relying on technology and maintaining individual voice and perspective. As someone who values authentic communication, I believe it's essential to approach this challenge head-on.

In my own writing experience, I've found that large language models can be a valuable starting point for exploring complex ideas and refining my thoughts. However, it's equally important to remember that these tools are not a substitute for human insight and empathy. Ultimately, effective communication involves more than just relying on algorithms – it requires us to connect with others on a fundamental level.

So what does this mean for your letter-writing experience? I'd argue that using large language models is not simply about convenience or efficiency but rather an opportunity to explore the boundaries of effective communication. By embracing this challenge, you can craft letters that resonate with your audience in new and meaningful ways.

In short, the benefits of using large language models for writing letters are indeed compelling – but only when approached from a perspective that values authentic communication, individual voice, and human connection.

Sincerely,

[Your Name]

-----

this attempt was given the feedback "it doesn't have any character, i don't really get a sense of the author"

endeavour to do better, ideally to achieva score of 20+/25.


(in discussion after the last attempt, an idea was considered: as the marking scheme is unkown and the feedback limited, it is hard to discern the exact reason for a given score. indeed, the task may even have 'hidden' parameters that the client is unable or unwilling to articulate; if so, a well-marked attempt may require the task to be figured out first and then completed, rather than simply completed. of course, it was agreed, the only way to learn more would be through repeat attempts, and comparing failure and sucess.)


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