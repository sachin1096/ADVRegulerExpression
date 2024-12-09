import re

def multi_vowel_words(text):
    # Regular expression to match words with 3 or more consecutive vowels
    pattern = r'\b\w*[aeiouAEIOU]{3,}\w*\b'
    result = re.findall(pattern, text)
    return result

# Test cases
print(multi_vowel_words("Life is beautiful")) 
# Expected: ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# Expected: ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# Expected: ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# Expected: ['queue']

print(multi_vowel_words("Hello world!")) 
# Expected: []
