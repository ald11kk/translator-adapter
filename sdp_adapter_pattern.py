# Interface
class Translator:
    def translate(self, text):
        pass

# Eng - Rus dictionary
dictionary = {
    "Hello": "Привет",
    "How are you?": "Как вы?",
    "What is your name?": "Как вас зовут?"
}

# Adapter
class DictionaryAdapter(Translator):
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def translate(self, text):
        return self.dictionary.get(text, "Перевод не найден")

class Client:
    def __init__(self, translator):
        self.translator = translator

    def translate_and_print(self, text):
        t_text = self.translator.translate(text)
        print(f"Перевод для '{text}' - '{t_text}'")

if __name__ == "__main__":
    dictionary_adapter = DictionaryAdapter(dictionary)
    client = Client(dictionary_adapter)

    text_to_translate = ["Hello", "How are you?", "What is your name?", "Goodbye"]

    for word in text_to_translate:
        client.translate_and_print(word)
