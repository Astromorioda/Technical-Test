def is_vowel(char):
    
    vowels = "aeiou"
    vowels_mayus = vowels.upper()
    
    if char in vowels or char in vowels_mayus:
        return True
    else:
        return False
