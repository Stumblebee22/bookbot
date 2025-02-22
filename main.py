from stats import get_word_count
from stats import get_character_count
from stats import sorted_list


def main():
    book_path = "books/frankenstein.txt"
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
        
    
    report = f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{character_report}============= END ==============="""
    print(report)


def get_book_text(path):
    with open(path) as f:
        return f.read()



main() 