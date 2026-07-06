import os
from dotenv import load_dotenv
from google import genai

load_dotenv()  # reads .env file and makes gemini api key available via the os.getenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# ceates a connection object authenticated with the api key
response = client.models.generate_content(  # the actual api call
    model="gemini-2.5-flash",  # model picks which gemini model answers
    # content is the prompt the user enters
    contents="Explain what a knowledge base assistant is, in one sentence."

)

print(response.text)
