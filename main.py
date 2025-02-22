from stats import get_word_count
from stats import get_character_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    character_count = get_character_count(text)
    message = f"{num_words} words found in the document"
    
    print(character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()



main() 