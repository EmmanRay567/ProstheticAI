# NeuroLimb AI Diagnostic System

NeuroLimb AI is my Python based prosthetic diagnostic support tool that collects prosthetic device information, checks FDA medical device event data, calculates a risk level, and generates an AI-powered support report using the OpenAI API.

## Features

- Collects prosthetic device data from the user
- Calculates a basic risk level based on battery, motor temperature, response delay, and grip strength
- Connects to the FDA openFDA medical device event API
- Generates AI support reports using OpenAI
- Saves diagnostic reports to a local history file
- Handles input and API errors

## Technologies Used

- Python
- OpenAI API
- FDA openFDA Device Event API
- Requests
- File handling
- Modular programming

## What I Learned

While building NeuroLimb AI, I learned how to structure a Python project using multiple files and separate responsibilities between user input, AI processing, and external API communication.

I gained experience working with the OpenAI API to generate AI-powered diagnostic support reports based on structured user input. I also learned how to connect to an external medical device API using the `requests` library and include real world FDA device event data in the AI response.

This project helped me practice input validation, exception handling, file handling, API integration, and modular programming. I also learned how to think more carefully about safety-focused software by adding risk-level logic and clear disclaimers for medical-related output.

Key concepts practiced:

- Python modular programming
- OpenAI API integration
- External API requests using `requests`
- FDA medical device event data
- User input validation
- `try` / `except` error handling
- File writing and diagnostic history logs
- Risk-level classification logic
- Safety-focused AI response design

## How to Run
To run the NeuroLimb AI Diagnostic System, clone this repository to your computer using git clone https://github.com/EmmanRay567/YOUR-REPO-NAME.git.

After cloning the repository, move into the project folder using cd YOUR-REPO-NAME.

Install the required Python packages by running pip install -r requirements.txt.

This project uses the OpenAI API, so you need to set your OpenAI API key as an environment variable. On Windows PowerShell, run setx OPENAI_API_KEY "your_api_key_here".

After setting the API key, close and reopen your terminal so the new environment variable can load correctly.

Run the program with python diagnostic_ai.py.

The program will ask for prosthetic device information such as the device type, battery level, motor temperature, grip strength, response delay, calibration status, error code, and a description of the issue. After the information is entered, Lexus will generate an AI-powered diagnostic support report using the OpenAI API and FDA medical device event data.

Important: This project is an educational prototype. It is not a medical device, does not provide medical diagnosis, and should not replace advice from a doctor, prosthetist, certified technician, or manufacturer support.
