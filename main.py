from stats import *
import sys


def main():

    file_input = None
    if len(sys.argv) == 2:
        file_input = sys.argv[1]
    else:
        sys.exit("Usage: python3 main.py <path_to_book>")

    
    file_path = file_input
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    counted_letters = kind_of_letters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_letters = sorting(counted_letters)
    print(sorted_letters)
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
