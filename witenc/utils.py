from datetime import datetime
from .bls import util

def hash256(m):
    return util.hash256(m)

def to_bytes(data) -> bytes:
    return bytes(data, 'utf-8')

def to_str(data: bytes) -> str:
    return bytes(data).hex()

def tuple_to_str(items, delimeter=";") -> str:
    chunks = []
    
    for item in items:
        chunks.append(to_str(item))
        
    return delimeter.join(chunks)

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

def bit_len(data):
    return data.bit_length() // 8 + 1
