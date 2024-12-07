import re
print(re.search(r"[a-zA-Z]{5}", "a ghost"))

print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")

print(re.findall(r"\w{5,10}", "I really like strawberries"))

print(re.findall(r"\w{5,}", "I really like strawberries"))

print(re.search(r"s\w{,20}", "I really like strawberries"))

Output --
<re.Match object; span=(2, 7), match='ghost'>
<re.Match object; span=(2, 7), match='scary'>
['scary', 'ghost', 'appea']
['really', 'strawberri']
['really', 'strawberries']
<re.Match object; span=(14, 26), match='strawberries'>
