import os
import subprocess
from google import genai
from google.genai import types

def call_function(function_call_part, verbose=False):
  if verbose:
    print(f"Calling function: {function_call_part.name}({function_call_part.args})")
  else:
    print(f" - Calling function: {function_call_part.name}")

  #if function name is invalid
  return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"error": f"Unknown function: {function_name}"},
        )
    ],
  )

  
  return types.Content(
      role="tool",
      parts=[
          types.Part.from_function_response(
              name=function_name,
              response={"result": function_result},
          )
      ],
  )
