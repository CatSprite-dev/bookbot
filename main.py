def main():
    with open("book/frankenstein.txt") as f:
        file_contents = f.read()    
        
        words = file_contents.split() # class 'list'
        count_words = len(words) 
        print(count_words)
        
        string = file_contents.lower()
        unique = set()
        for char in string:
            unique.add(char)
            chars = {key: 0 for key in unique}
        for char in string:   
            if char in chars:
                chars[char] += 1
        print(chars)

        
        
        

        


main()
