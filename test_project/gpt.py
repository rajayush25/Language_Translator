import cv2
import pytesseract
from langdetect import detect
import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image):
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

# Function to interact with ChatGPT API
def process_with_chatgpt(text):
    endpoint = "https://api.openai.com/v1/completions"
    api_key = "API Key Here"  # Replace with your ChatGPT API key

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "text-davinci-003",
        "prompt": text,
        "max_tokens": 50
    }

    response = requests.post(endpoint, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return None

# Function to process image and update GUI
# Function to process image and update GUI
def process_image():
    # Capture frame from camera
    ret, frame = cap.read()

    # Convert frame to grayscale for better OCR results
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extract text from the image
    extracted_text = extract_text_from_image(gray)

    # Pass extracted text to ChatGPT
    chatgpt_response = process_with_chatgpt(extracted_text)

    try:
        # Detect language
        detected_language = detect(extracted_text)
    except Exception as e:
        detected_language = "Language detection error: " + str(e)

    # Update GUI
    text_output.config(state=tk.NORMAL)
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, f"Extracted Text: {extracted_text}\n")
    text_output.insert(tk.END, f"Detected Language: {detected_language}\n")
    text_output.insert(tk.END, f"ChatGPT Response: {chatgpt_response}\n")
    text_output.config(state=tk.DISABLED)

    # Update video feed in GUI
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(frame)
    frame = ImageTk.PhotoImage(frame)
    video_label.imgtk = frame
    video_label.configure(image=frame)
    video_label.after(10, process_image)


# Create GUI window
root = tk.Tk()
root.title("Text Recognition and Language Detection")
root.geometry("800x600")

# Create video feed label
video_label = tk.Label(root)
video_label.pack(padx=10, pady=10)

# Create output text area
text_output = tk.Text(root, wrap=tk.WORD, height=10, state=tk.DISABLED)
text_output.pack(padx=10, pady=(0, 10), fill=tk.BOTH, expand=True)

# Set up camera interface
cap = cv2.VideoCapture(0)

# Start processing frames from camera
process_image()

# Run GUI
root.mainloop()

# Release the camera
cap.release()
