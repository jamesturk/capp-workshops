import json

# no need to change or modify this file, it is a mock data source
# assume it behaves like a real API

mock_data = [
    {
        "city": "Chicago",
        "current": {
            "description": "clear sky",
            "temperature_f": 62,
            "precipitation": 0,
            "humidity": 0.77,
        },
        "forecast": [
            {
                "date": "2022-05-02",
                "description": "clear sky",
                "temperature_f": 62,
                "precipitation": 0,
                "humidity": 0.77,
            },
            {
                "date": "2022-05-03",
                "description": "cloudy",
                "temperature_f": 52,
                "precipitation": 0,
                "humidity": 0.80,
            },
            {
                "date": "2022-05-04",
                "description": "showers",
                "temperature_f": 53,
                "precipitation": 0.4,
                "humidity": 0.82,
            },
            {
                "date": "2022-05-05",
                "description": "rain",
                "temperature_f": 55,
                "precipitation": 0.8,
                "humidity": 0.85,
            },
        ],
    },
    {
        "city": "New York",
        "current": {
            "description": "clear sky",
            "temperature_f": 68,
            "precipitation": 0,
            "humidity": 0.77,
        },
        "forecast": [
            {
                "date": "2022-05-02",
                "description": "clear sky",
                "temperature_f": 68,
                "precipitation": 0,
                "humidity": 0.77,
            },
            {
                "date": "2022-05-03",
                "description": "cloudy",
                "temperature_f": 58,
                "precipitation": 0,
                "humidity": 0.80,
            },
            {
                "date": "2022-05-04",
                "description": "sunny",
                "temperature_f": None,
                "precipitation": 0,
                "humidity": 0.82,
            },
            {
                "date": "2022-05-05",
                "description": "sunny",
                "temperature_f": None,
                "precipitation": 0.1,
                "humidity": 0.90,
            },
        ],
    },
    {
        "city": "Seattle",
        "current": {
            "description": "rain",
            "temperature_f": 55,
            "precipitation": 0.8,
            "humidity": 0.85,
        },
        "forecast": [
            {
                "date": "2022-05-02",
                "description": "rain",
                "temperature_f": 55,
                "precipitation": 0.8,
                "humidity": 0.85,
            },
            {
                "date": "2022-05-03",
                "description": "rain",
                "temperature_f": 55,
                "precipitation": 0.8,
                "humidity": 0.85,
            },
            {
                "date": "2022-05-04",
                "description": "rain",
                "temperature_f": 55,
                "precipitation": 0.8,
                "humidity": 0.85,
            },
            {
                "date": "2022-05-05",
                "description": "rain",
                "temperature_f": 55,
                "precipitation": 0.8,
                "humidity": 0.85,
            },
        ],
    },
]


def get_weather_json(city):
    """
    Given a city return JSON weather data for that city.
    """
    for data in mock_data:
        if data["city"] == city:
            return json.dumps(data)
    else:
        return json.dumps({"error": "City not found"})
