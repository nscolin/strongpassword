import secrets

class StrongPasswordGenerator:
    def __init__(self):
        pass
    
    def generate_random_string(self, length=16):
        # Calculate the number of bytes needed
        num_bytes = (length + 1) // 2

        # Generate a random hexadecimal string
        random_hex_string = secrets.token_hex(num_bytes)

        # Trim the string to the desired length
        random_string = random_hex_string[:length]

        return random_string

# Generate a random strong password of length 16 (with default constructor):
random_string_default_generator = StrongPasswordGenerator()
random_string = random_string_default_generator.generate_random_string()
print("Random String (length default):", random_string)

random_string_user_generator = StrongPasswordGenerator()
random_string1 = random_string_user_generator.generate_random_string(length=12)
print("Random String (length 12):", random_string1)