import argparse
import os
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise Exception("Could not find API key for Gemini")
    
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=args.user_prompt
    )

    if response.usage_metadata:
        prompt_token_count = response.usage_metadata.prompt_token_count
        candidates_token_count = response.usage_metadata.candidates_token_count

        print(f"Prompt tokens: {prompt_token_count}")
        print(f"Response tokens: {candidates_token_count}")
        print(f"Response: {response.text}")
    else:
        raise RuntimeError("Prompt failed to return a response")


if __name__ == "__main__":
    main()
