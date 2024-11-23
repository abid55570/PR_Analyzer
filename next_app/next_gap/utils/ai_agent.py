import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

def analyze_code_with_llm(file_content, file_name):
    key = os.getenv('GROQ_API_KEY')
    if not key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    prompt = f"""
        Analyze the following code for :
        - code style and formatting issues
        - Potential bugs and error
        - Performance improvements
        - Best Practices
        
    File : {file_name}
    Content : {file_content}
    
    Provide a detailed JSON output with the structure
    {{
        "issues" : [
            {{
                "type" : "<style|bugs|performance|best_practice>",
                "line" : <line_number>,
                "description" : "<description>",
                "suggestion" : "<suggestions>"
            }}
        ]
    }}
    """

    client = Groq(api_key=key)
    completion = client.chat.completions.create(
        model="llama-3.2-11b-text-preview",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,  # Lower temperature for more consistent output
        top_p=1
    )
    
    # Parse the response and return JSON
    try:
        response_content = completion.choices[0].message.content
        # You might need to clean/parse the response to get valid JSON
        return response_content
    except Exception as e:
        print(f"Error parsing LLM response: {str(e)}")
        return {"issues": []}