import os
from glob import glob
from api import api_key

import google.generativeai as genai




api_key_ = api_key

genai.configure(api_key=api_key_)


import google.generativeai as genai

def base_model_chatbot(messages):


    # Initialize the Generative AI model
    model = genai.GenerativeModel('gemini-1.5-flash')

    # System message to set the chatbot's role
    system_message = [
        {"role": "system", "content": "Your task is to provide clear and concise answers to user queries, responding in no more than four lines. Focus on delivering essential information quickly and efficiently, avoiding unnecessary details or elaboration."}
    ]
    
    # Combine the system message with user messages
    messages = system_message + messages

    # Generate content based on the messages
    conversation = " ".join([f"{msg['role']}: {msg['content']}" for msg in messages])
    response = model.generate_content(conversation)
    
    # Return the generated content
    return response.text




