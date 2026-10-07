import requests

URL = "https://api.weatherapi.com/v1/current.json"
KEY = "ad6b6fa408c74561940143210260710"
FILTERING = {
    "q": "Paris",
    "key": KEY
}
HEADERS = {
    "Accept": "application/json",
}


def get_weather() -> None:
    return requests.get(url=URL, params=FILTERING, headers=HEADERS).json()


if __name__ == "__main__":
    print(get_weather())
