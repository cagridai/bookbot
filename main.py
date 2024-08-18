def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    report = set_report(num_char)
    
    for c in report:
        print(f"The '{c['name']}' character was found {c['num']} times")
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
    
def get_num_char(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    
    return chars

def sort_on(dict):
    return dict["num"]

def set_report(chars):
    char_list = []
    for c in chars:
        if c.isalpha():
            char_list.append({"name": c, "num": chars[c]})
            
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
            

main()