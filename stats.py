def sort_all_char_data(unsorted_dict:dict, reverse:bool=False) -> dict:
    """Take the unsorted keys and values from unsorted_dict and convert
    to a sorted list of dictionaries.

    Sort options are:
        - least to greatest (default).
        - greatest to least (reverse=True)

    Args:
        unsorted_dict (dict): . Defaults to {}.

    Returns:
        dict: sorted list of dictionaries where keys = ["char","num"] for 
    each character and their total count(s) respectively.
    """
    sorted_dicts = []
    for k, v in unsorted_dict.items():
        if k.isalpha() == True:
            sorted_dicts.append({"char": k, "num": v})

    sorted_dicts.sort(reverse=reverse, key=sort_on)
    return sorted_dicts

def sort_on(data:dict) -> int:
    """Helper function to return sort criteria for data.

    Args:
        data (dict): dictionary{str: int}

    Returns:
        int: value of the "num" key
    """
    return data["num"]

def get_word_count(book_contents:str) -> str:
    """Take str contents and return word count based on .split()

    Args:
        book_contents (str)

    Returns:
        str: formatted string with total word count
    """
    list_of_words = book_contents.split()
    num_words = len(list_of_words)
    return f"Found {num_words} total words"

def get_all_chars_counts(book_contents:str) -> dict:
    """Return dictionary of each character and a count of how many times
    it appeared in book_contents. EX: "A small Test1_+" -> {'a':2, 's':2, ' ':2, '+',}

    Args:
        book_contents (str)

    Returns:
        dict: dictionary{str: int}
    """
    results = {}

    for c in book_contents:
        lower_c = c.lower()
        if lower_c not in results.keys():
            results[lower_c] = 1
            continue 
        results[lower_c] += 1

    return results
