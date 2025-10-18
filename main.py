def get_books_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
        return print(file_contents)
    

get_books_text('books/frankenstein.txt')

#hello world
#hello github
#hello if this works
