import google.generativeai as genai
from PIL import Image

genai.configure(api_key="")
model = genai.GenerativeModel('gemini-2.5-flash')

img = Image.open('chart_screenshot.JPG')
response = model.generate_content(["Is this stock chart showing a breakout? Give me a Buy/Sell verdict.", img])

print(response.text)
