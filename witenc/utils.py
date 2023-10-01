from datetime import datetime

from .chianetbls import ec
from .chianetbls import util
from .chianetbls.private_key import PrivateKey

def hash256(m):
    return util.hash256(m)

def to_bytes(data) -> bytes:
    return bytes(data, 'utf-8')

def to_str(data: bytes) -> str:
    if type(data) is bytes:
        return data.hex()

    return bytes(data).hex()

def tuple_to_str(items, delimeter=";") -> str:
    chunks = []

    for item in items:
        chunks.append(to_str(item))

    string = delimeter.join(chunks)

    return to_bytes(string).hex()

def to_int(data: bytes) -> int:
    if type(data) is not bytes:
        data = to_bytes(data)

    return int.from_bytes(data, 'big')

def timed(func):
    def wrapped(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(f'--> {func.__name__} finished in {get_elapsed_time(start)} seconds')
        return result
    return wrapped

def get_elapsed_time(start):
    return round((datetime.now() - start).total_seconds(), 2)

def size_in_bytes(data):
    return data.bit_length() // 8 + 1

def export_sk(sk: PrivateKey, type: str = 'hex') -> bytes:
    if not isinstance(sk, PrivateKey):
        raise TypeError('sk must be of type PrivateKey')

    sk = bytes(sk)

    if type == 'hex':
        return sk.hex()

    return sk

def import_sk(sk, type: str = 'hex') -> PrivateKey:
    if isinstance(sk, PrivateKey):
        return sk

    if isinstance(sk, bytes):
        return PrivateKey.from_bytes(sk)

    if isinstance(sk, str):
        sk = bytes.fromhex(sk) if type == 'hex' else sk.encode('utf-8')
        return PrivateKey.from_bytes(sk)

    raise TypeError('sk must be of type PrivateKey, bytes, or str')

def export_pk(pk: ec.G1Element, type: str = 'hex') -> bytes:
    if not isinstance(pk, ec.G1Element):
        raise TypeError('pk must be of type G1Element')

    pk = bytes(pk)

    if type == 'hex':
        return pk.hex()

    return pk

def import_pk(pk, type: str = 'hex') -> ec.G1Element:
    if isinstance(pk, ec.G1Element):
        return pk

    if isinstance(pk, bytes):
        return ec.G1FromBytes(pk)

    if isinstance(pk, str):
        pk = bytes.fromhex(pk) if type == 'hex' else pk.encode('utf-8')
        return ec.G1FromBytes(pk)

    raise TypeError('pk must be of type G1Element, bytes, or str')

def export_sig(sig: ec.G2Element, type: str = 'hex') -> bytes:
    if not isinstance(sig, ec.G2Element):
        raise TypeError('sig must be of type G2Element')

    sig = bytes(sig)

    if type == 'hex':
        return sig.hex()

    return sig

def import_sig(sig, type: str = 'hex') -> ec.G2Element:
    if isinstance(sig, ec.G2Element):
        return sig

    if isinstance(sig, bytes):
        return ec.G2FromBytes(sig)

    if isinstance(sig, str):
        sig = bytes.fromhex(sig) if type == 'hex' else sig.encode('utf-8')
        return ec.G2FromBytes(sig)

    raise TypeError('sig must be of type G2Element, bytes, or str')
