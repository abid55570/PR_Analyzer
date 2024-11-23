
# convert in base64
import base64
from urllib.parse import urlparse
code_str = ''

# print(base64.b64decode(code_str).decode())



# def get_owner_and_repo(url):
#     passed_url = urlparse(url)
#     path_parts = passed_url.path.strip("/").split("/")
#     if len(path_parts) >=2 :
#         owner, repo = path_parts[0], path_parts[1]
#         return owner, repo
#     return None,None
#
# print(get_owner_and_repo('https://github.com/ArcLogiQ/matchx_api/pulls'))

from groq import Groq

key = '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'


def analyze_code_with_llm(file_content,file_name):
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
    ```json
    """

    client = Groq(
        api_key=key
    )
    completion = client.chat.completions.create(
        model="llama-3.2-11b-text-preview",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        top_p=1
    )
    print(completion.choices[0].messages.content)

analyze_code_with_llm((base64.b64decode(code_str).decode()), "model.py")