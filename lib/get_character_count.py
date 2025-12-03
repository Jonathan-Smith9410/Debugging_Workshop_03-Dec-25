def get_character_count(text):
    char_count = {}

    for char in text:
        if not char_count.get(char):
            char_count[char] = 1
        else:
            char_count[char] += 1

    sorted_dict = dict(sorted(char_count.items(), key=lambda x: x[1], reverse=True))
    
    final_answer = f"The most appearing character is {list(sorted_dict.keys())[0]} and it appears {list(sorted_dict.values())[0]} times!"

    return final_answer
