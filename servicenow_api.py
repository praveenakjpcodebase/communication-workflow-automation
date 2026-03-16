import requests

class ServiceNOWAPI:
    def __init__(self, instance, username, password):
        self.instance = instance
        self.username = username
        self.password = password

    def create_ticket(self, ticket_data):
        url = f"https://{self.instance}.service-now.com/api/now/table/incident"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.username}:{self.password}"
        }
        response = requests.post(url, headers=headers, json=ticket_data)
        return response.json()

    def get_ticket(self, ticket_id):
        url = f"https://{self.instance}.service-now.com/api/now/table/incident/{ticket_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.username}:{self.password}"
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def update_ticket(self, ticket_id, ticket_data):
        url = f"https://{self.instance}.service-now.com/api/now/table/incident/{ticket_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.username}:{self.password}"
        }
        response = requests.put(url, headers=headers, json=ticket_data)
        return response.json()
