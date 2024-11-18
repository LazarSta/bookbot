def main():
    bookPath = "books/frankenstein.txt"
    text = get_book_text(bookPath)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    list_of_letters = convert_dict(letter_count)

    print("--- Begin report of " + bookPath)
    print(f"{num_words} words found in the document")
    print("")
    for entry in list_of_letters:
        print(f"The character {entry["char"]} was found {entry["num"]} times")
    print("--- End report ---")
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text):
    text = text.lower()
    letter_count = {}
    for c in text:
        if c in letter_count:
            letter_count[c] += 1
        else:
            letter_count[c] = 1
    return letter_count

def convert_dict(dictionary):
    list = []
    for each in dictionary:
        if each.isalpha():
            list.append({"char": each, "num": dictionary[each]})
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dict):
    return dict["num"]

main()