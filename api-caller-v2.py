import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key="")
model = genai.GenerativeModel('gemini-2.5-flash')

folder_path = 'D:\\Equities-ShareMarket\\tradingview_screenshotter\screenshots\\2026-05-09_17-25'
uploaded_files = []

# 1. Upload files to Gemini's storage
for filename in os.listdir(folder_path):
    if filename.endswith((".png", ".jpg")):
        full_path = os.path.join(folder_path, filename)
        print(f"Uploading {filename}...")
        sample_file = genai.upload_file(path=full_path, display_name=filename)
        uploaded_files.append(sample_file)

#print('total uploaded files:', uploaded_files.length)
# 2. Analyze all uploaded files
response = model.generate_content([
    "Analyze these charts. Return a table with columns: Symbol, Primary Pattern, Support Level, RSI Status, and Verdict (Buy/Wait/Ignore)",
    *uploaded_files
])

print(response.text)