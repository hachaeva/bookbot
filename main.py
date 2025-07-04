# take a filepath as input and return the contents of the file as a string

from stats import get_num_words
from stats import character_count_dict
from stats import sort_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(list,path,word_count):
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}...")
    print ("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print ("--------- Character Count -------")
    for character in list:
        if (character["char"].isalpha()):
            print (f"{character["char"]}: {character["num"]}")
    print ("============= END ===============")
    return


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    count_dict = character_count_dict(book_text)
    sorted_list = sort_count(count_dict)
    print_report(sorted_list,path,num_words)

main()