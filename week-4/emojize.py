'''import emoji
import sys

if len(sys.argv) != 2:
    sys.exit()

output = emoji.emojize( sys.argv[1], language='alias')
print(f"Output: {output}")'''

import emoji

x = input("Input: ")

output = emoji.emojize(x, language ='alias')
print(f"Output: {output}")
