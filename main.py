path = "books/frankenstein.txt"    

def full_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents): 
    words = file_contents.split() # class 'list'
    count_word = len(words) 
    return count_word

def count_characters(file_contents):
    string = file_contents.lower()
    unique = set()
    for char in string:
        unique.add(char)
    chars = {key: 0 for key in unique}
    for char in string:   
        if char in chars:
            chars[char] += 1
    return chars

def dict_list(characters_count):
    chars = []
    for k, v in characters_count.items():
        chars.append({k: v})
    return chars   

def sort(results):
    for i in results:
        return i
    



def main():
    
    file_contents = full_text(path) 
    word_count = count_words(file_contents) 
    characters_count = count_characters(file_contents) # dict
    results = dict_list(characters_count)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")


main()

