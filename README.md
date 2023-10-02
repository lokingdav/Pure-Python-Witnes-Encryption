# Witness Encryption based on BLS signatures

Implements a signature based witness encryption scheme based on the BLS signatures.

Uses the following implementations from [Chia-Network/bls-signatures](https://github.com/Chia-Network/bls-signatures/tree/main/python-impl)
- BLS12 curve and optimal ate pairing
- BLS signatures
- Other useful helper methods

## Installation
Requires Python ```3.8``` or later
```bash
pip install witenc
```

## Import the library
```python
from witenc import bls, utils, encrypt, decrypt
```

## Generate Keys
```python
# Example seed, used to generate private key. Always use
# a secure RNG with sufficient entropy to generate a seed (at least 32 bytes).
seed: bytes = bytes([0,  50, 6,  244, 24,  199, 1,  25,  52,  88,  192,
                        19, 18, 12, 89,  6,   220, 18, 102, 58,  209, 82,
                        12, 62, 89, 110, 182, 9,   44, 20,  254, 22])

# Generate secret key and public key
sk, pk = bls.key_gen(seed)
```

## Export and Import Secret keys
```python
# Export and import secret key
sk = utils.export_sk(sk) # only when storing, default type is 'hex'
sk = utils.import_sk(sk) # only when loading, default type is 'hex'
```

## Export and Import Public Keys
```python
# Export and import public key
pk = utils.export_pk(pk) # only when storing, default type is 'hex'
pk = utils.import_pk(pk) # only when loading, default type is 'hex'
```

The ```export_*``` and ```import_*``` funtions accept a ```type``` parameter that specifies the output encoding (```hex```, ```bytes```). 
The default is ```hex``` and the only implemented now.

## Sign a message
```python
# Tag to be signed, it's signature is required for decrypting the message
tag: str = 'tag'

# Message to be encrypted
message: str = 'Hello, world!'

# Sign the tag
signature = bls.sign(sk, tag)
```
## Export and Import Signatures
```python
# Export and import signature
signature = utils.export_sig(signature) # only when storing, default type is 'hex'
signature = utils.import_sig(signature) # only when loading, default type is 'hex'
```

## Verify Signature
```python
# Verify the signature
ok: bool = bls.verify(pk, tag, signature)
assert ok
print("Signature verified")
```

## Encrypt and Decrypt Message with a tag
```python
# Encrypt the message
ciphertext: str = encrypt(pk, tag, message)
print("Ciphertext:\n" + ciphertext)

# Decrypt the message
decrypted_message: str = decrypt(signature, ciphertext)

assert message == decrypted_message
print("Decrypted message\n" + decrypted_message)
```

Full example can be found in [example.py](https://github.com/kofi-dalvik/witenc/blob/master/example.py).

## Witenc license

Witenc uses code from [Chia-Network/bls-signatures](https://github.com/Chia-Network/bls-signatures/tree/main) and licensed under the
[Apache 2.0 license](https://github.com/kofi-dalvik/witenc/blob/master/LICENSE)