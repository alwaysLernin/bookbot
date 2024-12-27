def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words(text)
    #print(text)
    print(count_words(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    word_count = 0
    words = text.split(" ")
    #word_count += len(words)
    return len(words)

main()
    