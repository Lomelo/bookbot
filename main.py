def main():
    book_path = "books/frankenstein.txt"
    contents = book_content(book_path)
    character_dictionary = create_char_dic(contents)
    count = word_count(contents)
    total_characters = character_count(character_dictionary)
    print(report(book_path, count, contents))

def book_content(path):
    with open(path) as f:
        return f.read()

def word_count(contents):
    words = contents.split()
    return len(words)

def create_char_dic(contents):
    letter_count = {}
    for letter in (contents):
        lowered_letter = letter.lower()
        if lowered_letter not in letter_count:
            letter_count[lowered_letter] = 1
        elif lowered_letter in letter_count:
            letter_count[f"{lowered_letter}"] += 1
    return letter_count

def character_count(dictionary):
    total = 0
    for i in (dictionary):
        total += dictionary[i]
    return total

def grab_dict_number(dictionary):
    return dictionary["p"]

def report(path, word_count, contents):
    headline = f"Begin report of {path}"
    provide_word_total = f"{word_count} words found in the document"
    return headline, provide_word_total


main()
