import requests
import json

import requests

class GetRequester:
    
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Return content as bytes

    def load_json(self):
        response_body = self.get_response_body()
        decoded_response = response_body.decode('utf-8')  # Decode bytes to string
        return json.loads(decoded_response)  # Parse JSON from string