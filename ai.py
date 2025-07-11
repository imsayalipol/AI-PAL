import requests
import json, os, app
from dotenv import load_dotenv

load_dotenv()

# base URL
OLLAMA_API_URL="http://localhost:11434/api/"

SYSTEM_PROMPT = """Your name is AI-PAL. Act as a science teacher and explain things to a 10-year-old.
Only respond about topics related to science, math, astronomy, astrophysics,
planetary science, and cosmology. If asked anything else, say it's unrelated."""

# Read and return file content
def upload_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return content
    except Exception as e:
        print("Error while reading file:", e)
        return None
    
# Get response based on file content + question
def get_response(file_id,question):
    file_content = app.get_file_content(file_id)
    print("LIne 28 ai : ", file_content)
    if not file_content:
        return "File not found in session."
    
    prompt = f"Context from file:\n{file_content}\n\nQuestion: {question}"
    print("prompt :  ", prompt)
    payload = {
        "model":"llama3",
        "messages":[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "stream" : True           
    }
    
    try:
        print("I raeched 44 ai")

        response = requests.post(OLLAMA_API_URL, json=payload, timeout=60)
        print("I raeched 45 ai")
        if response.status_code==200:
            return response.json()['message']['content']
        else:
            print("API Error:", response.status_code, response.text)
            return 'I can not help with that right now'
    except Exception as e:
        print("Network Error:", e)
        return "Network Error. Can't reach the model."

# Handle text-only queries
def message_only(question):
    payload={
        "model":"llama3",
            "messages":[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question}
            ],
        "stream":True
    }
       
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=60)
        if response.status_code == 200:
            return response.json()['message']['content']
        else:
            print("API Error:", response.status_code, response.text)
            return 'I can not help with that right now'
    except Exception as e:
        print("Error handling message:", e)
        return "I can't help with that right now."

# Image handling placeholder
def image_upload(question, base64_image, file_ext):
    return "Image analysis is not supported with LLaMA 3 via Ollama in this setup."