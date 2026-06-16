from ProstheticAI import GiveDiagnosticReport

ConvoEnd = False

print("Welcome to your Prosthetic Diagnostic AI! My name is Lexus.")

while not ConvoEnd:
    print("\nEnter prosthetic diagnostic information below.")

    try:
        device_type = input("Enter prosthetic device type: ")
        battery_level = int(input("Enter battery level percentage: "))
        motor_temp = float(input("Enter motor temperature in Celsius: "))
        grip_strength = input("Enter grip strength status: ")
        response_delay = float(input("Enter response delay in seconds: "))
        calibration_status = input("Enter calibration status: ")
        error_code = input("Enter error code if any: ")
        user_symptom = input("Describe the issue: ")

        risk_level = "LOW"

        if motor_temp >= 70 or response_delay >= 2.0:
            risk_level = "HIGH"
        elif battery_level < 30 or grip_strength.lower() == "weak":
            risk_level = "MEDIUM"

        user_symptom = user_symptom + f"\nCalculated Risk Level: {risk_level}"

        print("\n--- Prosthetic Diagnostic Report ---")
        print("Device Type:", device_type)
        print("Battery Level:", battery_level, "%")
        print("Motor Temperature:", motor_temp, "°C")
        print("Grip Strength:", grip_strength)
        print("Response Delay:", response_delay, "seconds")
        print("Calibration Status:", calibration_status)
        print("Error Code:", error_code)
        print("User Symptom:", user_symptom)
        print("Risk Level:", risk_level)

        ai_report = GiveDiagnosticReport(
            device_type,
            battery_level,
            motor_temp,
            grip_strength,
            response_delay,
            calibration_status,
            error_code,
            user_symptom
        )

        print("\n--- Lexus AI Support Report ---")
        print(ai_report)

        file = open("diagnostic_history.md", "a")
        file.write("\n--- Lexus AI Support Report ---\n")
        file.write(ai_report)
        file.write("\n-----------------------------\n")
        file.close()

        user_choice = input("\nWould you like to run another diagnostic? yes/no: ")

        if user_choice.lower() == "no":
            ConvoEnd = True
            print("Lexus: Diagnostic session ended. Stay safe.")

    except ValueError:
        print("Lexus: Invalid input. Battery level must be a whole number, and motor temperature/response delay must be numbers.")
