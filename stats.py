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