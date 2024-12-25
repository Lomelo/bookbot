def main():
    book_path = "books/frankenstein.txt"
    contents = book_content(book_path)
    count = word_count(contents)
    print(count)

def book_content(path):
    with open(path) as f:
        return f.read()

def word_count(contents):
    words = (contents).split()
    total = len(words)
    return total




main()
