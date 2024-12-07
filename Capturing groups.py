import re  # The Python "re" module provides regular expression support.
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada") 
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])