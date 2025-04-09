from stats import get_num_words
from stats import get_character_frequency
from stats import sort_dict
import sys

def get_book_text(book_path: str) -> str:
    with open(book_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_count = sort_dict(get_character_frequency(book_text))

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print (f'Found {num_words} total words')

    print("--------- Character Count -------")
    for item in char_count:
        print(f"{item[0]}: {item[1]}")

    print("============= END ===============")



if __name__ == '__main__':
    main()