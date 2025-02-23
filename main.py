from stats import (
    get_word_count,
    get_character_count,
    sorted_list,
)
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    character_count = get_character_count(text)
    message = f"{num_words} words found in the document"
    neat_sorted_list = sorted_list(character_count)
    character_report = ""
    for char_dict in neat_sorted_list:
        char = list(char_dict.keys())[0]
        count = list(char_dict.values())[0]
        if char.isalpha(): 
            character_report += f"{char}: {count}\n"
    print_report(book_path, num_words, character_report)    

def print_report(book_path, num_words, character_report):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(f"{character_report}")
    print("============= END ===============")




def get_book_text(path):
    with open(path) as f:
        return f.read()
      


main() 