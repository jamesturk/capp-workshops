#!/usr/bin/env python3
import argparse
from statistics import mean
from weather import get_weather_json


def print_forecast(weather):
    print("Forecast:")
    for day in weather["forecast"]:
        print(f"{day['date']}: {day['description']}")
        print(f"  Temp: {day['temperature_f']}F")
        print(f"  Precipitation: {day['precipitation']}")
        print(f"  Humidity: {day['humidity']}")


def print_summary(weather):
    forecast = weather["forecast"]
    avg_temp = mean([day["temperature_f"] for day in forecast])
    # count days with chance of rain > 10%
    precip_days = len([day for day in forecast if day["precipitation"] > 10])

    print(f"The average temperature will be {avg_temp}F.")
    print(f"There will be {precip_days} days with a chance of rain.")


def print_current(weather):
    print("Current weather:")
    print(f"  Temp: {weather['current']['temperature_f']}F")
    print(f"  Precipitation: {weather['current']['precipitation']}")
    print(f"  Humidity: {weather['current']['humidity']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("city", help="the city to get the weather for")
    args = parser.parse_args()
    weather = get_weather_json(args.city)
    if weather:
        print_current(weather)
        print_forecast(weather)
        print_summary(weather)
    else:
        print(f"Could not get weather for {args.city}")


if __name__ == "__main__":
    main()
