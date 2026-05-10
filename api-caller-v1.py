import google.generativeai as genai
from PIL import Image

genai.configure(api_key="")
model = genai.GenerativeModel('gemini-2.5-flash')

img = Image.open('chart_screenshot.JPG')
img2=Image.open('12.AXISCADES.png')
img3=Image.open('32.AFFLE.png')

response = model.generate_content(["you are an stock expert, identify pattern like breakouts, consolidations, or potential reversals or anything else in images attached in this", img, img2, img3])

print(response.text)
