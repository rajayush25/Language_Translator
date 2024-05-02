# import cv2
# import pytesseract
# from langdetect import detect
# from googletrans import Translator, LANGUAGES
# import time  # Import the time module

# # Initialize the text recognition module (Tesseract OCR)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Initialize translator
# translator = Translator()

# def detect_language_and_translate(image, target_language):
#     # Perform text recognition using Tesseract OCR
#     text = pytesseract.image_to_string(image)
    
#     # Detect language of the recognized text
#     try:
#         detected_language = detect(text)
#     except:
#         detected_language = 'unknown'
    
#     # Check if the detected language is available for translation
#     if detected_language in LANGUAGES:
#         try:
#             translated_text = translator.translate(text, src=detected_language, dest=target_language).text
#         except Exception as e:
#             print("Translation Error:", e)
#             translated_text = "Translation Error"
#     else:
#         print("Detected language not supported for translation.")
#         translated_text = "Translation Not Supported"
    
#     # Display the original and translated text
#     print("Detected Language:", detected_language)
#     print("Original Text:", text)
#     print(f"Translated Text ({target_language}):", translated_text)

#     # Show the image with text recognized
#     cv2.imshow('Detected Text', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# def main():
#     # Access the camera
#     cap = cv2.VideoCapture(0)  # Access the device camera (0 for default camera)
    
#     start_time = time.time()  # Record the start time
#     duration = 10  # Capture frames for 10 seconds (adjust as needed)
    
#     # Get the target language input from the user
#     target_language = input("Enter the target language code (e.g., 'es' for Spanish): ").strip().lower()

#     while (time.time() - start_time) < duration:
#         ret, frame = cap.read()  # Capture frame-by-frame
#         if not ret:
#             break
        
#         # Detect language and translate text on each captured frame
#         detect_language_and_translate(frame, target_language)
    
#     # Release the camera
#     cap.release()

# if __name__ == "__main__":
#     main()
import cv2
import pytesseract
from langdetect import detect
from googletrans import Translator, LANGUAGES
import time

# Initialize the text recognition module (Tesseract OCR)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize translator
translator = Translator()

def preprocess_image(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return threshold

def detect_text_and_translate(frame, target_language):
    processed_image = preprocess_image(frame)
    extracted_text = pytesseract.image_to_string(processed_image)
    
    try:
        detected_language = detect(extracted_text)
    except:
        detected_language = 'unknown'
    
    if detected_language in LANGUAGES:
        try:
            translated_text = translator.translate(extracted_text, src=detected_language, dest=target_language).text
        except Exception as e:
            print("Translation Error:", e)
            translated_text = "Translation Error"
    else:
        print("Detected language not supported for translation.")
        translated_text = "Translation Not Supported"
    
    print("Detected Language:", detected_language)
    print("Original Text:", extracted_text)
    print(f"Translated Text ({target_language}):", translated_text)

    cv2.putText(frame, f"Detected Language: {detected_language}", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.putText(frame, f"Translated Text: {translated_text}", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    
    cv2.imshow('Text Translation', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    cap = cv2.VideoCapture(0)  # Access the device camera
    
    start_time = time.time()  # Record the start time
    duration = 10  # Capture frames for 10 seconds (adjust as needed)
    
    target_language = input("Enter the target language code (e.g., 'es' for Spanish): ").strip().lower()

    while (time.time() - start_time) < duration:
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            break
        
        detect_text_and_translate(frame, target_language)
    
    cap.release()

if __name__ == "__main__":
    main()
