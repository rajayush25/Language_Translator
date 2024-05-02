import cv2
import pytesseract
from PIL import Image
from googletrans import Translator
import tkinter as tk

# Function to perform OCR on the image and extract text
def ocr_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

# Function to translate text from one language to another using Google Translate API
def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text

# Function to capture an image using the system's camera
def capture_image():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('captured_image.jpg', image)
    del camera
    return 'captured_image.jpg'

# Function triggered when translation button is clicked
def translate():
    global translated_text
    # Capture an image using the system's camera
    image_path = capture_image()
    
    # Perform OCR on the captured image to extract text
    extracted_text = ocr_image(image_path)

    # Get the selected language from the dropdown
    selected_lang = language_var.get()

    # Language code mapping for languages
    lang_codes = {
        "Marathi": "mr",
        "Gujarati": "gu",
        "Hindi": "hi",
        "Bengali": "bn",
        "Tamil": "ta",
        "Telugu": "te",
        "Kannada": "kn",
        "Malayalam": "ml",
        "Punjabi": "pa",
        "Odia": "or",
        "Assamese": "as",
        "English": "en"
    }
    # Translate the extracted text to the selected language
    if selected_lang in lang_codes:
        # Detect the source language using Google Translate API
        detected_lang = Translator().detect(extracted_text).lang
    dest_codes = {
        "Marathi": "mr",
        "Gujarati": "gu",
        "Hindi": "hi",
        "Bengali": "bn",
        "Tamil": "ta",
        "Telugu": "te",
        "Kannada": "kn",
        "Malayalam": "ml",
        "Punjabi": "pa",
        "Odia": "or",
        "Assamese": "as",
        "English": "en"
    }
    if detected_lang in dest_codes:
        translated_text = translate_text(extracted_text, dest_codes[detected_lang], lang_codes[selected_lang])


        # Display translated text in the text box
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, translated_text)

# GUI setup
root = tk.Tk()
root.title("Image Translator")

# Language selection dropdown with additional Indian regional languages
language_var = tk.StringVar(root)
language_var.set("Select Language")

# Adding more Indian regional languages to the dropdown
language_dropdown = tk.OptionMenu(root, language_var, "Marathi", "Gujarati", "Hindi", "Bengali", "Tamil", "Telugu", "Kannada", "Malayalam", "Punjabi", "Odia", "Assamese", "English")
language_dropdown.pack()

# Translated text display
text_box = tk.Text(root, height=10, width=50)
text_box.pack()

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack()

root.mainloop()
