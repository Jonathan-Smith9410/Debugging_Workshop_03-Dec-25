def get_character_count(text):
    char_count = {}

    for char in text:
        if not char_count.get(char):
            char_count[char] = 1
        else:
            char_count[char] += 1

    sorted_dict = dict(sorted(char_count.items(), key=lambda x: x[1], reverse=True))
    
    return list(sorted_dict.keys())[1]
