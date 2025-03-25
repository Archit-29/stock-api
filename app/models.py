
import google.generativeai as genai
import os

API_KEY = os.getenv("GEMINI_API_KEY")  
genai.configure(api_key=API_KEY)

llm = genai.GenerativeModel("gemini-2.0-flash")

try:
    response = llm.generate_content("Hello, how are you?")
except Exception as e:
    print("Error:", e)

