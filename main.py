from stats import *

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    counted_letters = kind_of_letters(text)
    print(f"Found {num_words} total words")
    print(counted_letters)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
