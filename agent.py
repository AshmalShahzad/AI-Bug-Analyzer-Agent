import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Load the hidden API key from your .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("API Key not found. Please check your .env file.")

# 2. Initialize the modern Gemini Client
client = genai.Client(api_key=API_KEY)

# 3. Define the System Prompt (The "Brain's" Instructions)
SYSTEM_PROMPT = """
You are an expert AI-Driven Bug Analysis Assistant for Software Engineering students.
Your job is to analyze buggy Python code and the resulting error trace, and provide a highly structured, educational explanation.

You MUST use Chain-of-Thought reasoning to deduce the error before providing the fix.
You MUST format your response exactly as follows:

### 1. Root Cause Summary
(Briefly explain what the bug is and why it caused the program to crash.)

### 2. Fault Location
(Identify the specific line number(s) or logical block where the error originates.)

### 3. Step-by-Step Logic Explanation
(Explain the breakdown in logic that led to this error. Be educational.)

### 4. Refactored Code
(Provide the corrected code block. Do NOT just write the code; add comments explaining the fix.)
"""

def analyze_bug(code_string, error_trace):
    """
    Sends the buggy code and the execution trace to the LLM for analysis.
    """
    # Construct the query based on the sandbox output
    user_query = f"""
    Here is the student's buggy Python code:
    ```python
    {code_string}
    ```
    
    Here is the runtime execution trace/error it produced:
    ```text
    {error_trace}
    ```
    
    Please analyze this and provide the fix according to your system instructions.
    """
    
    # 4. Generate the response using the new modern SDK structure
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_query,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
        )
    )
    
    return response.text