import requests
from config import API_KEY, BASE_URL

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 404:
            return {"error": "City not found"}

        elif response.status_code == 401:
            return {"error": "Unauthorized – Invalid API key"}

        else:
            return {"error": "Server error"}

    except requests.exceptions.RequestException:
        return {"error": "Network error"}
