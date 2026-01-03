import os
from google import genai
from dotenv import load_dotenv

load_dotenv(".env.local")

# Initialize the client correctly
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def get_chatbot_response(user_input):
    try:
        # Define the prompt
        user_prompt = f"The user is feeling: {user_input}. Suggest a movie vibe."
        
        # CORRECT SYNTAX for google-genai 1.0+ 
        response = client.models.generate_content(
            model="gemini-2.0-flash", # Use 2.0 or 3-flash if available in your region
            contents=user_prompt
        )
        
        return response.text
        
    except Exception as e:
        return f"Error: {e}"

# Simple test
if __name__ == "__main__":
    vibe = input("How are you feeling? ")
    if vibe:
        print("\n--- Gemini's Recommendation ---")
        print(get_chatbot_response(vibe))
    else:
        print("Please enter a mood!")