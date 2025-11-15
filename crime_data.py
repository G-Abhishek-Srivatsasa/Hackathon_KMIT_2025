# crime_data.py
import requests
import os

API_URL = "https://api.data.gov.in/resource/15150682-a9ed-475d-b0e3-67b292e90d22"
API_KEY = "579b464db66ec23bdd000001c41215f69f6e45c77a7692ec62171327"

def fetch_crime_data():
    """
    Fetches state-wise IPC crime rate for 2022.
    Builds a lookup dictionary: {state: crime_rate}
    """
    params = {
        "api-key": API_KEY,
        "format": "json",
        "limit": 100,
        "offset": 0
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        crime_lookup = {}
        for record in data.get("records", []):
            state = record["state_ut"]
            rate = record["rate_of_cognizable_crimes__ipc___2022_"]
            crime_lookup[state.strip().lower()] = rate

        return crime_lookup

    except Exception as e:
        print("Error fetching crime data:", e)
        return {}

# Fetch data ONCE when app starts
CRIME_DATA_CACHE = fetch_crime_data()

def get_crime_rate(state):
    """
    Returns crime rate for a given state.
    Returns None if not found.
    """
    if not state:
        return None
    return CRIME_DATA_CACHE.get(state.strip().lower())
