from Exercise_Five import reverse_word

def is_palindrome(word: str):
    
    if word == reverse_word(word):
        return True
    else:
        return False

