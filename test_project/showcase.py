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

    # Translate the extracted text to the selected language
    if selected_lang == 'Marathi':
        translated_text = translate_text(extracted_text, 'en', 'mr')
    elif selected_lang == 'Gujarati':
        translated_text = translate_text(extracted_text, 'en', 'gu')
    elif selected_lang == 'Hindi':
        translated_text = translate_text(extracted_text, 'en', 'hi')
    elif selected_lang == 'Bengali':
        translated_text = translate_text(extracted_text, 'en', 'bn')
    elif selected_lang == 'Punjabi':
        translated_text = translate_text(extracted_text, 'en', 'pa')
    elif selected_lang == 'Tamil':
        translated_text = translate_text(extracted_text, 'en', 'ta')
    elif selected_lang == 'Telugu':
        translated_text = translate_text(extracted_text, 'en', 'te')
    elif selected_lang == 'Kannada':
        translated_text = translate_text(extracted_text, 'en', 'kn')
    elif selected_lang == 'Malayalam':
        translated_text = translate_text(extracted_text, 'en', 'ml')
    elif selected_lang == 'Odia':
        translated_text = translate_text(extracted_text, 'en', 'or')
    elif selected_lang == 'Urdu':
        translated_text = translate_text(extracted_text, 'en', 'ur')
    elif selected_lang == 'Sanskrit':
        translated_text = translate_text(extracted_text, 'en', 'sa')

    # Display translated text in the text box
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, translated_text)

# GUI setup
root = tk.Tk()
root.title("Image Translator")

# Language selection dropdown
language_var = tk.StringVar(root)
language_var.set("Select Language")

language_dropdown = tk.OptionMenu(root, language_var, "Marathi", "Gujarati", "Hindi", "Bengali", "Punjabi", "Tamil", "Telugu", "Kannada", "Malayalam", "Odia", "Urdu", "Sanskrit")
language_dropdown.pack()

# Translated text display
text_box = tk.Text(root, height=10, width=50)
text_box.pack()

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack()

root.mainloop()
