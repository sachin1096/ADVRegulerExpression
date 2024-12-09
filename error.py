import re

def extract_pid(log_line):
    # Updated regular expression to capture both PID and uppercase message
    regex = r"\[(\d+)\]:\s([A-Z]+)"
    result = re.search(regex, log_line)
    
    if result is None:
        return None
    
    # Return the PID and the uppercase message
    return "{} ({})".format(result.group(1), result.group(2))

# Test cases
print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) 
# Expected: "12345 (ERROR)"
print(extract_pid("99 elephants in a [cage]")) 
# Expected: None (No PID or uppercase message)
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) 
# Expected: None (No uppercase message)
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) 
# Expected: "67890 (RUNNING)"
