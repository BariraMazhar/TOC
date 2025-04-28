import string

class LanguageDFA:
    def __init__(self):
        self.language_patterns = {
            "English": {"the", "is", "and", "hello", "how", "are", "you", "good", "morning"},
            "Spanish": {"el", "es", "y", "hola", "como", "estas", "buenos", "dias"},
            "French": {"le", "est", "et", "bonjour", "comment", "ça", "va", "merci"},
            "Urdu": {"ہیلو", "آپ", "کیسے", "ہیں", "صبح", "اچھی", "شب", "بخیر"},
            "German": {"der", "ist", "und", "hallo", "wie", "gehts", "danke"},
            "Italian": {"il", "è", "e", "ciao", "come", "stai", "grazie", "buongiorno"},
            "Hindi": {"नमस्ते", "कैसे", "हो", "आप", "शुभ", "सुप्रभात"},
            "Arabic": {"مرحبا", "كيف", "حالك", "السلام", "عليكم", "صباح", "الخير"}
        }

    def clean_text(self, text):
        # Convert text to lowercase and remove punctuation
        text = text.lower().translate(str.maketrans("", "", string.punctuation))
        return set(text.split())

    def identify_language(self, text):
        words = self.clean_text(text)  
        detected_language = None
        max_matches = 0

        for language, patterns in self.language_patterns.items():
            matches = len(words.intersection(patterns))
            if matches > max_matches:
                max_matches = matches
                detected_language = language

        return detected_language if detected_language else "Unknown"
