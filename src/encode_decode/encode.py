from sha256 import sha256
from b32 import base32e
from b64 import base64e
from vigenere import cypher
from salter import get_salt


def encode(mess: str, method: str = "sha", key: str = "crypt", salty: bool = True):
    if salty == True:
        salt = get_salt()
    else:
        salt = ""
    mess += salt
    if method == "sha" or method == "sha256":
        return f"sha256${salt}${sha256(mess)}"
    elif method == "base32" or method == "b32":
        return f"base32${salt}${base32e(mess)}"
    elif method == "base64" or method == "b64":
        return f"base64${salt}${base64e(mess)}"
    elif method == "vigenere" or method == "vig":
        return f"vig${salt}${cypher(mess, key)}"
    else:
        return "I can't currently encode with that method"
