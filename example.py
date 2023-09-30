from witenc import bls, witenc, utils

# Example seed, used to generate private key. Always use
# a secure RNG with sufficient entropy to generate a seed (at least 32 bytes).
seed: bytes = bytes([0,  50, 6,  244, 24,  199, 1,  25,  52,  88,  192,
                        19, 18, 12, 89,  6,   220, 18, 102, 58,  209, 82,
                        12, 62, 89, 110, 182, 9,   44, 20,  254, 22])

# Generate private key and public key
sk, pk = bls.key_gen(seed)

# Export and import secret key
sk = utils.export_sk(sk) # only when storing, default type is 'hex'
sk = utils.import_sk(sk) # only when loading, default type is 'hex'

# Export and import public key
pk = utils.export_pk(pk) # only when storing, default type is 'hex'
pk = utils.import_pk(pk) # only when loading, default type is 'hex'

# Tag to be signed, it's signature is required for decrypting the message
tag: str = 'tag'
# Message to be encrypted
message: str = 'Hello, world!'

# Sign the tag
signature = bls.sign(sk, tag)

# Export and import signature
signature = utils.export_sig(signature) # only when storing, default type is 'hex'
signature = utils.import_sig(signature) # only when loading, default type is 'hex'

# Verify the signature
ok: bool = bls.verify(pk, tag, signature)
assert ok
print("Signature verified")

# Encrypt the message
ciphertext: str = witenc.enc(pk, tag, message)

# Decrypt the message
decrypted_message: str = witenc.dec(signature, ciphertext)

assert message == decrypted_message
print("Decrypted message\n" + decrypted_message)
