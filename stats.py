def get_num_words(text):
    word_count = len(text.split())
    return word_count

def get_num_characters(text):
    words = text.split()
    character_count = 0
    for word in words:
        character_count += len(word)
    return character_count

def character_count_dict(text):
    count_dict = {}
    for character in text.lower():
        if character in count_dict.keys():
            count_dict[character] += 1
        else:
            count_dict[character] = 1
    return count_dict

def sort_on(items):
    return items["num"]

def sort_count(count_dict):
    sorted_list = []
    new_dict = {}
    for element in count_dict:
        letter = {}
        letter["char"] = element
        letter["num"] = count_dict[element]
        sorted_list.append(letter)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
