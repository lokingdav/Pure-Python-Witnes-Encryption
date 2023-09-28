from . import ec
from collections import namedtuple
from .schemes import (PrivateKey, BasicSchemeMPL)

Keys = namedtuple('Keys', ['sk', 'pk'])

def key_gen(seed: bytes) -> Keys:
    sk: PrivateKey = BasicSchemeMPL.key_gen(seed)
    pk: ec.G1Element = sk.get_g1()
    
    return Keys(sk, pk)

def sign(sk: PrivateKey, message: bytes) -> ec.G2Element:
    signature: ec.G2Element = BasicSchemeMPL.sign(sk, message)
    
    return signature

def verify(pk: ec.G1Element, message: bytes, signature: ec.G2Element) -> bool:
    ok: bool = BasicSchemeMPL.verify(pk, message, signature)
    
    return ok