from PIL import Image
import binascii

# Utility functions
def rgb_to_hex(r, g, b):
    # Convert RGB to hex.
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex_to_rgb(hexcode):
    # Convert hex to RGB.
    hexcode = hexcode.lstrip('#')
    return tuple(int(hexcode[i:i+2], 16) for i in (0, 2, 4))

def str_to_bin(message):
    # Convert a string to binary.
    binary = bin(int(binascii.hexlify(message.encode()), 16))
    return binary[2:]

def bin_to_str(binary):
    # Convert binary to string.
    message = binascii.unhexlify('%x' % (int('0b'+binary, 2)))
    return message.decode()

def encode(hexcode, digit):
    # Encode a single bit into the least significant bit of the hex value of a color channel.
    if hexcode[-1] in ('0', '1', '2', '3', '4', '5'):
        return hexcode[:-1] + digit
    return None

def decode(hexcode):
    # Decode the least significant bit of a hex value of a color channel to a bit.
    if hexcode[-1] in ('0', '1'):
        return hexcode[-1]
    return None

# Main functions for the steganography
def hide(filename, message):
    # Function to hide the message inside an image.
    # A delimiter ('1111111111111110') is added at the end of the message to indicate the end.
    img = Image.open(filename)
    binary = str_to_bin(message) + '1111111111111110'
    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()

        newData = []
        digit = 0
        for item in datas:
            if digit < len(binary):
                # If there is still data to hide, hide a bit in the current pixel.
                newpix = encode(rgb_to_hex(item[0], item[1], item[2]), binary[digit])
                if newpix is None:
                    newData.append(item)
                else:
                    newData.append(tuple(hex_to_rgb(newpix)) + (255,))
                    digit += 1
            else:
                newData.append(item)
        img.putdata(newData)
        img.save(filename, "PNG")
        return "Completed!"
    return "Incorrect image mode, couldn't hide"

def retr(filename):
    # Function to retrieve hidden message from an image.
    img = Image.open(filename)
    binary = ''

    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()

        for item in datas:
            # Retrieve hidden bits from the image.
            digit = decode(rgb_to_hex(item[0], item[1], item[2]))
            if digit is None:
                pass
            else:
                binary += digit
                if binary[-16:] == '1111111111111110':  # Detect the delimiter to stop.
                    return bin_to_str(binary[:-16])
        return bin_to_str(binary)
    return "Incorrect image mode, couldn't retrieve"

def main():
    # Example usage:
    # Hide a message
    hidden_message = hide('Your-image-path', 'This is a secret message.')
    print(hidden_message)  # Output: "Completed!" if successful

    # Retrieve a hidden message
    secret = retr('Your-image-path')
    print(secret)  # Output: "This is a secret message." if successful

if __name__ == "__main__":
    main()
