import re

def transform_record(record):
    # Add +1- before the phone number in the record
    new_record = re.sub(r'(\d{3}-\d{3}-\d{4}|\d{3}-\d{7})', r'+1-\1', record)
    return new_record

# Test cases
print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Expected: Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Expected: Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Expected: Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Expected: Charlie Rivera,+1-698-746-3357,Web Developer
