import requests

# Replace with the desired URL
for i in range(10001):
    url = "https://www.cloudoplus.com"

    # Make a GET request
    response = requests.get(url)

    # Print status code and content
    print(f"Status Code: {response.status_code}")
    print(f"Response Body:\n{response.text}")
    print("hello world")