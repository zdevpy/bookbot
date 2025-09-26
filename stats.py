def sort_all_char_data(unsorted_dict:dict={}) -> dict:
    sorted_dicts = []
    for k, v in unsorted_dict.items():
        if k.isalpha() == True:
            sorted_dicts.append({"char": k, "num": v})

    sorted_dicts.sort(reverse=True, key=sort_on)
    return sorted_dicts

def sort_on(data):
    return data["num"]

def get_word_count(book_contents:str=None):
    list_of_words = book_contents.split()
    num_words = len(list_of_words)
    return f"Found {num_words} total words"

def get_all_chars_counts(book_contents:str=None):
    results = {}

    for c in book_contents:
        lower_c = c.lower()
        if lower_c not in results.keys():
            results[lower_c] = 1
            continue 
        results[lower_c] += 1

    return results
