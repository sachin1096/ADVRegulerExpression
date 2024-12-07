import re

def rearrange_name(name):
    # Adjusting regex to make sure we match at least one character for both parts of the name
    result = re.search(r"^([\w \.-]+), ([\w \.-]+)$", name)  # Use \w+ to match one or more characters
    if result is None:
        return name  # If no match, return the original name
    return "{} {}".format(result.group(2), result.group(1))  # Access the groups correctly

# Test the function
print(rearrange_name("Hopper, Grace M."))  # Expected: "Grace M. Hopper"