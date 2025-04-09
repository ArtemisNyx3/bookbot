from stats import get_num_words
from stats import get_character_frequency

def get_book_text(book_path: str) -> str:
    with open(book_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    print (f'{num_words} words found in the document')
    print(get_character_frequency(book_text))

if __name__ == '__main__':
    main()