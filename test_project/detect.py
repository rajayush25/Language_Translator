import cv2
import pytesseract
from langdetect import detect_langs

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change this path to your Tesseract installation directory

# Function to detect text language
def detect_language(text):
    try:
        lang = detect_langs(text)[0]
        return lang.lang
    except:
        return "Unknown"

# Function to process camera feed
def process_camera_feed():
    # Initialize camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Use Tesseract to perform OCR
        text = pytesseract.image_to_string(gray)

        # Detect language
        language = detect_language(text)

        # Display the detected text and language on the frame
        cv2.putText(frame, "Detected Text: " + text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, "Detected Language: " + language, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Camera Feed', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Main function
if __name__ == "__main__":
    process_camera_feed()
