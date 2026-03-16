import json
from ibm_watson import WatsonxAgenticAI

class WatsonxAPI:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def create_agent(self, agent_data):
        url = f"{self.api_url}/agents"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.post(url, headers=headers, json=agent_data)
        return response.json()

    def get_agent(self, agent_id):
        url = f"{self.api_url}/agents/{agent_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def update_agent(self, agent_id, agent_data):
        url = f"{self.api_url}/agents/{agent_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.put(url, headers=headers, json=agent_data)
        return response.json()
