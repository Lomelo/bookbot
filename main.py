def main():
    book_path = "books/frankenstein.txt"
    contents = book_content(book_path)
    count = word_count(contents)
    total_characters = character_count(contents)
    print(total_characters)

def book_content(path):
    with open(path) as f:
        return f.read()

def word_count(contents):
    words = contents.split()
    return len(words)

def character_count(contents):
    letter_count = {}
    total = 0
    for letter in (contents):
        lowered_letter = letter.lower()
        if lowered_letter not in letter_count:
            letter_count[lowered_letter] = 1
        elif lowered_letter in letter_count:
            letter_count[f"{lowered_letter}"] += 1
    for i in (letter_count):
        total += letter_count[i]
    return total

    




main()
