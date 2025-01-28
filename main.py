def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    sorted_chars = sorted(chars_dict.items(), key=sort_by_frequency, reverse=True)
    
    print(f"Total number of words: {num_words}")
    for char, freq in sorted_chars:
        print(f"The '{char}' character was found {freq} times.")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars


def sort_by_frequency(item):
    return item[1]


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()