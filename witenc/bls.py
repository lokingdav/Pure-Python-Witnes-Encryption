from collections import namedtuple

from . import utils
from .chianetbls import ec
from .chianetbls.schemes import (PrivateKey, BasicSchemeMPL)

Keys = namedtuple('Keys', ['sk', 'pk'])

def key_gen(seed: bytes) -> Keys:
    sk: PrivateKey = BasicSchemeMPL.key_gen(seed)
    pk: ec.G1Element = sk.get_g1()

    return Keys(sk, pk)

def sign(sk: PrivateKey, message: str) -> ec.G2Element:
    message = utils.to_bytes(message)

    signature: ec.G2Element = BasicSchemeMPL.sign(sk, message)

    return signature

def verify(pk: ec.G1Element, message: str, signature: ec.G2Element) -> bool:
    message = utils.to_bytes(message)
    ok: bool = BasicSchemeMPL.verify(pk, message, signature)

    return ok