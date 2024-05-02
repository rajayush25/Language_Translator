from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text
    return translated_text

if __name__ == "__main__":
    # Get user input text
    input_text = input("Enter the text to translate: ")

    # Get target language from user
    target_language = input("Enter the language code of the desired Indian regional language (e.g., hi for Hindi): ")

    # Translate the input text
    translated_text = translate_text(input_text, target_language)

    # Print the translated text
    print("Translated text:")
    print(translated_text)
