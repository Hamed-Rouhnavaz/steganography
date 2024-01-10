# steganography
#### Description:
This project is a script that implements steganography, which is the practice of hiding a message within another medium, in this case, an image file. Steganography allows for a message to be concealed so that unless you are specifically looking for it, you wouldn't know it exists. This script uses the Python Imaging Library (PIL), now known as Pillow, and the binascii module to achieve this.

Let's break down the script into its components to understand better how it works:

**Utility Functions:**

1. `rgb_to_hex(r, g, b)`: This function converts red, green, and blue color values into a hexadecimal string. This is useful in this instance to represent the color of a pixel compactly.

2. `hex_to_rgb(hexcode)`: This does the opposite, turning hexadecimal color values back into tuples of RGB (red, green, blue). This is necessary when we need to work with color values to encode or decode our message.

3. `str_to_bin(message)`: A string is converted into a binary representation using this function. Each character in the string is turned into bytes, and then to its binary form. This is crucial because it's the binary data that we'll actually be hiding within our image.

4. `bin_to_str(binary)`: As expected, this function reverses the
 process of `str_to_bin`, turning a binary string back into human-readable text.

5. `encode(hexcode, digit)`: Here, we start getting into the steganography part. This function takes a hexadecimal color value and a binary digit (0 or 1) and encodes that digit into the color value. It does this by altering the least significant bit of the color value.

6. `decode(hexcode)`: This retrieves the least significant bit that was encoded into a color value, essentially extracting the hidden data.

**Main Steganography Functions:**

1. `hide(filename, message)`: This is the heart of the script. It opens an image and loops through each pixel, modifying the color values in such a way that our message's binary data is encoded into those pixels. To signal the end of the message, a delimiter '1111111111111110' is added. The updated image is then saved.

2. `retr(filename)`: This function retrieves the hidden message from an image. It reads the modified color values, extracts the binary data, detects the delimiter to know where the message ends, and then converts that binary data back into a string.

**Main Procedure:**

The `main` function demonstrates how to use the `hide` and `retr` functions. An image file and message are passed to `hide`, which encodes the message into the image. Then, the `retr` function is used to extract the message from the same image.

**Detailed Workflow:**

When `hide` is called, it reads the original image and encodes the message's binary representation into the least significant bits of the image's color channels. To maintain the integrity of the image, only one bit of each color channel is altered, which is generally imperceptible to the naked eye.

Conversely, when `retr` is called on an image that contains a hidden message, it examines the least significant bits of each pixel's color channels. It collects these bits and assembles them into the original binary data corresponding to the hidden message. Once the end of the binary string is detected (marked by the delimiter), the binary string is converted back to text.

By using a delimiter, the script knows precisely where the hidden data stops, as images typically have large amounts of pixel data, but the message might be quite short in comparison. This makes the retrieval process efficient and accurate.

**Potential Applications:**

While this example is somewhat basic and meant for demonstrative purposes, similar techniques can be used for various applications, such as copyright marking, secret communications, or protecting information by hiding it in plain sight.

**Security and Limitations:**

While steganography can add a layer of security by obfuscation, it is not inherently secure against individuals who know to look for such hidden messages. Moreover, the method demonstrated is relatively simplistic and might be vulnerable to detection or loss of data through image compression or format conversion.

**Conclusion:**

This project is a fascinating example of how one can manipulate digital images to contain hidden messages. Through the use of utility and main functions, it can effectively hide and retrieve data within an image. This introduction to steganography showcases the elegant intertwining of computer science, cryptography, and image processing, giving the user a powerful tool for concealed communication. With this basic understanding and the code provided, users are equipped to explore the world of steganography further, develop it, and potentially adapt it for more robust applications.
