from . import ec
from . import groups

def enc(pk: ec.G1Element, tag: bytes, message: bytes) -> bytes:
    print("enc")
    r1 = groups.random_Zq()
    r2 = groups.random_GT()
    c1 = r1 * ec.G1Generator()
    # compute c2 = e(pk, H(tag))^r1 * r2
    return message
    
def dec(signature: ec.G2Element, ciphertext: bytes) -> bytes:
    print("dec")

