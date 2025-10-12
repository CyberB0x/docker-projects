import requests


def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

if __name__ == "__main__":
    city = input("Введите город: ")
    print(get_weather(city))

