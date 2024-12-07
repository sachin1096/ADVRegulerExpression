import re

def rearrange_name(name):
    # Use \w+ to ensure at least one character in both name parts
    result = re.search(r"^(\w+), (\w+)$", name)
    if result is None:
        return name  # Return the original name if it doesn't match the pattern
    # Return the rearranged name (first name, last name)
    return "{} {}".format(result.group(2), result.group(1))

# Test the function
print(rearrange_name("Lovelace, Ada"))
