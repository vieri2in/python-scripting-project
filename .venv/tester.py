from  translate import Translator
translator = Translator(to_lang='ja')
try:
    with open("text.txt", mode='r') as my_file:
        text = my_file.read()
        tranlation = translator.translate(text)
        with open("text_copy.txt", mode='w') as my_file2:
            my_file2.write(tranlation)
except FileNotFoundError as err:
    print("File not found")

