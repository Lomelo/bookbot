def main():
    book_path = "books/frankenstein.txt"
    contents = book_content(book_path)
    character_dictionary = create_char_dic(contents)
    count = word_count(contents)
    total_characters = character_count(character_dictionary)
    sorted_list = dict_list(character_dictionary)
    print(f"--- Begin report of {book_path} ---", f"{count} words found in the document")
    for i in sorted_list:
        print(f"The {i['char']} character was found {i["count"]} times")
    print("--- End Report ---")

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
        if lowered_letter not in letter_count and lowered_letter.isalpha() == True:
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
    return dictionary["count"]

def dict_list(dictionary):
    char_list = []
    for key, value in dictionary.items():
        char_dict = {"char": key, "count": value}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=grab_dict_number)
    return char_list


main()
