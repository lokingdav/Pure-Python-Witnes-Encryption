from collections import namedtuple

from . import utils
from .bls import ec
from . import groups
from .bls import fields
from .bls import pairing
from .bls.op_swu_g2 import g2_map
from .bls.schemes import basic_scheme_dst

delimeter = ';'
byteorder = 'big'

def enc(pk: ec.G1Element, tag: str, message: str) -> str:
    tag = utils.to_bytes(tag)
    r1 = groups.random_Zq()
    r2 = groups.random_GT()
    c1 = r1 * ec.G1Generator()
    
    h = utils.hash256(bytes(r2))
    gt = pairing.ate_pairing(pk, g2_map(tag, basic_scheme_dst)) ** r1
    
    c2 = bytes(gt * r2)
    c3 = encode_msg(message, h)
    ciphertext = utils.tuple_to_str((c1, c2, c3), delimeter)
    
    return ciphertext
    
def dec(signature: ec.G2Element, ciphertext: str) -> str:
    c1, c2, c3 = parse_ciphertext(ciphertext)
    c1 = ec.G1FromBytes(c1)
    c2 = fields.Fq12.from_bytes(buffer=c2, Q=ec.default_ec.q)
    
    r2 = c2 / pairing.ate_pairing(c1, signature)
    
    h = utils.hash256(bytes(r2))
    message = decode_msg(c3, h)

    return message

def parse_ciphertext(ciphertext: str):
    c1, c2, c3 = ciphertext.split(delimeter)
    return bytes.fromhex(c1), bytes.fromhex(c2), c3

def encode_msg(message: str, hash) -> str:
    message = utils.to_int(message)
    hash = utils.to_int(hash)
    c3 = (hash + message) % ec.default_ec.n
    c3 = c3.to_bytes(utils.bit_len(c3), byteorder)
    return c3

def decode_msg(c3: str, hash) -> str:
    c3, hash = int(c3, 16), utils.to_int(hash)
    message = (c3 - hash) % ec.default_ec.n
    message = message.to_bytes(utils.bit_len(message), byteorder)
    return message.decode()