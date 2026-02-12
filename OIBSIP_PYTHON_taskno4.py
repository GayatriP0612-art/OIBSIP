import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

# Simple weather code to emoji mapping (WMO codes)
def get_weather_icon(code):
    icons = {
        0: "☀️", 1: "🌤️", 2: "⛅", 3: "☁️",
        45: "🌫️", 48: "🌫️", 51: "🌧️", 61: "🌧️", 71: "❄️",
        80: "🌦️", 95: "⛈️"
    }
    return icons.get(code, "🌍")

def fetch_weather(city, units="celsius"):
    try:
        # Get coordinates
        geo = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1").json()
        if not geo.get("results"):
            messagebox.showerror("Error", "City not found!")
            return None, None
        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]
        city_name = geo["results"][0]["name"]

        # Current weather + forecast
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&hourly=temperature_2m,weather_code&daily=temperature_2m_max,temperature_2m_min,weather_code&timezone=auto"
        data = requests.get(url).json()

        return data, city_name
    except:
        messagebox.showerror("Error", "Failed to fetch weather data.")
        return None, None

def show_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    data, city_name = fetch_weather(city)
    if not data:
        return

    unit = "°C" if unit_var.get() == "celsius" else "°F"
    temp = data["current"]["temperature_2m"]

    # Current weather
    code = data["current"]["weather_code"]
    icon = get_weather_icon(code)
    humidity = data["current"]["relative_humidity_2m"]
    wind = data["current"]["wind_speed_10m"]

    current_label.config(text=f"{icon} {city_name}\n{temp}{unit} | Humidity: {humidity}% | Wind: {wind} km/h")

    # Hourly forecast (next 6 hours)
    hourly_text = "Hourly:\n"
    for i in range(6):
        time = data["hourly"]["time"][i][11:16]  # HH:MM
        t = data["hourly"]["temperature_2m"][i]
        hourly_text += f"{time}: {t}{unit}\n"
    hourly_label.config(text=hourly_text)

    # Daily forecast
    daily_text = "7-Day Forecast:\n"
    for i in range(7):
        day = datetime.fromisoformat(data["daily"]["time"][i]).strftime("%a %d")
        max_t = data["daily"]["temperature_2m_max"][i]
        min_t = data["daily"]["temperature_2m_min"][i]
        daily_text += f"{day}: {max_t} / {min_t}{unit}\n"
    daily_label.config(text=daily_text)

# GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("420x620")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Weather App", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=15)

tk.Label(root, text="Enter City:", bg="#f0f0f0").pack()
city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=8)

unit_var = tk.StringVar(value="celsius")
tk.Radiobutton(root, text="Celsius", variable=unit_var, value="celsius", bg="#f0f0f0").pack()
tk.Radiobutton(root, text="Fahrenheit", variable=unit_var, value="fahrenheit", bg="#f0f0f0").pack()

tk.Button(root, text="Get Weather", font=("Arial", 12), bg="#4CAF50", fg="white", command=show_weather).pack(pady=15)

current_label = tk.Label(root, text="", font=("Arial", 16), bg="#f0f0f0", justify="center")
current_label.pack(pady=10)

hourly_label = tk.Label(root, text="", font=("Arial", 11), bg="#f0f0f0", justify="left")
hourly_label.pack(pady=10, padx=20, anchor="w")

daily_label = tk.Label(root, text="", font=("Arial", 11), bg="#f0f0f0", justify="left")
daily_label.pack(pady=10, padx=20, anchor="w")

root.mainloop()