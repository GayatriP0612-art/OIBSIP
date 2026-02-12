# OIBSIP
IN THIS REPOSITORY IT INCLUDES THE TASKS COMPLETED IN OVERALL INTERNSHIP.

**THE TECHNOLOGIES OR THE SOFTWARE USED DURING TASKS COMPLETION ARE:**
1. PROG LANG USED IS PYTHON.
2. IDE USED :- PYCHARM

TASKS THAT ARE COMPLETED UNDER THIS REPOSITORY ARE AS WELL AS THE FEATURES OF IT:

**TASK NO 1:-VOICE ASSISTANT**:- 

**📝 Features of the Voice Assistant Code**:-
**Speech Output (TTS)**

Uses pyttsx3 for text-to-speech.

Customizable voice (male/female) and speaking rate.

Speaks responses aloud and prints them to console.

**Speech Input (STT)**

Uses speech_recognition to capture voice commands via microphone.

Handles ambient noise adjustment.

Configurable energy threshold for sensitivity.

Supports Indian English (en-IN) recognition.

**Error Handling in Listening**

Detects timeout if user doesn’t speak.

Handles unrecognized speech gracefully.

Reports network issues.

Catches unexpected audio errors.

**Core Functionalities**

Greetings: Responds to "hello" or "hi".

Time & Date: Speaks current time and date.

Wikipedia Search: Fetches and summarizes information (2 sentences).

Web Search: Opens Google search results in browser.

YouTube Playback: Plays requested videos using pywhatkit.

Exit Command: Stops assistant when user says "exit", "stop", or "bye".

**Fallback Response**

If command is not recognized, assistant says it doesn’t know how to help yet.
   

**TASK NO 2:-BMI CALCULATOR:- **

**BMI Calculation**
Takes weight (kg) and height (cm) as input.

Validates inputs (positive values, height between 100–250 cm).

Computes BMI and displays both value and category.

**BMI Categories**

Underweight (<18.5)

Normal weight (18.5–24.9)

Overweight (25–29.9)

Obese (≥30)

**History Tracking**

Saves each calculation into a CSV file (bmi_history.csv).

Records date/time, weight, height, BMI, and category.

Creates file with headers if it doesn’t exist.

**History Viewer**

Opens a new window showing past BMI records in a text widget.

Provides a button to view BMI trend graph.

**Trend Graph**

Uses Matplotlib to plot BMI values over time.

Displays dates vs. BMI with markers, grid, and rotated labels.

Embeds the graph inside a Tkinter window.

**User Interface**

Built with Tkinter (labels, entry fields, buttons).

Styled buttons and labels for readability.

Fixed window size (400x500) for consistency.

Separate windows for history and graph.

**Error Handling**

Shows error messages for invalid inputs.

Displays info messages when history is empty.

**History Management**

Includes a “Clear History” button to delete the CSV file.   


**TASK NO 3:- RANDOM PASSWORD GENERATOR:- **

**📝 Features**

**Password Length Control**

User sets desired length (minimum 8, up to 50).

Validation ensures length is at least 8.

Character Type Selection

**Options to include/exclude:**

Letters (uppercase + lowercase)

Numbers

Symbols (punctuation)

Each type has a minimum count requirement (e.g., at least 2 numbers).

**Exclude Specific Characters**

User can input characters to avoid (e.g., oO0 to prevent confusion).

**Randomized Password Generation**

Ensures minimum requirements are met first.

Fills remaining slots with random characters from selected sets.

Shuffles final password for randomness.

**Error Handling**

Alerts if:

Length < 8

Minimum requirements exceed total length

No character type selected

**Clipboard Integration**

Generated password can be copied directly to clipboard.

Confirmation message shown after copying.

**User Interface (Tkinter GUI)**

Clean layout with labels, spinboxes, checkboxes, and entry fields.

Buttons for Generate and Copy to Clipboard.

Result displayed in a label with wrapping for readability.

Fixed window size (400x450) for consistency.

**TASK NO 4:- BASIC WEATHER APP:- **

**📝 Features**

**City-based Weather Lookup**

User enters a city name.

App fetches latitude/longitude using Open-Meteo’s geocoding API.

Displays proper city name if found, or error if not.

**Current Weather Display**

Shows temperature, humidity, wind speed, and weather condition.

Uses simple emoji icons for weather codes (☀️, 🌧️, ❄️, etc.).

Supports unit selection: Celsius or Fahrenheit.

**Hourly Forecast**

Displays next 6 hours of temperature and weather codes.

Shows time in HH:MM format.

**Daily Forecast**

Provides a 7-day forecast.

Shows max/min temperatures for each day.

Displays day name and date (e.g., Mon 16).

**Error Handling**

Alerts if city is not found.

Handles API failures gracefully with error messages.

**User Interface (Tkinter GUI)**

Clean layout with labels, entry fields, radio buttons, and buttons.

Styled with background color and fonts.

Organized sections for current weather, hourly forecast, and daily forecast.

Fixed window size (420x620) for consistency.

**TASK NO 5:- CHAT APPLICATION:- **

**📝 Features**
**🔹 Server-Side**
**Socket Setup**

Runs on 127.0.0.1 (localhost) and port 55555.

Listens for incoming client connections.

**Client Management**

Maintains lists of active clients and their nicknames.

Sends a request (NICK) to each new client to collect their nickname.

Broadcasts join/leave messages to all connected clients.

**Message Broadcasting**

Any message received from a client is sent to all other clients.

Ensures real-time group chat functionality.

**Threaded Handling**

Each client runs in its own thread for simultaneous communication.

Prevents blocking and allows multiple users to chat at once.

**Disconnection Handling**

Detects when a client disconnects.

Removes them from the active lists.

Notifies others that the user has left the chat.

**🔹 Client-Side**
**Connection**

Connects to the server at 127.0.0.1:55555.

Prints confirmation message once connected.

****Messaging****

Allows user to type and send messages to the server.

Messages are broadcast to all other connected clients.

**Exit Command**

User can type quit to leave the chat.

Closes the socket connection cleanly.
