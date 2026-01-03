import sys
from api_client import get_weather

def display_weather(data):
    print("\nWeather Report")
    print("----------------")
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']} °C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

def main():
    if len(sys.argv) < 2:
        print("Please enter a city name")
        return

    city = sys.argv[1]
    result = get_weather(city)

    if "error" in result:
        print("Error:", result["error"])
    else:
        display_weather(result)

if __name__ == "__main__":
    main()
