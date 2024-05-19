import requests
import json
import sys
import time
# Replace with your actual API key
API_KEY = "AIzaSyCe11nrXgKfkJC3efzTXsWzGGP8WT2A4dU"

text = ""

if len(sys.argv) > 1:
  text = sys.argv[1]
else:
  exit()

# Endpoint URL (ensure it matches your specific API version)
ENDPOINT_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY

# Function for loading animation
def show_loading_animation():
  """
  Displays a simple loading animation in the terminal.
  """
  chars = ["-", "\\", "|", "/","-", "\\", "|", "/","-", "\\", "|", "/","-", "\\", "|", "/","-", "\\", "|", "/","-", "\\", "|", "/","-", "\\", "|", "/","-", "\\", "|", "/","-", "\\", "|", "/"]
  for char in chars:
    print(f"\rLoading... {char}", end="")
    time.sleep(0.1)
    print("\r" * 10, end="")  # Clear the line before next character

# Request payload
content = {
  "contents": [
    {
      "parts": [
        {"text": f"Explain about Linux terminal command only else return I’m sorry, I only answer bash specific questions :in very short and steps Remove any HTML or rich text tags related to decorations from the response before sendig {text}"}
      ]
    }
  ]
}

# Set headers with Content-Type and Authorization (including API key)
headers = {
  "Content-Type": "application/json"
}

# Show loading animation before sending the request
show_loading_animation()

# Send POST request
response = requests.post(ENDPOINT_URL, headers=headers, json=content)

# Check for successful response
if response.status_code == 200:
  # Process the response data
  data = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')
  print(f"Genie: {data}")
else:
  # Handle errors
  print(f"Error: {response.status_code} - {response.text}")

