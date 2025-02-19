def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    character_count = get_character_count(text)
    
    print(character_count)

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    lowered_text = text.lower()
    character_counter = {} 
    for character in lowered_text:
        if character not in character_counter:
            character_counter[character] = 0
        if character in character_counter:
            character_counter[character] +=1 
    return character_counter




def get_book_text(path):
    with open(path) as f:
        return f.read()



main() 