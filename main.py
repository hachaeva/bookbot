# take a filepath as input and return the contents of the file as a string

from stats import get_num_words
from stats import get_num_characters
from stats import character_count_dict
from stats import sort_count

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
    path = "./books/frankenstein.txt"
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    count_dict = character_count_dict(book_text)
    sorted_list = sort_count(count_dict)
    print_report(sorted_list,path,num_words)

main()