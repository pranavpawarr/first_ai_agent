import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from config import SYSTEM_PROMPT
from call_function import available_functions, call_function


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    max_iterations = 20
    
    for iteration in range(max_iterations):
        if verbose:
            print(f"\n--- Iteration {iteration + 1} ---")
        
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions], 
                    system_instruction=SYSTEM_PROMPT
                ),
            )
            
            if verbose:
                print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                print("Response tokens:", response.usage_metadata.candidates_token_count)
            
            # Add the model's response to messages
            for candidate in response.candidates:
                messages.append(candidate.content)
            
            # Handle function calls FIRST (before checking for text)
            if response.candidates[0].content.parts:
                has_function_calls = any(
                    hasattr(part, 'function_call') and part.function_call 
                    for part in response.candidates[0].content.parts
                )
                
                if has_function_calls:
                    function_responses = []
                    
                    for part in response.candidates[0].content.parts:
                        if hasattr(part, 'function_call') and part.function_call:
                            # Print function name even when not verbose
                            print(f" - Calling function: {part.function_call.name}")
                            
                            function_response_content = call_function(part.function_call, verbose=verbose)
                            
                            # Extract the function response part
                            try:
                                function_response_part = function_response_content.parts[0]
                                function_responses.append(function_response_part)
                                
                                if verbose:
                                    response_data = function_response_part.function_response.response
                                    print(f"-> {response_data}")
                            except (AttributeError, IndexError):
                                raise RuntimeError("Function call did not return a valid response.")
                    
                    # Add all function responses as a single user message
                    if function_responses:
                        tool_message = types.Content(
                            role='user',
                            parts=function_responses
                        )
                        messages.append(tool_message)
                    continue  # Continue to next iteration
            
            # Check if we got a final text response (no function calls)
            if response.text:
                print("Final response:")
                print(response.text)
                break
            else:
                # No function calls and no text - something unexpected happened
                print("Warning: No function calls or text in response")
                break
                
        except Exception as e:
            print(f"Error during generation: {e}")
            break
    
    else:
        # Loop completed without breaking (max iterations reached)
        print(f"Warning: Reached maximum iterations ({max_iterations}) without completion")
if __name__ == "__main__":
    main()