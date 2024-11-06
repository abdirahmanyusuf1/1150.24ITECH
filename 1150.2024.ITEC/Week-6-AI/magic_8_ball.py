import requests

# Ask the user for their question
question = input("Ask the Magic 8 Ball a question: ")

# Prepare the API URL with the question parameter
url = f"https://magic-8-ball-mctc.uc.r.appspot.com/8ball?question={question}"

# Send the GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the response from the API
    data = response.json()
    print("Magic 8 Ball says:", data.get("answer"))
else:
    print("Failed to get a response from the Magic 8 Ball. Please try again.")
