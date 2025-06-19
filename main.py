from stats import word_count,char_count,create_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



def main():
    if (len(sys.argv)!=2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text=get_book_text(sys.argv[1])
    count=word_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {len(count)} total words")
    print("--------- Character Count -------")
    count=char_count(text)
    capture=create_list(count)
    for item in capture:
        if item["char"].isalpha() ==False:
            continue
        else:
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

main()
    
