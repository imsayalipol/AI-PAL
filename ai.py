import ollama
import logging
from dotenv import load_dotenv
import os

# Load environment variables (not needed for Ollama, but may be used elsewhere)
load_dotenv()

SYSTEM_PROMPT = """Your name is WALL-E. Act as a science teacher and explain things to a 10-year-old.
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
def get_response(question, file_content):
    prompt = f"Context from file:\n{file_content}\n\nQuestion: {question}"
    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )
        return response['message']['content']
    except Exception as e:
        print("Failed to get response:", e)
        return "I can't help with that right now."

# Handle text-only queries
def message_only(question):
    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question}
            ]
        )
        return response['message']['content']
    except Exception as e:
        print("Error handling message:", e)
        return "I can't help with that right now."

# Image handling placeholder
def image_upload(question, base64_image, file_ext):
    return "Image analysis is not supported with LLaMA 3 via Ollama in this setup."