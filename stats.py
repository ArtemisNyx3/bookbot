def get_num_words(book_text: str) -> int:
    book_words = book_text.split()
    return len(book_words)

def get_character_frequency(book_text: str) -> dict:
    frequency_dict = {}
    # lower case
    book_text = book_text.lower() 
    for ch in book_text:
        keys = frequency_dict.keys()
        if ch in keys:
            frequency_dict[ch] += 1
        else: 
            frequency_dict[ch] = 1
    return frequency_dict

def sort_dict(freq_dict:dict):
    # remove nonaplha
    rem_list = []
    for x in freq_dict.keys():
        if not x.isalpha():
            rem_list.append(x)
    for key in rem_list:
        freq_dict.pop(key)
    return sorted(freq_dict.items() ,key=lambda x:x[1], reverse=True)
