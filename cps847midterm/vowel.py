def hasVowel(word):
    "returns True or False if word has a vowel"

    vowels = ["a", "e", "i", "o", "u"]

    for vowel in vowels:
        if vowel in word:
            return True

    return False

def hasNumber(word):
    "returns True or False if word has a number"
    numbers= ["1","2","3","4","5","6","7","8","9","0"]

    for number in numbers:
        if number in word:
            return True
    return False