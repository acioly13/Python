from translate import Translator

translator = Translator(to_lang="pt")
translation = translator.translate("This is a pen.")

print(translation)