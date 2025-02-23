def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    lowered_text = text.lower()
    character_counter = {} 
    for character in lowered_text:
        if character not in character_counter:
            character_counter[character] = 1
        else:
            character_counter[character] += 1
    return character_counter

def sorted_list(character_counter):
    list_from_dict = [{key: value} for key, value in character_counter.items()]
    def sort_on(dict):
        return list(dict.values())[0]

    list_from_dict.sort(reverse=True, key=sort_on)
    return(list_from_dict)


