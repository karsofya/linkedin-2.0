from textblob import Word
import re

def check_word_spelling(word):

    word = Word(word)

    result = word.spellcheck()

    if word == result[0][0]:
        print(f'Spelling of "{word}" is correct!')
    else:
        print(f'Spelling of "{word}" is not correct!')    
        print(f'correct spelling of "{word}": "{result[0][0]}" (with {round(result[0][1], 2)} confidence)')

if __name__ == "__main__":
   print("Starting spelling check..")
   check_word_spelling(input("Enter word: "))
