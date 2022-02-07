# There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.
# A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. 
# "whi" is a triplet for the string "whatisup".
# As a simplification, you may assume that no letter occurs more than once in the secret string.
# You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string.
# In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.




def recoverSecret(triplets):
    secret = ''
    secret_dict = {}
    for x in triplets:
        for y in x:
            secret_dict.setdefault(y, set()).update(x[x.index(y) - 1]) if x.index(y) != 0 else secret_dict.setdefault(y, set())

    def removeChar(c) -> dict:
        '''find first char in secret'''
        {v.remove(c) for k, v in secret_dict.items() if c in v}

    def findChar() -> str:
        '''find first char in secret when there is no char in front of it'''
        return next(k for k, v in secret_dict.items() if not v)

    while secret_dict:
        first_char = findChar()
        secret_dict = {k: v for k, v in secret_dict.items() if k != first_char}
        removeChar(first_char)
        secret = secret + first_char
    return secret

secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))