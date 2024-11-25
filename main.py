def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    generate_book_stat_report(filepath,word_count,char_count)


def get_book_text(filepath):
    '''
    Gets the text from a given filepath.
    '''
    try:
        with open(filepath) as f:
            return f.read()
    except Exception as e:
        return e

def count_words(text):
    '''
    Gives the count of words given a string.
    '''
    try:
        word_count = text.split()
        return len(word_count)
    except Exception as e:
        return e

def count_characters(text):
    '''
    Takes text and returns the number of times each character appears in the string.
    '''
    if text:
        text = text.lower()
        unique_character_count = {}

        for char in text:
            if char in unique_character_count:
                unique_character_count[char] += 1
            else:
                unique_character_count[char] = 1

        return unique_character_count
    else:
        raise Exception("you can't submit blank text!")

def generate_book_stat_report(filepath,word_count,char_count):
    '''
    Just a general report. Added a lil bit of logic to handle newlines
    '''
    char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    print('\|||/' * 15)
    print(f'--- Begin reporting stats for text found at {filepath} ---')
    print(f'There were {word_count} found in this text.')
    for key in char_count:
        if key == '\n':
            key_fix = 'Newline'
            print (f'The {key_fix} character ("\\n") was found {char_count[key]} times.')
        elif key == " ":
            key_fix = 'Space'
            print(f'The {key_fix} character (" ") was found {char_count[key]} times.')
        else:
            print (f'The {key} character was found {char_count[key]} times.')
    print("--- End reporting stats ---")
    print('\|||/' * 15)
main()