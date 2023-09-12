import random
import string

def generate_serial_keys(num_keys):
    serial_keys = set()
    
    while len(serial_keys) < num_keys:
        # Generate Stack+-8Digits
        prefix = input("Enter the first 4-8 letters of the serial key(Letters and numbers only): ")
        digits = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        key = prefix + digits
        
        # Generate 4Digits (1-9)
        suffix = ''.join(random.choices(string.digits[1:], k=4))
        key += '-' + suffix
        
        serial_keys.add(key)
    
    return serial_keys

def save_serial_keys(serial_keys, file_path):
    with open(file_path, 'w') as file:
        for key in serial_keys:
            file.write(key + '\n')

# Example usage
num_keys = int(input("Enter the number of serial keys to generate: "))
file_path = input("Enter the file path to save the serial keys (including the filename and extension): ")

keys = generate_serial_keys(num_keys)
save_serial_keys(keys, file_path)

print(f"{num_keys} unique serial keys generated and saved to {file_path}.")