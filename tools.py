
import json
from PyPDF2 import PdfReader
from openai import OpenAI
import streamlit as st

def resume_into_json(resume):
    pdf_reader = PdfReader(resume)
    text=""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    client = OpenAI()

    prompt = f" don't give any explantion. please analyze and convert file data from this {text} into  json, remove data like name, email or personal information and  please return only json file  "

    response = client.chat.completions.create(
            model="gpt-4-0125-preview",
              response_format={ "type": "json_object" },  # Adjust the model identifier as needed
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": prompt}
        ],temperature=0.2
    )
    
    
    return json.loads(response.choices[0].message.content)