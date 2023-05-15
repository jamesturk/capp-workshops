#!/usr/bin/env python3
import json
import argparse
from statistics import mean
from weather import get_weather_json

"""
A simple script to get the weather for a city and print it out.

How many bugs could it possibly have?

Run it with a city name as an argument, e.g.:

    python3 main.py Chicago
    python3 main.py Seattle
    python3 main.py NYC
    python3 main.py Paris (this one should print an error)

"""


def print_forecast(weather):
    print("Forecast:")
    for day in weather["forecast"]:
        print(f" {day['date']}: {day['description']}")
        print(f"    Temp: {day['temperature_f']}F")
        print(f"    Precipitation: {day['precipitation']}")
        print(f"    Humidity: {day['humidity']}")


def print_summary(weather):
    forecast = weather["forecast"]
    # BUG #2: avg_temp did not properly handle days with no temperature
    avg_temp = mean([day["temperature_f"] for day in forecast if day["temperature_f"]])
    # count days with chance of rain > 10%
    # BUG #3: precip days are counted incorrectly, because the precipitation is 0-1 not 0-100
    precip_days = len([day for day in forecast if day["precipitation"] > .1])

    # figure out if the temperature is rising or falling monotonically
    last_temp = None
    trend = set()
    for day in forecast:
        temp_f = day["temperature_f"]
        # BUG #4: temperature trend is not calculated correctly because
        # last_temp is not initialized to the first day's temperature
        if not last_temp:
            last_temp = temp_f
            continue
        if not temp_f or not last_temp:
            continue
        elif temp_f > last_temp:
            trend.add("rising")
        elif temp_f < last_temp:
            trend.add("falling")
        elif temp_f == last_temp:
            trend.add("steady")
        last_temp = temp_f

    # if trend is consistent, display it, otherwise ???
    if len(trend) == 1:
        trend = trend.pop()
    else:
        trend = "???"

    print(f"The average temperature will be {avg_temp}F.")
    print(f"There will be {precip_days} days with a chance of rain.")
    print(f"The trend for the week is {trend}.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("city", help="the city to get the weather for")
    args = parser.parse_args()
    weather = get_weather_json(args.city)
    # BUG #1: weather is a string, not a dict
    weather = json.loads(weather)
    if weather:
        print_forecast(weather)
        print_summary(weather)
    else:
        print(f"Could not get weather for {args.city}")


if __name__ == "__main__":
    main()
