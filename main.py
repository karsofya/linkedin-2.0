from textblob import Word, TextBlob

def check_word_spelling(word: str):

    word_checker = Word(word)
    result = word_checker.spellcheck()
    print(result)

    if word == result[0][0] and result[0][1] == 1:
        print(f'Spelling of "{word}" is correct!')
    else:
        print(f'Spelling of "{word}" is not correct!')    
        print(f'correct spelling of "{word}": "{result[0][0]}" (with {round(result[0][1], 2)} confidence)')

def check_text_spelling(text: str):
    text_checker = TextBlob(text)
    print (text_checker)
    print(text_checker.correct()) 


if __name__ == "__main__":
   print("Starting spelling check..")
   #check_word_spelling(input("Enter word: "))
   check_text_spelling(input("Enter text: "))
