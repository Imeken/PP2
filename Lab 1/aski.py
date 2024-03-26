def shift_characters(address):
    shifted_address = ''
    for char in address:
        if char.isalpha():
            if char == 'z':
                shifted_char = 'a'
            elif char == 'Z':
                shifted_char = 'A'
            else:
                shifted_char = chr(ord(char) + 1)
        elif char.isdigit():
            if char == '9':
                shifted_char = '0'
            else:
                shifted_char = str(int(char) + 1)
        else:
            shifted_char = char 
        shifted_address += shifted_char
    return shifted_address

input_address = input()
shifted_address = shift_characters(input_address)
print(shifted_address)