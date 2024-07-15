import requests

API_KEY = "50752b6f213cf13caf46f5ba51f8f224"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    observations = 8 * forecast_days
    filtered_data = filtered_data[:observations]
    return filtered_data


if __name__ == "__main__":
    print(get_data("place", "forecast_days"))