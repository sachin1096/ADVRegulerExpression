import re

def rearrange_name(name):
    # Updated regex to match last names with middle names, initials, and double surnames
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name  # Return original name if no match
    # Return first name first, then last name
    return "{} {}".format(result.group(2), result.group(1))

# Test the function
name = rearrange_name("Kennedy, John F.")
print(name)  # Expected: "John F. Kennedy"

# Additional test cases:
print(rearrange_name("Smith-Jones, Alice Marie"))  # Expected: "Alice Marie Smith-Jones"
print(rearrange_name("de la Cruz, Juan Carlos"))  # Expected: "Juan Carlos de la Cruz"
print(rearrange_name("Gonzalez, Maria"))  # Expected: "Maria Gonzalez"