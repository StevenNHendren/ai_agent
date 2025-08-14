import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python_file
from functions.call_function import call_function

#system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


def main():
    print("Hello from ai-agent!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file
        ]
    )
    if (len(sys.argv) > 1):
        user_prompt = sys.argv[1]
        if (user_prompt != ""):
            messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
            ]
            response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
            )
        else:
            print("Error: prompt not provided")
            sys.exit(1)
    else:
        print("Error: prompt not provided")
        sys.exit(1)
    x = response.usage_metadata.prompt_token_count
    y = response.usage_metadata.candidates_token_count
    calls = response.function_calls
    if calls != None:
        for call in calls:
            fc = genai.types.FunctionCall(
                name=call.name,
                args=call.args
            )                                      
            print(f"Calling function: {fc.name}({fc.args}) \n")
            if (len(sys.argv) > 2):
                if (sys.argv[2] == "--verbose"):
                    function_call_result = call_function(fc, verbose=True)
                    print(f"-> {function_call_result.parts[0].function_response.response}")  
                else:
                    function_call_result = call_function(fc)
            if function_call_result.parts[0].function_response.response == None:
                raise Exception(f"fatal error executing function {function_call_part.name}")

    print(response.text)
    if (len(sys.argv) > 2):
        if (sys.argv[2] == "--verbose"):
            print (f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {x}")
            print(f"Response tokens: {y}")

if __name__ == "__main__":
    main()
