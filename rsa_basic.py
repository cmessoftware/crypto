from pythonlibs.numbthy import *
from pythonlibs.primes import *

# Apply RSA lalgoritm with large prime numbers but without hash the message before encript


def rsa_basic():
    # Alice create her public parameters
    # p=79; q=67; e=17; n=p*q;
    # Use large primes (256 and 512 bits)
    # p = Primes.getRandomPrime()
    # q = Primes.getRandomPrime()

    # Use real 1024 bits primes
    p = 124685024020957187131200052801845902253969612546755920130553920454137689384135220545088499385393875408732815791924680272200615058698344676319151783905225321217494862219782119636646706988705771738741199721356711351347991881760506345758932607907362373588747448240305985449118370643422595871279522576863430861069
    q = 96429091131389215441405716329460352148044567118115970886965602798182629303949256848898060916535854529916599474419790683284395790612874044807272645138663834724378099864485742312775570849340297113530968971122960367136508115926791093578026435549165856716675977565872296628353668911539221556889349332132294997037

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

    e = 65537

    d = xgcd(e, phi)[1]  # d = Alice compute secret decrypt exponent
    # while d < 0:
    #     e = random.randint(1, phi)
    #     # d = Alice compute secret decrypt exponent
    #     d = xgcd(e, phi)[1]

    print(f"p: {hex(p)}")
    print(f'{len(str(p))} digits')
    print('')
    print(f"q: {hex(q)}")
    print(f'{len(str(q))} digits')
    print('')
    print(f"n: {hex(n)}")
    print(f'{len(str(n))} digits')
    print('')
    print(f"e: {bin(e)}")
    print('')
    # print (f"Public key: {[n,e]}")
    print('')
    print(f"phi: {hex(phi)}")
    print(f'{len(str(phi))} digits')
    print('')
    print(f"d: {hex(d)}")
    print(f'{len(str(d))} digits')
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

rsa_basic()
