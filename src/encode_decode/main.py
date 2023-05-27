import sys
from getopt import getopt
from encode import encode
from decode import decode
from helper import func_check

argv = sys.argv[1:]

try:
    options, args = getopt(
        argv, "e:d:m:k:s:", ["encode=", "decode=", "method=", "key=", "salt="]
    )
except:
    print("No optinons specified!")

method = [y for i, [x, y] in enumerate(options) if (x == "-m" or x == "--method")]

method = method[0] if method else None

key = [y for i, [x, y] in enumerate(options) if (x == "-k" or x == "--key")]

key = key[0] if key else None

salty = [y for i, [x, y] in enumerate(options) if (x == "-s" or x == "--salt")]

salty = salty[0] if salty else True

encoded, decoded = None, None

for name, value in options:
    if name in ["-e", "--encode"]:
        params = func_check(method, key)
        encoded = encode(value, salty=salty, **params)
    elif name in ["-d", "--decode"]:
        params = func_check(method, key)
        decoded = decode(value, **params)

print(encoded) if encoded else None
print(decoded) if decoded else None

"""
values = [
    'Baszodj meg Robi!',
    'Ne pofazz hanem gypgyulj meg te gyoker.',
    'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book',
    'Why do we use it?',
    'The quick brown fox jumps over the lazy dog',
    'Hello World!',
    'BuziRobi',
    'asdasdasdasd',
    'Lorem Ipsum',
    'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...'
]

for i in values:
    print(i)
    print(encode(i, method='b32'), 'base32')
    print(encode(i, method='b64'), 'base64')
    print(encode(i, method='sha'), 'sha')
    print()
"""
