import string
import math

def count_uppercase(s):
    return sum([1 for x in s if x in string.ascii_uppercase])

def count_lowercase(s):
    return sum([1 for x in s if x in string.ascii_lowercase])

def count_digit(s):
    return sum([1 for x in s if x in string.digits])

def check_strength(s):
    if len(s) < 8:
        return False
    
    min_count = math.ceil(len(s) / 4)
    
    if count_uppercase(s) < min_count:
        return False
    
    if count_lowercase(s) < min_count:
        return False
    
    if count_digit(s) < min_count:
        return False
    
    return True

if __name__ == '__main__':
    import sys
    words = [word for word in sys.argv[1].split(',') if len(word) > 0]
    
    score = sum([1 for word in words if check_strength(word) == True]) / len(words)
    
    print(score)
    