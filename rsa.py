from pythonlibs.numbthy import *
from pythonlibs.primes import *


def rsa():
    # Alice create her public parameters
    # p=79; q=67; e=17; n=p*q;
    # Use large primes (256 and 512 bits)
    p = Primes.getRandomPrime()
    q = Primes.getRandomPrime()
    # p can be equals q
    # while(p == q):1
    #     q = Primes.getRandomPrime()

    n = p*q

    # Not use this validation because Numbthy.isSquareFree is very low with large numbers.
    # while(nth.isSquareFree(n) != True):#n MUST squarefree in RSA algorithm.
    #     p = Primes.getRandomPrime()
    #     q = Primes.getRandomPrime()
    #     n = p*q

    phi = (p-1)*(q-1)

    e = random.randint(1, phi)
    # Verify if e is coprime with p and q
    if(n % e == 0):
        e = random.randint(1, phi)

    d = xgcd(e, phi)[1]  # d = Alice compute secret decrypt exponent
    while d < 0:
        e = random.randint(1, phi)
        # d = Alice compute secret decrypt exponent
        d = xgcd(e, phi)[1]

    print(f"p: {p}")
    print('')
    print(f"q: {q}")
    print('')
    print(f"n: {n}")
    print('')
    print(f"e: {e}")
    print('')
    # print (f"Public key: {[n,e]}")
    print('')
    print(f"phi: {phi}")
    print('')
    print(f"d: {d}")
    # print(f"Private Key: {[n,d]}")
    print('')

    m = 111  # plain text
    print(f"Plain message {code_message(str(m))}")
    print('')
    print(f"Code plain message {m}")
    print('')
    c = pow(m, e, n)
    # print(f"Crypted message: {decode_message(c)}")
    # print('')
    print(f"Code crypted message: {c}")
    print('')

    m = pow(c, d, n)
    print(f"Alice decrypt message: {m}")
    print('')

# Code legible ASCII code message in numbers


def code_message(m):
    code_message = ''
    for char in enumerate(m):
        code_message += str(ord(char[1]))

    return code_message


# Code code message in legible ASCII message
def decode_message(code_message):
    m = ''
    for char in enumerate(code_message):
        m += str(chr(int(char[1])))

    return m


## run code ##
# m = "Hola como andas?"
# c = code_message(m)
# print(c)
# md = decode_message(c)
# print(md)
# r = "OK" if md == m else "ERROR"

rsa()
