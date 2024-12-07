import re

def rearrange_name(name):
    result = re.search(r"^(\w+), (\w+)$", name)  # Use \w+ to ensure that there's at least one word character
    if result is None:
        return name
    return "{} {}".format(result.group(2), result.group(1))  # Access groups using group(1) and group(2)

# Test the function
print(rearrange_name("Ritchie, Dennis"))  # Expected: "Dennis Ritchie"