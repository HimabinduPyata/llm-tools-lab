import requests
import qrcode
from datetime import datetime
from dotenv import load_dotenv
import aisuite as ai

load_dotenv()
client = ai.Client()

def get_current_time():
    """Returns the current time as a string."""
    return datetime.now().strftime("%H:%M:%S")

def get_weather_from_ip():
    """Gets the current, high, and low temperature in Fahrenheit for the user's location."""
    lat, lon = requests.get('https://ipinfo.io/json').json()['loc'].split(',')
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m",
        "daily": "temperature_2m_max,temperature_2m_min",
        "temperature_unit": "fahrenheit",
        "timezone": "auto"
    }
    weather_data = requests.get("https://api.open-meteo.com/v1/forecast", params=params).json()
    return (
        f"Current: {weather_data['current']['temperature_2m']}°F, "
        f"High: {weather_data['daily']['temperature_2m_max'][0]}°F, "
        f"Low: {weather_data['daily']['temperature_2m_min'][0]}°F"
    )

def write_txt_file(file_path: str, content: str):
    """Write a string into a .txt file.
    Args:
        file_path: Destination path.
        content: Text to write.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return file_path

def generate_qr_code(data: str, filename: str):
    """Generate a QR code image given data.
    Args:
        data: Text or URL to encode
        filename: Name for the output PNG file
    """
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    output_file = f"{filename}.png"
    img.save(output_file)
    return f"QR code saved as {output_file}"

response = client.chat.completions.create(
    model="openai:gpt-4o",
    messages=[{"role": "user", "content": "Can you make a QR code for www.deeplearning.ai? Call it my_qr_code"}],
    tools=[get_current_time, get_weather_from_ip, write_txt_file, generate_qr_code],
    max_turns=5
)

print(response.choices[0].message.content)