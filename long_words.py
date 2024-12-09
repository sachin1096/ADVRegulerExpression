import re

def long_words(text):
    # Regular expression to match words with at least 7 characters
    pattern = r'\b\w{7,}\b'
    result = re.findall(pattern, text)
    return result

# Test cases
print(long_words("I like to drink coffee in the morning."))  # Expected: ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon."))  # Expected: ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night."))  # Expected: []
