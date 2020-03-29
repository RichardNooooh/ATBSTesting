#this is broken.
def hash_val(s: str) -> int:
    modulus = 1000000007
    hash_sum = 0
    for i, char in enumerate(s):
        hash_sum += (((ord(char) - ord('a')) * 26 ** i) % modulus) % modulus

    return hash_sum


def suffix_val(s: str, prefix_hash: int, offset: int) -> int:
    modulus = 1000000007
    ind_of_next = len(s) - offset
    ind_to_rem = 0
    prefix_hash %= modulus
    while ind_of_next < len(s):
        prefix_hash = (prefix_hash - (ord(s[ind_to_rem]) - ord('a')) % modulus) % modulus
        prefix_hash = (prefix_hash * 26 % modulus) % modulus
        prefix_hash = (prefix_hash + ((ord(s[ind_of_next]) - ord('a')) * 26 ** (len(s) - offset - 1)) % modulus) % modulus
        ind_to_rem += 1
        ind_of_next += 1
    return prefix_hash


def longestPrefix(s: str) -> str:
    for offset in range(1, len(s)):
        result_str = s[:len(s) - offset]
        prefix_hash = hash_val(result_str)
        suffix_hash = suffix_val(s, prefix_hash, offset)
        if suffix_hash == prefix_hash:
            return result_str

    return ""





print(longestPrefix("aaaabdaaaa"))
