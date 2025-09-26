import os
import sys

from stats import get_word_count, get_all_chars_counts, sort_all_char_data

def get_book_text(file_path:str=None):
    fd = os.open(file_path, os.O_RDONLY, 0o644) 
    file_size = os.fstat(fd).st_size
    content = os.pread(fd, file_size, 0).decode('utf-8')
    os.close(fd)
    return content

def generate_report(sorted_data, file_path, word_count):
    """Generate a report str for console output.

    Arguments:
        - sorted_data(dict): dictionary of k=char and v=count. EX: {'c':101}
        - file_path(str): /path/to/file 
        - word_count(int): total word count

    Returns:
        report_str(str): formatted str based on args.
    """

    report_str = "============ BOOKBOT ============\n" + \
                 f"Analyzing book found at {file_path}...\n" + \
                 "----------- Word Count ----------\n" + \
                 f"Found {word_count} total words\n" + \
                 "--------- Character Count -------\n"
    for d in sorted_data:
        report_str += f"{d['char']}: {d['num']}\n"
    report_str += "============= END ==============="
    return report_str


if __name__=="__main__":

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Static relative path variable
    relative_file_path = sys.argv[1]
    
    # Get the following:
    # Book Contents
    # Word Count
    # Count of all characters (and sort by count, greatest to least)
    book_contents = get_book_text(relative_file_path)
    word_count = get_word_count(book_contents)
    all_char_data = get_all_chars_counts(book_contents)
    sorted_char_data = sort_all_char_data(all_char_data)

    # Generate report
    report = generate_report(sorted_char_data, relative_file_path, word_count)

    # Output
    print(report)
