def get_books_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
        return print(file_contents)
    

get_books_text('/home/kali/bootdev/bookbot/books/frankenstein.txt')

#hello world
#hello github
