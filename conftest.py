import pytest
from src.routes.request import PlankaRequests
from utils.config import BASE_URI, USER_EMAIL, USER_PASSWORD



@pytest.fixture(scope="session")
def get_token():
    url = f"{BASE_URI}/access-tokens"
    payload = {
            "emailOrUsername": USER_EMAIL,
            "password": USER_PASSWORD
    }
    print("PAYLOAD", payload)
    headers = {'Content-Type': 'application/json'}
    response = PlankaRequests.post(url, headers, payload)
    response_json = response.json()
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    access_token = response_json['item']
    return access_token











    
