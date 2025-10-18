from stats import *

def main():
    file_path = "books/frankenstein.txt"
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
