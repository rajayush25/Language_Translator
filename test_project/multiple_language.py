import cv2
import pytesseract
from PIL import Image
from googletrans import Translator, LANGUAGES
import tkinter as tk
import os

# Set the path to Tesseract's tessdata directory
os.environ['TESSDATA_PREFIX'] = 'C:/Program Files/Tesseract-OCR/tessdata/'

# Custom language code mapping
custom_language_codes = {
    'eng': 'English',
    'pan': 'Punjabi',
    'ben': 'Bengali',
    'mar': 'Marathi',
    'tel': 'Telugu',
    'tam': 'Tamil',
    'guj': 'Gujarati',
    'hin': 'Hindi',
    'kan': 'Kannada',
    'mal': 'Malayalam',
    'ori': 'Odia',
    'urd': 'Urdu'
    # Add more language codes and names as needed
}

# Function to perform OCR on the image and extract text
def ocr_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

# Function to detect language of the extracted text
def detect_language(text):
    translator = Translator()
    try:
        detected = translator.detect(text)
        lang_code = detected.lang
        lang_name = LANGUAGES.get(lang_code, 'Unknown')
        return lang_name
    except Exception as e:
        print("Language detection error:", e)
        return "Language detection error"

# Function to translate text to the selected regional language
def translate_text(text, dest_lang):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_lang)
        return translated.text
    except Exception as e:
        print("Translation error:", e)
        return "Translation error occurred"

# Function to capture an image using the system's camera
def capture_image():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('captured_image.jpg', image)
    del camera
    return 'captured_image.jpg'

# Function triggered when translation button is clicked
def translate():
    # Capture an image using the system's camera
    image_path = capture_image()

    # Extract text from the captured image
    extracted_text = ocr_image(image_path)

    # Detect language of the extracted text
    detected_language = detect_language(extracted_text)

    # Get the selected regional language
    selected_language = language_var.get()
    selected_language_code = [code for code, name in custom_language_codes.items() if name == selected_language][0]

    # Translate the detected text to the selected regional language
    translated_text = translate_text(extracted_text, selected_language_code)

    # Display translated text and detected language in the text box
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, f"Detected Language: {detected_language}\n")
    text_box.insert(tk.END, f"Extracted Text: {extracted_text}\n\n")
    text_box.insert(tk.END, f"Selected Language: {selected_language}\n")
    text_box.insert(tk.END, f"Translated Text: {translated_text}\n\n")

# GUI setup
root = tk.Tk()
root.title("Image Translator")

# Language selection dropdown
language_var = tk.StringVar(root)
language_var.set("English")

# List of supported regional languages
regional_languages = ['English', 'Punjabi', 'Bengali', 'Marathi', 'Telugu', 'Tamil', 'Gujarati', 'Hindi', 'Kannada', 'Malayalam', 'Odia', 'Urdu']

language_dropdown = tk.OptionMenu(root, language_var, *regional_languages)
language_dropdown.pack()

# Translated text display
text_box = tk.Text(root, height=10, width=50)
text_box.pack()

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack()

root.mainloop()
