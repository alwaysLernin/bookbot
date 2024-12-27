all_lower = "abcdefghijklmnopqrstuvwxyz"
lowercase_dict = {key: 0 for key in all_lower}

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = get_char_count(text)
    #print(text)
    #print(count_words(text))
    #print(char_count)
    
    print(f"--- Begin report of {book_path}")
    print(f"{word_count} words found in the document")
    for key, value in char_count.items():
        print(f"The '{key}' character was found '{value}' times")



def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split(" ")
    return len(words)

def get_char_count(text):
    for l in text:
        lowered_string = l.lower()
        if lowered_string in lowercase_dict:
            lowercase_dict[lowered_string] += 1
    
    return lowercase_dict

    

main()
    