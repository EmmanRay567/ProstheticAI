from tkinter import EventType

import requests

def SearchDeviceEvents(device_type):
    url = "https://api.fda.gov/device/event.json"

    SearchFilter = {
        "search": f'device.generic_name:"{device_type}"',
        "limit": 10

    }

    try:
        response = requests.get(url, params=SearchFilter)
        data = response.json()

        if "results" not in data:
            return "No FDA device event reports found for this device type."

        eventInfo = ""

        for event in data["results"]:
            EventType = event.get("event_type", "No event type available")
            date_received = event.get("date_received", "No date available")
            report_number = event.get("report_number", "No report number available")

            eventInfo += f"""
Event Type: {EventType}
Date Received: {date_received}
Report Number: {report_number}
"""

        return eventInfo
    except requests.exceptions.RequestException as e:
          return f"Network error while accessing FDA Device Event API: {e}"
    except Exception as e:
        return f"FDA Device Event API Error: {e}"
