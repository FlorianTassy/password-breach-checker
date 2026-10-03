import string
import math

FAMILY_SIZE = {
    "lower": 26,  # from a to z
    "upper": 26,  # from A to Z
    "digit": 10,  # from 0 to 9
}

def family_of(char):
    if char in string.ascii_lowercase:
        return "lower"
    if char in string.ascii_uppercase:
        return "upper"
    if char in string.digits:
        return "digit"
    return "other"

def families(password):
    found = []
    for char in password:
        family = family_of(char)
        if family not in found:
            found.append(family)
    return found

def characters_pool_size(password):
    total = 0
    for family in families(password):
        total += FAMILY_SIZE[family]
    return total

def naive_entropy(password):
    if len(password) == 0:
        return 0
    return len(password) * math.log2(characters_pool_size(password))
