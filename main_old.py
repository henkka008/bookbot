#!/bin/python3
def get_books_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
        return print(file_contents)
    

#get_books_text('books/frankenstein.txt')

def count_book_words(filePath):
    with open(filePath) as f:
        file_contents = f.read()
        words = file_contents.split()
        total = 0
        for word in words:
            total += 1
        return print(f"Found {total} total words")

count_book_words('books/frankenstein.txt')
