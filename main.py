def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_chars(text)
    print("--- Begin report of",book_path," ---")
    print(f"{num_words} words found in the document")
    print(char_count)


def get_num_chars(text):
    text_lowered=text.lower()
    char_count = {}

    # Iterate through each character in the string
    for char in text_lowered:
        if char in char_count:
            char_count[char] += 1  # Increment the count if character already in dictionary
        else:
            char_count[char] = 1   # Initialize the count if character is not in dictionary

    return(char_count)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()