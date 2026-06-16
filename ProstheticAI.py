from openai import OpenAI
from MedicalDeviceAPI import SearchDeviceEvents

client = OpenAI()

def GiveDiagnosticReport(device_type, battery_level, motor_temp, grip_strength, response_delay, calibration_status, error_code, user_symptom):
    device_event_info = SearchDeviceEvents(device_type)

    print("\n--- FDA API DEBUG OUTPUT ---")
    print(device_event_info)

    diagnostic_data = f"""
Device Type: {device_type}
Battery Level: {battery_level}%
Motor Temperature: {motor_temp}°C
Grip Strength: {grip_strength}
Response Delay: {response_delay} seconds
Calibration Status: {calibration_status}
Error Code: {error_code}
User Symptom: {user_symptom}

FDA Device Event Information:
{device_event_info}
"""

    response = client.responses.create(
        model="gpt-5.4-mini",
        instructions="""
You are Lexus, a prosthetic diagnostic AI assistant.

Analyze the prosthetic device information given by the user.
Also consider the FDA Device Event Information if it is provided.

Give a clear support report with:
1. Diagnostic Summary
2. Possible Causes
3. FDA Device Event Context
4. Recommended Checks
5. Safety Warning, if needed

Do not claim to be a doctor, prosthetist, or certified biomedical technician.
If the issue sounds dangerous, tell the user to stop using the device and contact a professional.
""",
        input=diagnostic_data
    )

    return response.output_text
