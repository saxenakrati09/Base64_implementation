# Base64_implementation
Implementation of binary to text encoding "BASE64"

## Implement a BASE64 Encoder / Decoder
Base64 is a conversion logic for binary and text that has historically been used in basic authentications of e-mail and HTTP.
(Please refer to Wikipedia (https://en.wikipedia.org/wiki/Base64) for detailed specifications.)

## Specifications for running:
- "-i [FILENAME]" is required
- "-o [FILENAME]" is required
- For "-e" input, perform Base64 Encoding
- For "-d" input, perform Base64 Decoding
- For both "-e -d" input, perform Base64 Encoding
- if neither "-e" or "-d" are specified, perform Base64 Encoding

## Sample Run looks like this:
input.txt has text "Hello World"

- python index.py -i input.txt -o output.txt
- cat output.txt

output -> SGVsbG8gd29ybGQK

- python index.py -i output.txt -o revert.txt
- cat revert.txt

output -> Hello World
